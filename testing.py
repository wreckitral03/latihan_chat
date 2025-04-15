import streamlit as st
import os
from openai import OpenAI

# Load token and endpoint
token = os.environ.get("GITHUB_TOKEN")  # Replace with your actual env var name if different
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

# Initialize client
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Streamlit UI
st.title("Put your question here.")
st.text("Latihan Ricky")
question = st.text_area("Ask anything below:", height=150)
submit = st.button("Submit")

# When the user clicks submit
if submit:
    if not token:
        st.error("API token not found. Make sure GITHUB_TOKEN is set in environment variables.")
    elif not question.strip():
        st.error("Please enter a question.")
    else:
        try:
            with st.spinner("Thinking..."):
                response = client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": question}
                    ]
                )
                answer = response.choices[0].message.content
                st.success(f"Answer:\n\n{answer}")

        except Exception as e:
            st.error(f"Error: {e}")