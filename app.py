# streamlit code 

#import libraries 
import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

import streamlit as st
from dotenv import load_dotenv
from crew import legat_assistant_crew

load_dotenv()

st.title("AI legal Assistant")
st.markdown(
    "Enter a legal problem. The AI Legal Assistant will help you with this: "
)
with st.form("form"):
    user_input=st.text_area("Enter your issue :")
    submit = st.form_submit_button() 

if submit:
    if not user_input.strip():
        st.warning("Please enter a legal issue to analyze.")
    else:
        with st.spinner("Analyzing your case and preparing legal document...."):
            result = legat_assistant_crew.kickoff(inputs={"user_input":user_input})
        st.success("Legal Assistant completed the workflow")
        st.subheader("📄 Final Output")
        st.markdown(result if isinstance(result, str) else str(result))



