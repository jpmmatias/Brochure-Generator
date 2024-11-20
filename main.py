from typing import List
from OpenAi import OpenAiService
from Brouchure import Brouchure


print("Starting the application...")

print("What is the company name?")
company_name = str(input())

print("What is the company URL?")
url = str(input())

print("Want to generate a markdown file? (y/n)")
generate_markdown_file = input() == "y"

print("What sections do you want to include? If you don't know, just press enter (comma separated list)")
sections = input().split(",")

print("What language do you want the brochure in? (e.g. en, es, fr, etc.)")
language = str(input())

print("Generating the brochure...")

openAiService = OpenAiService()

brouchure = Brouchure(company_name=company_name,url=url, openAiService=openAiService, sections=sections, language=language)

brouchure.create_brochure(generate_markdown_file=generate_markdown_file)

print("Done!")