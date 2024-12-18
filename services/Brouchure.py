from services.Website import Website
from services.OpenAi import OpenAiService
import uuid

class Brouchure:
    def __init__(self, company_name: str, url: str, openAiService: OpenAiService, sections: list[str], language: str) -> None:
        if not sections:
            sections = ["About", "Company Culture", "Our Customers", "Connect with Us", "Our Offerings", "Our Mission", "Our Values", "Our Events"]
        self.website = Website(url=url, openAiService=openAiService)
        self.company_name = company_name
        self.open_ai = openAiService
        self.url = url
        self.id = str(uuid.uuid4())
        self.language = language
        self.system_prompt  = f"You are an assistant that analyzes the contents of several relevant pages from a company website \
and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown.\
The brochure should be in {language.replace(' ', '')} and include the following sections: {', '.join(sections)} if you have the information."

    def get_all_details(self):
        links = self.website.get_links()
        result = "Landing page:\n"
        result += self.website.get_contents()
        for link in links["links"]:
            result += f"\n\n{link["type"]}\n"
            result += Website(url=link["url"], openAiService=self.open_ai).get_contents()
        return result
    
    def __get_brouchure_user_prompt(self):
        user_prompt = f"You are looking at a company called: {self.company_name}\n"
        user_prompt += f"Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
        user_prompt += self.get_all_details()
        user_prompt = user_prompt[:20_000]
        return user_prompt
    
    def create_brochure(self, generate_markdown_file=False):
        response = self.open_ai.get_chat_completion(self.system_prompt, self.__get_brouchure_user_prompt())
        if generate_markdown_file:
            self.create_brouchure_markdown_file(response)
        return response.replace("```markdown","")
    
    def create_brouchure_markdown_file(self, response):
        with open(f"generated/{self.company_name}_{self.language}_{self.id}.md", "w") as file:
            file.write(response)
