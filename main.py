import streamlit as st

from agent import ask_ai
from memory import get_all_history
from visualize import plot_scores


st.set_page_config(page_title="SelfEvolve AI", layout="wide")


st.sidebar.title("⚙️ Menu")

page = st.sidebar.radio(
    "Go to",
    ["Chat", "Learning History"]
)


# ---------------- CHAT PAGE ----------------

if page == "Chat":

    st.title("🤖 SelfEvolve AI")
    st.write("A Self-Improving AI Assistant")

    user_input = st.text_area("Ask something:")

    if st.button("Submit"):
        if user_input.strip():

            with st.spinner("Thinking..."):
                answer = ask_ai(user_input)

            st.subheader("AI Answer:")
            st.write(answer)


# ---------------- HISTORY PAGE ----------------
chart = plot_scores()

if chart:
    st.pyplot(chart)

elif page == "Learning History":

    st.title("📚 Learning History")

    history = get_all_history()

    if len(history) == 0:
        st.info("No learning data yet. Ask some questions first!")
    else:

        for i, (q, a, fb, score) in enumerate(history, 1):

            with st.expander(f"#{i} — {q[:60]}..."):

                st.markdown("### ❓ Question")
                st.write(q)

                st.markdown("### 🤖 Answer")
                st.write(a)

                st.markdown("### 💡 Feedback")
                st.write(fb)

                st.markdown("### ⭐ Score")
                st.write(score)
