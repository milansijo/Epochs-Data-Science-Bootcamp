import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_answer(context, question, history=""):
    """
    Generate an answer using the retrieved context.
    """

    prompt = f"""
You are an AI Study Assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context, reply:
"I couldn't find the answer in the uploaded document."

Conversation History:
{history}

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text