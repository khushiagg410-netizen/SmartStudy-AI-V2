from flask import Flask, render_template, request
import os
import json

from pdf_reader import extract_text
from gemini_helper import (
    generate_summary,
    generate_mcqs,
    chat_with_notes,
    generate_revision_notes
)

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

saved_text = ""
quiz_answers = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    global saved_text

    pdf = request.files["pdf_file"]

    pdf_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        pdf.filename
    )

    pdf.save(pdf_path)

    saved_text = extract_text(pdf_path)

    print("\n========== UPLOAD ==========")
    print("FILE:", pdf.filename)
    print("TEXT LENGTH:", len(saved_text))
    print(saved_text[:500])
    print("============================\n")

    return render_template(
        "index.html",
        upload_success=True
    )


@app.route("/summary")
def summary():

    global saved_text

    summary = generate_summary(saved_text)

    return render_template(
        "index.html",
        summary=summary
    )


@app.route("/quiz")
def quiz():

    global saved_text
    global quiz_answers

    mcqs = generate_mcqs(saved_text)

    mcqs = mcqs.replace("```json", "")
    mcqs = mcqs.replace("```", "")
    mcqs = mcqs.strip()

    mcqs = json.loads(mcqs)

    quiz_answers = []

    for q in mcqs:
        quiz_answers.append(q["answer"])

    return render_template(
        "index.html",
        mcqs=mcqs
    )


@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():

    global quiz_answers

    score = 0

    for i in range(len(quiz_answers)):

        user_answer = request.form.get(f"q{i}")

        if user_answer:

            if quiz_answers[i] in user_answer:
                score += 1

    return render_template(
        "index.html",
        score=score,
        total=len(quiz_answers)
    )


@app.route("/chat", methods=["GET", "POST"])
def chat():

    global saved_text

    answer = ""

    if request.method == "POST":

        question = request.form["question"]

        print("QUESTION:", question)
        print("NOTES LENGTH:", len(saved_text))

        answer = chat_with_notes(
            saved_text,
            question
        )

    return render_template(
        "chat.html",
        answer=answer
    )


@app.route("/revision")
def revision():

    global saved_text

    revision_notes = generate_revision_notes(
        saved_text
    )

    return render_template(
        "index.html",
        revision_notes=revision_notes
    )


if __name__ == "__main__":
    app.run(debug=True)