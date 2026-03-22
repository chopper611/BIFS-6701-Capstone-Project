import streamlit as st

# Import the function that runs your LLM
from src.app.run_llm import run_llm

# Title shown at the top of the app
st.title("BIFS 614 LLM")

# Input box for user question
question = st.text_input("Enter your question:")

# Dropdown for selecting mode
mode = st.selectbox("Select mode:", ["study", "assessment"])

# Button to trigger the model
if st.button("Submit"):

    # Prevent empty input
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Run the LLM pipeline
        result = run_llm(question, mode=mode)

        # Display the answer
        st.subheader("Answer")
        st.write(result["answer"])

        # Display sources if available
        if result["chunks"]:
            st.subheader("Sources")
            for i, chunk in enumerate(result["chunks"], 1):
                source = chunk.get("source", "Unknown") if isinstance(chunk, dict) else getattr(chunk, "source", "Unknown")
                st.write(f"{i}. {source}")