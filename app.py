import streamlit as st
from agent import research_topic

st.title("AI Research Assistant Agent")

query = st.text_input("Enter a research topic")

if st.button("Start Research"):

    with st.spinner("Researching the web..."):

        summary, links = research_topic(query)

        st.subheader("Research Summary")
        st.write(summary)

        st.subheader("Sources")

        for link in links:
            st.write(link)