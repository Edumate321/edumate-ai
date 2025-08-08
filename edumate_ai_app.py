import openai
import streamlit as st
import random

# --- CONFIGURE OPENAI ---
openai.api_key = st.secrets["OPENAI_API_KEY"]
# --- BIBLE VERSES ---
bible_verses = [
    "Proverbs 1:5 – Let the wise listen and add to their learning.",
    "Philippians 4:13 – I can do all things through Christ who strengthens me.",
    "Proverbs 22:6 – Train up a child in the way he should go...",
    "James 1:5 – If any of you lacks wisdom, ask God..."
]

# --- FUNCTIONS ---
def ask_chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

def generate_quiz():
    prompt = "Generate 5 multiple-choice questions on English grammar for secondary school students. Include the correct answers."
    return ask_chatgpt(prompt)

def explain_grammar(topic):
    prompt = f"Explain the grammar topic '{topic}' for a student in simple terms with examples."
    return ask_chatgpt(prompt)

def improve_essay(essay_text):
    prompt = f"Improve the following essay and give suggestions:\n\n{essay_text}"
    return ask_chatgpt(prompt)

# --- STREAMLIT UI ---
st.title("📘 EduMate AI – Smart Study Buddy")
# --- OPENAI FUNCTION ---
menu = st.sidebar.selectbox("Choose a Feature", [
    "Ask a Question",
    "Grammar Help",
    "Take a Quiz",
    "Essay Helper",
    "Daily Study Plan",
    "Fun Stuff (Word/Riddle of the Day)"
])

if menu == "Ask a Question":
    user_input = st.text_input("What's your question?")
    if st.button("Get Answer") and user_input:
        response = ask_chatgpt(/mount/src/edumate-ai/edumate_ai_app.py)
        st.success(response)

elif menu == "Grammar Help":
    topic = st.text_input("Enter a grammar topic (e.g., Adjective Clause)")
    if st.button("Explain") and topic:
        explanation = explain_grammar(topic)
        st.info(explanation)

elif menu == "Take a Quiz":
    if st.button("Generate Quiz"):
        quiz = generate_quiz()
        st.write(quiz)

elif menu == "Essay Helper":
    essay = st.text_area("Paste your essay here")
    if st.button("Improve Essay") and essay:
        improved = improve_essay(essay)
        st.write(improved)

elif menu == "Daily Study Plan":
    st.markdown("**Here’s a sample 7-day plan:**")
    st.markdown("""
    - **Day 1**: Nouns & Verbs
    - **Day 2**: Tenses
    - **Day 3**: Sentence Types
    - **Day 4**: Adjective & Adverb Clauses
    - **Day 5**: Comprehension Practice
    - **Day 6**: Writing an Essay
    - **Day 7**: Quiz & Review
    """)

elif menu == "Fun Stuff (Word/Riddle of the Day)":
    fun_prompt = "Give me a word of the day with meaning and a riddle."
    fun_content = ask_chatgpt(fun_prompt)
    st.write(fun_content)

st.markdown("---")
st.caption("Built with ❤️ for learners everywhere.")
