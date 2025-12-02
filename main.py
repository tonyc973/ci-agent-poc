import streamlit as st
import os
from PyPDFForm import PdfWrapper
import generator  # Import our generator script

# CONFIG
TEMPLATE_PATH = "assets/application_form.pdf"
OUTPUT_FILE = "Completed_Application.pdf"

# INITIALIZATION 
st.set_page_config(page_title="CI Agent", page_icon="🆔")

#  Check if PDF exists, if not, create it
if not os.path.exists(TEMPLATE_PATH):
    with st.spinner("Generating English Template..."):
        generator.create_english_template()
    st.success("Template Ready!")

# Session State Setup
if "form_data" not in st.session_state:
    st.session_state.form_data = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "step" not in st.session_state:
    st.session_state.step = 0

# THE AGENT'S LOGIC 

flow = [
    ("LastName", "Hello! Let's prepare the ID application. What is the minor's **Last Name**?"),
    ("FirstName", "Great. What is the **First Name**?"),
    ("CNP", "Please enter the **Personal ID (CNP)**?"),
    ("FatherName", "What is the **Father's** First Name?"),
    ("MotherName", "What is the **Mother's** First Name?"),
    ("City", "What **City or Sector** is the address in?"),
    ("Street", "What is the **Street Name**?"),
    ("Number", "What is the **Street Number** (and block/apartment if applicable)?"),
]

#  UI LAYOUT 
st.title("🆔 AI Civil Servant (English)")
st.caption("I will generate the official PDF application for you.")

# Display Chat History
for role, text in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(text)

# Agent Loop
if st.session_state.step < len(flow):
    current_key, current_question = flow[st.session_state.step]

    # If the last message was NOT the assistant, show the question
    if not st.session_state.chat_history or st.session_state.chat_history[-1][0] != "assistant":
        with st.chat_message("assistant"):
            st.markdown(current_question)
        st.session_state.chat_history.append(("assistant", current_question))

    # User Input
    user_input = st.chat_input(f"Answer for {current_key}...")
    
    if user_input:
        # Save input
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.form_data[current_key] = user_input
        
        # Advance
        st.session_state.step += 1
        st.rerun()

else:
    # --- COMPLETION ---
    with st.chat_message("assistant"):
        st.markdown("✅ **I have all the details!** Generating your PDF now...")

    # Fill PDF
    try:
        wrapper = PdfWrapper(TEMPLATE_PATH)
        filled = wrapper.fill(st.session_state.form_data)
        
        with open(OUTPUT_FILE, "wb+") as f:
            f.write(filled.read())

        # Show Result
        st.success("Document Generated Successfully!")
        
        with open(OUTPUT_FILE, "rb") as f:
            st.download_button(
                label="📄 Download Completed PDF",
                data=f,
                file_name="My_Application.pdf",
                mime="application/pdf"
            )
            
        with st.expander("View Data Summary"):
            st.json(st.session_state.form_data)
            
        if st.button("Start Over"):
            st.session_state.clear()
            st.rerun()
            
    except Exception as e:
        st.error(f"Error: {e}")