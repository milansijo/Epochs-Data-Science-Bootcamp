PROMPTS={
"Explain Topic":
"""You are an expert teacher.

Explain the following topic for a college student.
Requirements:
-Use simple language.
-Explain step by step.
-Include a real-world example.
-Mention important concepts.
-End with a short summary

Topic:
{topic}
""",

    "Generate Notes":"""
    You are an expert educator.
    Create structured study notes on the following topic.

    Requirements:
    -Use headings.
    -Use bullet points.
    -Include imporrtant definitions.
    -Mention exam points.
    -Keep the explaination concise.

    Topic:
    {topic}
    """,

    "Generate Quiz": """
    Generate 10 multiple-choice questions on the following topic.

    Requirements:
    -4 options for each question.
    -Mention the correct answer.
    -Give a one line explaination

    Topic:
    {topic}
    """,

    "Generate Flashcards": """
    Generate 15 study flashcards.

    Format:

    Question:
    Answer:

    Topic:
    {topic}
    """,

    "Study Planner":
    """
    Create a study timetable.

    Topic:
    {topic}

    Days Available:
    {days}

    Requirements:
    - Day-wise plan
    - Topic to cover each day
    - Revision Schedule
    - Final mock test day
    """
    }