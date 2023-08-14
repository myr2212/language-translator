

import streamlit as st
from langchain.llms import OpenAI

openai_api_key = "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"

st.title("Multi-Language Translation Tool (Using OpenAI API)")

input_text = st.text_area("Enter Text to Translate:", "")

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

if input_text:
    st.subheader("Select Target Languages:")
    target_languages = st.multiselect("", ["franch", "spanish", "chiness", "russian", "arabic"])
    
    if st.button("Translate"):
        st.write("Translations:")
        for target_lang in target_languages:
            prompt = f"Translate the following text to '{target_lang}': '{input_text}'"
            response = generate_response(prompt);
            st.write(f"{target_lang.upper()}: {response}")

