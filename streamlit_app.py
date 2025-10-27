import streamlit as st

st.set_page_config(page_title="Question 1", page_icon="🧠")
st.title("🧩 Interactive Quiz — Question 1")

# --- EDIT THESE LINES FOR EACH REPO ---
question = "What is 5 + 3?"
choices = ["6", "7", "8", "9"]
correct_answer = "8"
success_message = "✅ Correct! Great job!"
try_again_message = "❌ Try again!"
# --------------------------------------

# Keep state so users can try until correct
if "answered_correctly" not in st.session_state:
    st.session_state.answered_correctly = False

st.subheader(question)
user_choice = st.radio("Choose your answer:", choices, index=None)

if st.button("Submit"):
    if user_choice == correct_answer:
        st.session_state.answered_correctly = True
        st.success(success_message)
    else:
        st.warning(try_again_message)

if st.session_state.answered_correctly:
    st.balloons()
    st.info("You solved this question! You can close this tab or scan the next QR.")
