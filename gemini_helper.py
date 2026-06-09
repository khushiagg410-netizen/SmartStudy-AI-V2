print("Gemini Helper Loaded")
print("Using gemini-2.5-flash")
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

print("Gemini Helper Loaded")
print("Using gemini-2.5-flash")
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_summary(text):

    prompt = f"""
    Summarize these notes.

    Return plain text only.

    Use this format:

    OVERVIEW:
    - point
    - point
   

KEY CONCEPTS:
- point
- point

IMPORTANT POINTS:
- point
- point

QUICK REVISION:
- point
- point

Do NOT use:
#, *, **, markdown symbols.

Notes:
{text}
"""
    

    response = model.generate_content(prompt)

    return response.text
def generate_mcqs(text):
#f -> formatting string
#name = "Khushi"
#print(f"Hello {name}") #prnts Hello Khushi

    prompt = f""" 
    
    Generate 10 MCQs from these notes.

    Format:

    Question:
    A)
    B)
    C)
    D)

    Correct Answer:
    
    Notes:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text



def generate_mcqs(text):
#f -> formatting string
#name = "Khushi"
#print(f"Hello {name}") #prnts Hello Khushi

#JSON easier 
#install json5 to convert String into Python
    prompt = f"""  
    
    Generate 10 MCQs from these notes.
    Return ONLY valid JSON.

    Format:

    [
      {{
        "question": "...",
        "options": ["A","B","C","D"],
        "answer": "A"
      }}
    ]

    Notes:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text
def chat_with_notes(notes, question):

    prompt = f"""
    You are a study assistant.

    Answer ONLY using the notes below.

    Notes:
    {notes}

    Question:
    {question}
    """

    response = model.generate_content(prompt)

    return response.text
def generate_revision_notes(text):

    prompt = f"""
    Create ultra-short revision notes.

    Format:

    EXAM CRASH COURSE

    IMPORTANT CONCEPTS:
    - point
    - point

    MOST IMPORTANT DEFINITIONS:
    - point
    - point

    LAST MINUTE REVISION:
    - point
    - point

    Keep everything short.
    Focus only on exam-relevant content.

    Notes:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text





    