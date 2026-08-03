import streamlit as st
from prompts import PROMPTS
from utils import generate_response

st.set_page_config(
    page_title="StudyBuddy AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 StudyBuddy AI")
st.markdown("### Your Personal AI Study Assistant")

st.sidebar.title("📚 Features")

feature = st.sidebar.selectbox(
    "Choose a Feature",
    (
        "Explain Topic",
        "Generate Notes",
        "Generate Quiz",
        "Generate Flashcards",
        "Study Planner"
    )
)

# --------------------------
# Explain Topic
# --------------------------

if feature == "Explain Topic":

    topic = st.text_input("Enter Topic")

    difficulty = st.selectbox(
        "Difficulty Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    if st.button("Explain"):

        if topic.strip() == "":
            st.warning("Please enter a topic.")
        else:

            prompt = PROMPTS["Explain Topic"].format(
                topic=topic,
                difficulty=difficulty
            )

            with st.spinner("Generating explanation..."):
                response = generate_response(prompt)

            st.success("Done!")
            st.markdown(response)

# --------------------------
# Generate Notes
# --------------------------

elif feature == "Generate Notes":

    topic = st.text_input("Enter Topic")

    level = st.selectbox(
        "Academic Level",
        [
            "School",
            "Undergraduate",
            "Postgraduate"
        ]
    )

    if st.button("Generate Notes"):

        if topic.strip() == "":
            st.warning("Please enter a topic.")
        else:

            prompt = PROMPTS["Generate Notes"].format(
                topic=topic,
                level=level
            )

            with st.spinner("Generating notes..."):
                response = generate_response(prompt)

            st.success("Done!")
            st.markdown(response)

# --------------------------
# Quiz Generator
# --------------------------

elif feature == "Generate Quiz":

    topic = st.text_input("Enter Topic")

    num_questions = st.slider(
        "Number of Questions",
        5,
        20,
        10
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    if st.button("Generate Quiz"):

        if topic.strip() == "":
            st.warning("Please enter a topic.")
        else:

            prompt = PROMPTS["Generate Quiz"].format(
                topic=topic,
                num_questions=num_questions,
                difficulty=difficulty
            )

            with st.spinner("Generating quiz..."):
                response = generate_response(prompt)

            st.success("Done!")
            st.markdown(response)

# --------------------------
# Flashcards
# --------------------------

elif feature == "Generate Flashcards":

    topic = st.text_input("Enter Topic")

    num_cards = st.slider(
        "Number of Flashcards",
        5,
        20,
        10
    )

    if st.button("Generate Flashcards"):

        if topic.strip() == "":
            st.warning("Please enter a topic.")
        else:

            prompt = PROMPTS["Generate Flashcards"].format(
                topic=topic,
                num_cards=num_cards
            )

            with st.spinner("Generating flashcards..."):
                response = generate_response(prompt)

            st.success("Done!")
            st.markdown(response)

# --------------------------
# Study Planner
# --------------------------

elif feature == "Study Planner":

    topic = st.text_input("Subject")

    days = st.number_input(
        "Days Available",
        min_value=1,
        max_value=365,
        value=7
    )

    hours = st.slider(
        "Hours per Day",
        1,
        12,
        3
    )

    if st.button("Generate Study Plan"):

        if topic.strip() == "":
            st.warning("Please enter a subject.")
        else:

            prompt = PROMPTS["Study Planner"].format(
                topic=topic,
                days=days,
                hours=hours
            )

            with st.spinner("Creating study plan..."):
                response = generate_response(prompt)

            st.success("Done!")
            st.markdown(response)