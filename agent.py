import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

from memory import get_similar, save_memory, init_db
from evaluator import evaluate_answer


# Load environment variables
load_dotenv()

# Create client
client = OpenAI(api_key=os.getenv("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"))

# Init DB
init_db()


def call_ai(prompt: str) -> str:

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


def ask_ai(prompt: str) -> str:
    """
    Main agent function
    """

    past = get_similar(prompt)

    memory_text = ""

    for q, fb in past:
        memory_text += f"- Q: {q}\n  Feedback: {fb}\n"

    final_prompt = f"""
Learn from past mistakes:

{memory_text}

Now answer clearly:

{prompt}
"""

    answer = call_ai(final_prompt)

    # Self review
    review = evaluate_answer(prompt, answer, call_ai)

    score = 7  # (Later we will auto-parse this)

    feedback = review

    save_memory(prompt, answer, feedback, score)

    return answer
