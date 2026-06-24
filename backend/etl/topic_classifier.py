import os

from groq import Groq

from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

ALLOWED_TOPICS = [

    "Technology",

    "Politics",

    "Business",

    "Sports",

    "Science",

    "Health",

    "Entertainment",

    "World News"
]


def classify_topic(text):

    text = text[:1500]

    prompt = f"""
You are a news classifier.

Choose EXACTLY ONE category.

Categories:

Technology
Politics
Business
Sports
Science
Health
Entertainment
World News

Return ONLY the category name.

Article:

{text}
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )

    topic = (
        response
        .choices[0]
        .message
        .content
        .strip()
    )

    if topic not in ALLOWED_TOPICS:

        return "World News"

    return topic