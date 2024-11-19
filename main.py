from typing import List
from OpenAi import OpenAiService
from Brouchure import Brouchure


print("Starting the application...")

print("What is the company name?")
company_name = input()

print("What is the company URL?")
url = input()

print("Want to generate a markdown file? (y/n)")
generate_markdown_file = input() == "y"
    
openAiService = OpenAiService()

brouchure = Brouchure(company_name=company_name,url=url, openAiService=openAiService)

brouchure.create_brochure(generate_markdown_file=generate_markdown_file)
