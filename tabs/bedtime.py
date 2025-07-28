import streamlit as st
import requests
import json
import asyncio
import edge_tts
import os
import webbrowser

# --- Function to query Gemma via Ollama ---
def query_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    
    system_prompt = (
        "You are NANIAI, an expert in storytelling for babies. "
        "Generate a calming, short bedtime story suitable for a baby or toddler. "
        "Use simple, peaceful language and keep it under 150 words."
    )
    
    full_prompt = f"{system_prompt}\n\nUser: {prompt}\nNANIAI:"
    
    data = {
        "model": "gemma",
        "prompt": full_prompt,
        "stream": True
    }

    try:
        response = requests.post(url, headers=headers, json=data, stream=False, timeout=120)
        story = ""
        for line in response.iter_lines():
            if line:
                part = json.loads(line.decode("utf-8"))
                story += part.get("response", "")
        return story.strip()
    except Exception as e:
        return f"🤖 Connection Error: {str(e)}"

# --- Narration Function using Edge TTS ---
async def narrate_story(story_text):
    tts = edge_tts.Communicate(text=story_text, voice="en-US-AriaNeural")
    await tts.save("story.mp3")

def play_story_audio():
    os.system("start story.mp3")  # For Windows. Use 'afplay' on Mac or 'xdg-open' on Linux.

# --- Streamlit UI ---
def run():
    st.subheader("🌙 Bedtime Stories & Baby Sleep Music")
    st.markdown("Let NANIAI read a gentle bedtime story for your little one.")

    if st.button("🧠 Generate Bedtime Story"):
        with st.spinner("Generating a calming story..."):
            story = query_ollama("Tell a short baby bedtime story.")
            st.success("Here's your bedtime story:")
            st.markdown(f"### 🍼 Story Time\n{story}")

            # Narrate
            with st.spinner("🎤 Narrating softly..."):
                asyncio.run(narrate_story(story))
                play_story_audio()

    st.markdown("---")
    st.markdown("🎵 **Need calming music too?** Click below:")

    if st.button("🎶 Play Baby Sleep Music"):
        webbrowser.open("https://www.youtube.com/watch?v=2x2CDVKD9RA")

    # Optional: show a cute calming image
    #st.image("https://cdn.pixabay.com/photo/2018/03/23/13/38/baby-3254165_1280.jpg", use_column_width=True)
    #st.image("httpsS://www.freepik.com/free-ai-image/view-3d-person-sleeping-clouds_133554583.htm#fromView=search&page=1&position=0&uuid=03cf16b7-dc49-4dce-a7e9-e44cc3e71bda&query=baby+ai", use_container_width=True)


