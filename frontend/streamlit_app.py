import streamlit as st
import requests

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="📚",
)

st.title("Enterprise GenAI Knowledge Assistant")
st.caption("Ask questions about your indexed PDF documents.")

question = st.text_area("Enter your question")

if st.button("Ask AI"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"question": question},
                timeout=120,
            )
            response.raise_for_status()
            result = response.json()

            st.subheader("Answer")
            st.write(result["answer"])

            st.subheader("Retrieved sources")
            for source in result["sources"]:
                st.write(
                    f"**{source['source']}** — "
                    f"Page {source['page']}"
                )
                st.caption(source["snippet"])

        except requests.RequestException:
            st.error(
                "Could not reach the API. "
                "Check that FastAPI is running."
            )