import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

#Load environment variables
load_dotenv()

#Configure streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:", #Favicon emoji
    layout="centered", #page layout option
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#Set up Google Gemini-pro AI Model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-2.0-flash-exp')

#Function to translate roles between Gemini-pro and streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role
    
#Initialize chat session in streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

#Display chatbot's title on the page
st.title("🤖 Gemini-Pro Boty😎")

#display chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)
        
#input field for user 
user_prompt = st.chat_input("Ask Gemini-pro.. ")
if user_prompt:
    #Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    #send user's message to the gemini-pro and get the response 
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    #display gemini - pro response 
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)