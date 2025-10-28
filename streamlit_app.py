import streamlit as st

st.set_page_config(page_title="QR Code Quiz 2", page_icon="🧠")
st.title("🧩 Interactive College Corps Quiz!")
st.markdown("<h3 style='color:#4CAF50;'>Let's see if you can solve this!</h3>", unsafe_allow_html=True)

question = "Who is the entity that oversees all College Corps Program?"
choices = ["AmeriCorps", "California Volunteers", "Your University", "The Government"]
correct_answer = "California Volunteers"
success_message = "✅ Correct! Great job!"
try_again_message = "❌ Try again!"

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
