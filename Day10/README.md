# 🎓 StudyGenie AI – Your Personal AI Study Assistant

**Name:** Milan Sijo  
**MUID:** milansijo@mulearn

---

## 🌐 Live Demo

🔗 **Live Website:** https://study-buddy-ai-h030.onrender.com/

You can access and use the deployed application directly using the above link without any local setup.

---

## 📖 Project Overview

StudyGenie AI is an AI-powered study assistant built using **Streamlit** and **Google Gemini 3.5 Flash**. It helps students learn more effectively by generating AI-powered explanations, structured notes, quizzes, flashcards, and personalized study plans through an interactive web interface.

---

## ✨ Features

- 📖 Explain any topic with AI
- 📝 Generate structured study notes
- ❓ Create multiple-choice quizzes
- 🧠 Generate flashcards for revision
- 📅 Generate personalized study plans
- ⚡ Fast responses using Google Gemini 3.5 Flash
- 🌐 Deployed and accessible online

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI Model
- Google Gemini 3.5 Flash

### Libraries
- Streamlit
- Google GenAI SDK
- Python Dotenv

---

## 📂 Project Structure 

```text
Day10/
│
├── app.py
├── prompts.py
├── utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Live Application

The deployed application can be accessed here:

**🌍 Website:** https://study-buddy-ai-h030.onrender.com/

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/milansijo/Epochs-Data-Science-Bootcamp.git
```

Navigate to the project:

```bash
cd Epochs-Data-Science-Bootcamp/Day10
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variable

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## 💡 How It Works

1. Launch the application.
2. Select a study feature from the sidebar.
3. Enter the topic or required information.
4. Click the corresponding **Generate** button.
5. The prompt is sent to **Google Gemini 3.5 Flash**.
6. The AI generates the requested educational content.
7. The generated response is displayed instantly.

---

## 📌 Available Features

### 📖 Explain Topic
Explains any topic in Beginner, Intermediate, or Advanced mode.

### 📝 Generate Notes
Creates concise and structured notes for revision.

### ❓ Generate Quiz
Generates multiple-choice questions with answers and explanations.

### 🧠 Generate Flashcards
Creates question-and-answer flashcards for effective memorization.

### 📅 Study Planner
Generates a personalized study schedule based on the selected subject and available study days.

---

## 🧠 Prompt Engineering

Each feature uses a dedicated prompt template to guide the Gemini model in generating accurate, structured, and educational responses tailored to the selected task.

---

## 🎯 Learning Outcomes

This project demonstrates:

- Large Language Model (LLM) Integration
- Prompt Engineering
- Streamlit Web Application Development
- Google Gemini API Integration
- Environment Variable Management
- AI-Powered Educational Assistance
- Cloud Deployment using Render

---

## 🚀 Deployment

**Platform:** Render

**Live Website:** https://study-buddy-ai-h030.onrender.com/

---

## 🔮 Future Improvements

- PDF upload and summarization
- Voice-based interaction
- User authentication
- Study history
- Download generated notes as PDF
- Dark mode
- Multi-language support
- AI-powered learning analytics

---

## 👨‍💻 Author

**Milan Sijo**

**MUID:** milansijo@mulearn

---

## 📄 License

This project was developed as part of the **Epochs Data Science Bootcamp – Day 10 Assignment** for educational purposes.
