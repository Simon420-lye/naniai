import streamlit as st
import requests
import json

def query_gemma(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    full_prompt = f"You are NANIAI, a helpful, calming AI designed for pregnant women and new moms. Generate a short, encouraging daily affirmation and one mindful wellness tip to help reduce stress.\n\nUser: {prompt}\nNANIAI:"

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
    st.subheader("💗 NANI AI: Your Companion for Life")

    st.markdown("""
    - 🧐 Baby & Pregnancy advice, 🥛 Nutrition tips  
    - 📅 Week-by-week milestones  
    - 🛌 Bedtime Stories & Sleep Music  
    """)

    st.divider()

    # --- Affirmation Section ---
    st.subheader("🧘‍♀️ NANI's Mindful Moments")
    if st.button("✨ Get Today’s AI Affirmation"):
        with st.spinner("Generating calming message..."):
            output = query_gemma("Give today’s daily affirmation and wellness tip.")
            st.success("Here’s your message 💖")
            st.write(output)

    st.divider()

    # --- Game-style Pregnancy Guide ---
    st.subheader("🎮 Fun & Learning Explorer")

    # Track button click using session state
    if "show_week_guide" not in st.session_state:
        st.session_state.show_week_guide = False

    # Week selection first
    week = st.slider("📅 Pick your week of pregnancy:", min_value=1, max_value=40, value=1, step=1)

    # Guide generation trigger
    if st.button("🍎 Show What to Eat, Avoid, Do & Don't"):
        st.session_state.show_week_guide = True

    # Optional Reset
    if st.session_state.show_week_guide:
        if st.button("🔄 Reset Guide"):
            st.session_state.show_week_guide = False

    # Show guide after click
    if st.session_state.show_week_guide:
        st.markdown("### 🤖 NANI AI is preparing your guide...")

        prompt = f"""
        I am {week} weeks pregnant. What should I eat and avoid? Also, what should I do and avoid doing at this stage? 
        Give simple, encouraging advice in 4 sections:
        1. ✅ Eat
        2. ❌ Avoid
        3. ✅ Do
        4. ❌ Don’t

        Keep it short and helpful. Add emojis to make it friendly.
        """

        with st.spinner("🧠 Thinking..."):
            result = query_gemma(prompt)
            st.success(f"🤰 Week {week} - Your Guide")
            st.markdown(result)
