import streamlit as st
from prompt_engine import generate_response

st.set_page_config(page_title="AI Assistant", page_icon="🤖")
st.title("🎯 Personalized Prompt-Tuned AI Assistant")

st.markdown("Interact with an intelligent assistant powered by GPT-4.")

task_type = st.selectbox("Choose Task Type", ["Summarize", "Analytics Insight", "Persona-Based"])
user_input = st.text_area("Enter your input")

if st.button("Generate Response"):
    if user_input.strip() != "":
        with st.spinner("Generating response..."):
            output = generate_response(task_type, user_input)
            st.success("Response generated!")
            st.markdown("### 🧠 Assistant's Reply:")
            st.write(output)
    else:
        st.warning("Please enter some input.")
