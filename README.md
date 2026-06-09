# 📚 SmartStudy AI

An AI-powered study assistant that transforms lengthy PDF notes into concise summaries, interactive quizzes, revision notes, and intelligent Q&A using Gemini AI.

## 🚀 Features

### 📄 PDF Upload

Upload your study notes in PDF format and let AI process the content.

### ✨ AI Summary

Convert lengthy notes into structured and easy-to-understand summaries.

### 🧠 Quiz Generator

Automatically generate multiple-choice questions from uploaded notes to test your understanding.

### 💬 Chat With Notes

Ask questions directly from your uploaded notes and receive AI-powered answers.

### 🚀 Revision Mode

Generate last-minute revision notes and exam-focused key points.

---

## 🛠️ Tech Stack

* Python
* Flask
* Google Gemini AI
* HTML5
* CSS3
* PyPDF

---

## 📂 Project Structure

```text
project/
│
├── app.py
├── gemini_helper.py
├── pdf_reader.py
│
├── templates/
│   ├── index.html
│   ├── chat.html
│   ├── summary.html
│   ├── quiz.html
│   ├── revision.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
└── uploads/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/khushiagg410-netizen/SmartStudy-AI-V2.git
```

### Move Into Project Folder

```bash
cd SmartStudy-AI-V2
```

### Install Dependencies

```bash
pip install flask pypdf google-generativeai
```

### Add Gemini API Key

Inside `gemini_helper.py`:

```python
genai.configure(api_key="YOUR_API_KEY")
```

### Run Project

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🎯 Future Improvements

* User Authentication
* Flashcards Generator
* Dark Mode
* Notes History
* Multi-PDF Support
* PDF Highlighting
* Voice Assistant

---

## 👩‍💻 Author

**Khushi Aggarwal**

Built with ❤️ using Flask and Gemini AI.

---

## 🌟 Project Goal

SmartStudy AI aims to make studying smarter, faster, and more interactive by leveraging the power of Generative AI for education.
