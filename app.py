import json
import urllib.parse
import urllib.request
import streamlit as st

st.set_page_config(page_title="Navneet AI", page_icon="🤖", layout="centered")

st.title("🤖 Navneet's Custom AI")
st.write("Welcome! Ask me anything below.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input field
if prompt := st.chat_input("Type your question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        try:
            url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(prompt)}&format=json"
            req = urllib.request.Request(
                url, headers={"User-Agent": "Mozilla/5.0"}
            )

            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode("utf-8"))
                answer = data.get("AbstractText", "")

            if not answer:
                answer = "I received your question! Try asking about general facts, places, or science topics."

            message_placeholder.markdown(answer)
            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

        except Exception:
            message_placeholder.markdown(
                "An error occurred while fetching the answer. Please try again."
            )
          
