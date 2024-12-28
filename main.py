import streamlit as st
import time

from gemini import gen_text

st.set_page_config(page_title="⭐StreamGemini", layout="wide")

st.header("⭐StreamGemini")
st.markdown("Hey! This is a simple implementation of ChatGPT like Chatbot using Streamlit and Using Gemini model as LLM. \
         The UI is implemented using Streamlit and in the Backend it uses the responses generated from Gemini Model. To see the source code please refer to my [GitHub](https://github.com/nimadindar/-StreamGemini)")

st.markdown("---")
st.markdown(
    """
    <style>
    .centered {
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
    }
    </style>
    <div class="centered">What can I help with?</div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

col1, col2, col3 = st.columns([1, 2, 1])  
with col2:
    user_message = st.text_input("", key="message", placeholder="Message StreamGemini")
    
    if user_message.strip():  

        st.session_state.chat_history.append(("User", user_message))

        bot_response = gen_text(user_message)

        st.session_state.chat_history.append(("Bot", bot_response))
        st.session_state.chat_history[-1] = ("Bot", bot_response)

st.write("### Conversation:")
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
    st.markdown("---")