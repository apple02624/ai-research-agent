import os
from openai import OpenAI
from dotenv import load_dotenv
from utils.prompts import SUMMARY_PROMPT

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_research(text):

    prompt = SUMMARY_PROMPT.format(text=text)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text