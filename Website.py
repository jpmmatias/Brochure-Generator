from bs4 import BeautifulSoup
import requests
from OpenAi import OpenAiService

class Website:
    def __init__(self, url:str, openAiService: OpenAiService):
        self.url = url
        self.openAiService = openAiService 
        response = requests.get(url)
        self.body = response.content
        soup = BeautifulSoup(self.body, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = ""
        links = [link.get('href') for link in soup.find_all('a')]
        self.links = [link for link in links if link]

    def get_contents(self):
        return f"Webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n"

    
    def get_links(self):
        response = self.openAiService.get_chat_completion(self.__get_links_system_prompt(), self.__get_links_user_prompt())
        return response

    def __get_links_user_prompt(self):
        user_prompt = f"Here is the list of links on the website of {self.url} - "
        user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. \
            Do not include Terms of Service, Privacy, email links.\n"
        user_prompt += "Links (some might be relative links):\n"
        user_prompt += "\n".join(self.links)
        return user_prompt

    def __get_links_system_prompt(self):
        link_system_prompt = "You are provided with a list of links found on a webpage. \
            You are able to decide which of the links would be most relevant to include in a brochure about the company, \
            such as links to an About page, or a Company page, or Careers/Jobs pages.\n"
        link_system_prompt += "You should respond in JSON as in this example:"
        link_system_prompt += """
            {
            "links": [
                {"type": "about page", "url": "https://full.url/goes/here/about"},
                {"type": "careers page": "url": "https://another.full.url/careers"}
            ]
            }
        """
        return link_system_prompt