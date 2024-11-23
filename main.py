from typing import List
from services.OpenAi import OpenAiService
from services.Brouchure import Brouchure
from gradio import gradio as gr


def generate_brochure(company_name: str, url: str, generate_markdown: bool, sections: str, language: str, stream: bool):
    sections_list = [s.strip() for s in sections.split(",")] if sections.strip() else []
    openAiService = OpenAiService()
    brouchure = Brouchure(
        company_name=company_name,
        url=url,
        openAiService=openAiService,
        sections=sections_list,
        language=language
    )
    print("generating brouchure..") 
    
    return "".join(brouchure.create_brochure(generate_markdown_file=generate_markdown))

demo = gr.Interface(
    fn=generate_brochure,
    inputs=[
        gr.Textbox(label="Company Name"),
        gr.Textbox(label="Company URL"),
        gr.Checkbox(label="Generate Markdown File"),
        gr.Textbox(label="Sections (comma-separated)", placeholder="Leave empty for default sections"),
        gr.Textbox(label="Language", placeholder="en", value="en"),
    ],
    outputs=[gr.Markdown(label="Generated Brochure")],
    title="Company Brochure Generator",
    description="Generate a company brochure using AI",
    flagging_mode="never"
)

demo.launch()   
