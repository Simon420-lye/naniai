import streamlit as st
import torch, librosa, tempfile, sounddevice as sd, soundfile as sf
import numpy as np
from transformers import AutoProcessor, AutoModelForAudioClassification
import os
#from dotenv import load_dotenv


# HF_TOKEN = os.getenv("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")

# @st.cache_resource
# def load_model_and_processor():
#     processor = AutoProcessor.from_pretrained(
#         "Marcos12886/distilhubert-finetuned-cry-detector",
#         token=HF_TOKEN
#     )
#     model = AutoModelForAudioClassification.from_pretrained(
#         "Marcos12886/distilhubert-finetuned-cry-detector",
#         token=HF_TOKEN
#     )
#     return processor, model


@st.cache_resource
def load_model_and_processor():
    processor = AutoProcessor.from_pretrained("Marcos12886/distilhubert-finetuned-cry-detector")
    model = AutoModelForAudioClassification.from_pretrained("Marcos12886/distilhubert-finetuned-cry-detector")
    return processor, model

def analyze_cry(audio_path):
    y, sr = librosa.load(audio_path, sr=16000)
    processor, model = load_model_and_processor()
    inputs = processor(audio=y, sampling_rate=sr, return_tensors="pt", padding=True)
    model.eval()
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)[0].cpu().numpy()
    id2label = processor.model.config.id2label
    idx = np.argmax(probs)
    return id2label[str(idx)], float(probs[idx])

def record_audio(filename="recorded.wav", duration=5, samplerate=16000):
    st.info("Recording for {} seconds...".format(duration))
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(filename, audio, samplerate)
    return filename

def run():
    st.subheader("🎤 Baby Cry Analyzer (Real-time Detection)")

    # if st.button("🎧 Start Real-Time Cry Monitoring"):
    #     placeholder = st.empty()
    #     for i in range(10):  # check 10 times (5s * 10 = 50 seconds)
    #         with st.spinner(f"Listening... ({i+1}/10)"):
    #             audio_file = record_audio()
    #             label, confidence = analyze_cry(audio_file)
    #             placeholder.success(f"Detected Cry Type: **{label}** ({confidence*100:.1f}% confidence)")
    #             if confidence > 0.75:
    #                 st.balloons()
    #             if label.lower() != "no cry":
    #                 st.warning(f"🔔 Attention: Baby is likely **{label}**")
    #             st.divider()

    # st.markdown("### 📤 Or Upload a Recording")
    uploaded = st.file_uploader("Upload audio (.wav or .mp3)", type=["wav", "mp3"])
    if uploaded:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(uploaded.read())
            label, confidence = analyze_cry(f.name)
            st.success(f"🧠 Cry Type: **{label}** ({confidence*100:.1f}% confidence)")

    st.markdown("### 💡 Tips Based on Cry Type:")
    st.markdown("""
    - **Hungry** 🍽️ → Try feeding your baby.
    - **Tired** 😴 → Soothe with rocking or lullabies.
    - **Pain** 😢 → Check for illness, fever, or tight clothing.
    - **Discomfort** 🧸 → Adjust diaper, room temperature, or position.
    - **Burping** 🫧 → Gently burp your baby over your shoulder.
    """)
