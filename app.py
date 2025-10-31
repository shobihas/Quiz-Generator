import streamlit as st
import chains

def quiz_generator_app():
    """
    Generates Quiz Generator App with Streamlit, providing user input and displaying output.
    """
    st.title("Lets generate a quiz ! 👋")

    with st.form("quiz_generator"):
        topic = st.text_input("Enter a topic for the quiz:")
        num_questions = st.number_input("Enter the number of questions:", min_value=1, value=5)
        submitted = st.form_submit_button("Submit")

        if submitted:
            response = chains.generate_quiz_chain(topic, num_questions)
            st.info(response)

quiz_generator_app()
