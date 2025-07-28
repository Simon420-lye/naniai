# --- tabs/brain_boost.py ---
import streamlit as st
import requests
import json
from datetime import date

def query_gemma(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    full_prompt = (
        "You are NANIAI, a calm and compassionate AI parenting mentor. "
        "Each week, provide a 'Parenting Brain Boost' — a tip to improve mental well-being, "
        "strengthen bonding, or handle common parenting stress with wisdom and empathy.\n\n"
        f"User: {prompt}\nNANIAI:"
    )
    data = {
        "model": "gemma",
        "prompt": full_prompt,
        "stream": True
    }

    try:
        response = requests.post(url, headers=headers, json=data, stream=False, timeout=120)
        full_response = ""
        for line in response.iter_lines():
            if line:
                part = json.loads(line.decode("utf-8"))
                full_response += part.get("response", "")
        return full_response.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

def run():
    st.subheader(" Weekly Parenting Brain Boost")

    today = date.today()
    this_week = today.strftime("Week %W, %Y")

    st.markdown(f"#### 📅 {this_week}")

    if "brain_boost_tip" not in st.session_state:
        st.session_state.brain_boost_tip = None

    if st.button("✨ Get My Weekly Brain Boost Tip"):
        with st.spinner("Generating wisdom..."):
            tip = query_gemma("Give this week's parenting brain boost tip.")
            st.session_state.brain_boost_tip = tip

    if st.session_state.brain_boost_tip:
        st.success("Here’s your AI-powered insight 💡")
        st.markdown(f"> {st.session_state.brain_boost_tip}")
