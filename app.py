# Cell 1: Setup
import streamlit as st
import groq
import os

# Get your Groq API key from environment variables
api_key = os.getenv("GROQ_API_KEY")  # Ensure this is set in your environment variables

# Cell 2: Title & Description
st.title('🤖 AI Data Interview Assistant')
st.markdown('I was made to answer data interview questions. This app demonstrates how to use Groq API to answer data-related interview questions in a deployed environment. Remember, always verify AI-generated responses.')

# Cell 3: Function to analyze text using Groq API
def analyze_text(text):
    """
    This function sends a text prompt to the Groq API.
    
    Args:
        text (str): The tech interview question to be answered.
    
    Returns:
        str: The response generated by the Groq API.
    """
    if not api_key:
        st.error("Groq API key is not set. Please set it in your environment variables.")
        return

    client = groq.Client(api_key=api_key)
    model = "mixtral-8x7b-32768"  # Adjust based on available models
    
    messages = [
        {"role": "system", "content": "You are an assistant who answers interview and technical questions for data science-related jobs."},
        {"role": "user", "content": f"Answer the following job interview question:\n{text}"}
    ]
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0  # Lower temperature for less random responses
    )
    
    return response.choices[0].message.content

# Cell 4: Streamlit UI
user_input = st.text_area("Enter question to answer:", "How should you maintain a deployed model?")

if st.button('Answer Interview Question'):
    with st.spinner('Answering...'):
        result = analyze_text(user_input)
        st.write(result)
