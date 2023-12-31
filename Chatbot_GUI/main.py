import streamlit as st
from utils import *
from streamlit_chat import message

# Function to reset session state
def on_change():
    # Clear existing session state keys
    keys_to_delete = list(st.session_state.keys())
    for key in keys_to_delete:
        del st.session_state[key]

    # Reinitialize session state variables if needed
    st.session_state['responses'] = ["Welcome to PDF QnA chatbot. How may I assist you?"]
    st.session_state['requests'] = []

# Display file uploader to allow the user to upload a PDF file
uploaded_files = st.file_uploader("Choose a PDF file", type=["pdf"], accept_multiple_files=False, on_change=on_change)

# Check if a file is uploaded
if not uploaded_files:
    st.warning("Please upload a PDF file.")
    st.stop()  # Jump back to the file uploading section

# Get the path of the uploaded PDF file
pdf_path = uploaded_files.name

# Update the session state variable to store the selected PDF file path
st.session_state["selected_pdf_path"] = pdf_path

# Initialize the Chatbot if not already done
if "model_initialized" not in st.session_state:
    bot = ChatbotResponse(path=st.session_state["selected_pdf_path"])
    st.session_state["model_initialized"] = True
    st.session_state["bot"] = bot
else:
    bot = st.session_state["bot"]

st.title("QnA Chatbot")

# Container for chat history
response_container = st.container()

# Container for text box
textcontainer = st.container()

with textcontainer:
    if "model_initialized" in st.session_state:
        query = st.text_input("Enter a question and get an answer:", key="query")
        if query:
            with st.spinner("Please wait ...."):
                response, docs = bot.get_query_response(query)
                st.session_state.requests.append(query)
                st.session_state.responses.append(response)

# Check if the PDF file path is still available in the session state
if "selected_pdf_path" not in st.session_state:
    st.warning("Please upload a PDF file.")

with response_container:
    if st.session_state['responses']:
        for i in range(len(st.session_state['responses'])):
            message(st.session_state['responses'][i], key=str(i))
            if i < len(st.session_state['requests']):
                message(st.session_state["requests"][i], is_user=True, key=str(i)+'_user')