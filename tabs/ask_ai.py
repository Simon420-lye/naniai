# --- tabs/ask_ai.py ---
import streamlit as st
import requests, json


def query_ollama(question):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    prompt = f"""
    You are NANIAI, a helpful medical assistant for pregnant women and baby care.
    Respond compassionately and informatively to the user's question.

    User: {question}
    NANIAI:
    """
    data = {"model": "gemma", "prompt": prompt, "stream": True}
    try:
        r = requests.post(url, headers=headers, json=data, stream=False, timeout=120)
        output = ""
        for line in r.iter_lines():
            if line:
                part = json.loads(line.decode("utf-8"))
                output += part.get("response", "")
        return output
    except Exception as e:
        return f"Error: {e}"
    

# from ai_utils import query_naniai

# def run():
#     st.subheader("🤖 Ask NANI AI")
#     prompt = st.text_area("Ask anything about pregnancy, baby care, etc.")
#     if st.button("Get Answer"):
#         with st.spinner("NANI is thinking..."):
#             response = query_naniai(prompt)
#             st.success(response)



def run():
    st.subheader("🧠 Ask NANIAI")

    # --- Handle suggested click before input is rendered ---
    if "suggested_clicked" in st.session_state:
        st.session_state["question"] = st.session_state["suggested_clicked"]
        del st.session_state["suggested_clicked"]
        st.rerun()

    # --- Input box ---
    question_input = st.text_input("What's on your mind?", key="question")

    if st.button("Ask"):
        with st.spinner("Thinking..."):
            answer = query_ollama(st.session_state.question)
            st.success(answer)

    st.markdown("### 💡 Suggested Questions:")
    suggested = [
        "What should I eat during the first trimester?",
        "How do I soothe my baby when crying at night?",
        "Is it normal to feel anxious during pregnancy?",
        "When should I schedule my baby’s vaccinations?",
        "What exercises are safe while pregnant?",
    ]

    for idx, q in enumerate(suggested):
        if st.button(f"💬 {q}", key=f"suggested_{idx}"):
            st.session_state["suggested_clicked"] = q
            st.rerun()

if "suggested_clicked" in st.session_state:
    st.session_state["question"] = st.session_state["suggested_clicked"]
    del st.session_state["suggested_clicked"]
    st.rerun()  # <-- fixed here
