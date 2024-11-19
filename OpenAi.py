from openai import OpenAI
import os
from dotenv import load_dotenv
import json
from typing import Union

class OpenAiService:
    def __init__(self) -> None:
        load_dotenv()
        self.open_ai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.model = 'gpt-4o-mini'

    def get_chat_completion(self, system_prompt: str, user_prompt: str) -> Union[dict, str]:
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ] 
        isJson = "JSON" in system_prompt or "json" in system_prompt

        response_format = {"type": "json_object"} if isJson else {"type": "text"}
        response = self.open_ai.chat.completions.create(
        model=self.model,
        messages=messages,
        response_format=response_format
        )

        result = response.choices[0].message.content
        return  json.loads(result) if isJson else result