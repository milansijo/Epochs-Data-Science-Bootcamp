import os
import shutil
import gradio as gr

from rag import create_vector_store, retrieve_context
from utils import generate_answer

# -----------------------------
# Conversation Memory
# -----------------------------

chat_history = []


# -----------------------------
# Upload PDF
# -----------------------------

def upload_pdf(pdf):

    global chat_history

    chat_history = []

    if pdf is None:
        return "Please upload a PDF first."

    create_vector_store(pdf.name)

    return "✅ PDF processed successfully!\n\nYou can now ask questions."


# -----------------------------
# Ask Question
# -----------------------------

def chat(question):

    global chat_history

    if question.strip() == "":
        return "Please enter a question."

    context = retrieve_context(question)

    history_text = ""

    for q, a in chat_history:

        history_text += f"User: {q}\n"

        history_text += f"Assistant: {a}\n\n"

    answer = generate_answer(
        context=context,
        question=question,
        history=history_text
    )

    chat_history.append(
        (question, answer)
    )

    return answer


# -----------------------------
# Clear Chat
# -----------------------------

def clear_chat():
    global chat_history

    chat_history = []

    if os.path.exists("chroma_db"):
        shutil.rmtree("chroma_db", ignore_errors=True)

    return (
        None,                                   
        "",                                     
        "",                                     
        "✅ Conversation cleared successfully!" 
    )

# -----------------------------
# Gradio UI
# -----------------------------

with gr.Blocks(title="StudyBuddy AI") as demo:

    gr.Markdown(
        """
# 📂 PDF Buddy

### PDF Question Answering using RAG + Gemini
"""
    )

    with gr.Row():

        pdf = gr.File(
            file_types=[".pdf"],
            label="Upload PDF"
        )

        upload_button = gr.Button(
            "Process PDF"
        )

    upload_status = gr.Textbox(
        label="Status",
        interactive=False
    )

    gr.Markdown("---")

    question = gr.Textbox(
        label="Ask a Question",
        placeholder="Ask anything from the uploaded PDF..."
    )

    ask_button = gr.Button(
        "Ask"
    )

    answer = gr.Textbox(
        label="Answer",
        lines=12
    )

    clear_button = gr.Button(
        "Clear Conversation"
    )

    upload_button.click(
        upload_pdf,
        inputs=pdf,
        outputs=upload_status
    )

    ask_button.click(
        chat,
        inputs=question,
        outputs=answer
    )

    clear_button.click(
    fn=clear_chat,
    inputs=[],
    outputs=[
        pdf,
        question,
        answer,
        upload_status
    ]
)


demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)