import streamlit as st
from utils import generate_response
from prompts import get_question_prompt

st.title("💬 TalentScout: AI Hiring Assistant")

# Step tracker
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.data = {}

questions = [
    "What is your full name?",
    "What is your email address?",
    "What is your phone number?",
    "How many years of experience do you have?",
    "What position are you applying for?",
    "Where are you currently located?",
    "List the tech stack you’re skilled in (languages, frameworks, tools):"
]

# Display the assistant's message
if st.session_state.step < len(questions):
    st.chat_message("assistant").write(questions[st.session_state.step])
else:
    # When all info collected, show a summary and generate questions
    st.chat_message("assistant").write(
        "Thanks! Here's a summary of what you shared:")
    for key, value in st.session_state.data.items():
        st.write(f"**{key}**: {value}")

    tech_stack = st.session_state.data["Tech Stack"]
    prompt = get_question_prompt(tech_stack)
    response = generate_response([{"role": "user", "content": prompt}])
    st.chat_message("assistant").write(
        "Based on your tech stack, here are some questions you might face in an interview:")
    st.markdown(response)

# Get user input
user_input = st.chat_input("Type your answer here...")

if user_input:
    if st.session_state.step < len(questions):
        key_map = [
            "Full Name", "Email", "Phone", "Experience",
            "Position", "Location", "Tech Stack"
        ]
        st.session_state.data[key_map[st.session_state.step]] = user_input
        st.session_state.step += 1
        st.rerun()
