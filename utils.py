import openai
import streamlit as st

# Get API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to send messages to OpenAI and receive response


def generate_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message["content"]
