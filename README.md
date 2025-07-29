NANI AI: An AI-Powered Companion for Pregnant Women & New Moms 🤰✨

Overview

NANI AI is a private, offline-first AI app designed to support pregnant women and new moms with timely, accurate, and compassionate guidance. Powered by Gemma 3n, running locally via Ollama, NANI AI provides week-by-week milestones, health tips, interactive baby care features, and mindful wellness affirmations — all in a privacy-first environment that doesn't rely on constant internet connectivity.

🚀 Built for: Google Gemma 3n Impact Challenge Hackathon
Track: Ollama Special Prize + Overall Impact Track

Live Demo Video: https://youtu.be/GZomdAtsj_A?si=kA0cwvF_Je9hADyd

GitHub Repository: https://github.com/Simon420-lye/naniai


***Key Features***

Feature	Description
🧘‍♀️ AI-Powered Daily Affirmations	Personalized mental wellness tips and affirmations to reduce stress.
📅 Pregnancy & Baby Milestone Tracker	Week-by-week guides with interactive content on nutrition, do's & don'ts.
🛌 Bedtime Stories & Sleep Music	AI-generated bedtime stories and sleep-friendly music for babies.
🎙️ Baby Cry Analyzer	(Optional) Detects cry types using local audio analysis.
🎮 Interactive Game-Style Education	Fun sliders & explorables for nutrition & health tips per week of pregnancy.
⚡ Offline-First & Private	Runs 100% locally using Gemma 3n via Ollama, ensuring data privacy.

***Technology Stack***

Stack Component	Details
AI Model	Google Gemma 3n via Ollama
Frontend	Streamlit
Local Inference	Ollama API (localhost:11434)
Frameworks: Python, Transformers, Streamlit
Multimodality	Text, Audio (Optional cry analysis)

Installation & Running Locally
1. Prerequisites
   
* Python 3.10+

* Ollama Installed Locally

* Gemma Model pulled into Ollama:

ollama pull gemma:3n

(Optional) For Baby Cry Detection:
pip install torch librosa transformers

2. Clone the Repository

git clone https://github.com/Simon420-lye/naniai.git
cd naniai-gemma3n

3. Install Dependencies

pip install -r requirements.txt

4. Run Ollama Locally
   
Make sure Ollama is running in the background:
ollama serve

5. Run the NANI AI App

streamlit run app.py


***Project Architecture***

naniai-gemma3n/
├── app.py                   # Main entry file for Streamlit App
├── tabs/                    # Modular tabs for each feature
│   ├── home.py
│   ├── milestone_tracker.py
│   ├── bedtime_stories.py
│   ├── cry_analyzer.py
│   ├── weekly_tips.py
│   └── settings.py
├── assets/                  # Images, Audio files, Story Templates
├── README.md                 # (This file)
├── requirements.txt          # Python dependencies
└── LICENSE



***How NANI AI Uses Gemma 3n (Technical Deep Dive)***

1. Gemma 3n via Ollama Local API:

* All AI responses are generated using Ollama’s Local API (localhost:11434), ensuring offline availability and private processing.

* API Calls in home.py, milestone_tracker.py, weekly_tips.py etc., dynamically query Gemma 3n using custom prompts.

2. Optimized Prompting Strategy:

* Contextual prompts tailored per feature.
* Example: In Weekly Tips → “I am X weeks pregnant, give me simple do’s and don’ts with emojis.”

3. Frontend & User Interface:

* Lightweight Streamlit app, modularized into tabs for maintainability.

* UI optimized for a friendly, playful user experience for new moms.


***Challenges Overcome***

1. Optimizing response time by choosing Ollama Local Deployment instead of cloud APIs.

2. Balancing local inference performance with user experience interactivity.

3. Creating a game-style UI flow using simple sliders and Streamlit widgets for education.

***Future Improvements***

1. Integrate on-device voice-driven interactions.

2. Expand to image-based guides for new moms.

3. Add multilingual support for rural communities.

4. Develop a mobile-first Progressive Web App (PWA).

***Team & Credits***

1. Developer: Shayamon Bastakoti 

2. Mentorship & Guidance: Google Gemma Community, OpenAI ChatGPT.

3. Special thanks: Kaggle, Ollama Community.
  
