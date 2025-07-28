import streamlit as st
import requests
import json
from datetime import date, timedelta

# --- AI Query using Gemma (localhost via Ollama) ---
def query_gemma(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "gemma",
        "prompt": prompt,
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

# --- Milestone Logic ---
def calculate_pregnancy_milestone(lmp_date):
    today = date.today()
    days_pregnant = (today - lmp_date).days
    weeks = days_pregnant // 7
    days = days_pregnant % 7
    due_date = lmp_date + timedelta(days=280)

    return weeks, days, due_date

def calculate_baby_milestone(dob):
    today = date.today()
    baby_days = (today - dob).days
    baby_weeks = baby_days // 7
    baby_months = baby_days // 30
    return baby_weeks, baby_months

# --- Main Tracker UI ---
def show_milestone_tracker():
    st.subheader("📅 Pregnancy & Baby Milestone Tracker")

    st.markdown("Select what you want to track:")
    mode = st.radio("Tracker Mode", ["Pregnancy", "Baby"], horizontal=True)

    if mode == "Pregnancy":
        lmp_date = st.date_input("Enter your Last Menstrual Period (LMP):", max_value=date.today())
        if lmp_date:
            weeks, days, due_date = calculate_pregnancy_milestone(lmp_date)

            st.info(f"You're **{weeks} weeks and {days} days pregnant**.")
            st.success(f"Estimated Due Date: **{due_date.strftime('%B %d, %Y')}**")

            if weeks in [12, 20, 28, 36]:
                st.warning(f"📋 Reminder: Important health checkup around week {weeks}!")

            # AI Advice Section
            if st.button("🧠 Get Weekly AI Guidance"):
                with st.spinner("Talking to your AI guide..."):
                    prompt = f"You are a supportive pregnancy coach. Give helpful guidance, reminders, and health tips for someone who is {weeks} weeks pregnant."
                    response = query_gemma(prompt)
                    st.markdown("### 🤰 AI Weekly Guide:")
                    st.success(response)

    else:
        dob = st.date_input("Enter your Baby’s Date of Birth:", max_value=date.today())
        if dob:
            weeks, months = calculate_baby_milestone(dob)

            st.info(f"Your baby is **{weeks} weeks old** (~{months} months).")

            if months in [2, 4, 6]:
                st.warning("📋 Time for baby’s vaccinations and growth check!")

            # AI Advice Section
            if st.button("🧠 Get Baby Growth Guidance"):
                with st.spinner("Getting insights..."):
                    prompt = f"You are a baby care expert. Give guidance, milestone expectations, and parenting support for a {months}-month-old baby."
                    response = query_gemma(prompt)
                    st.markdown("### 👶 Baby Growth AI Tips:")
                    st.success(response)
