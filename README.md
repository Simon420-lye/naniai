NANI AI: An AI-Powered Companion for Pregnant Women & New Moms 🤰✨

Overview

NANI AI is a private, offline-first AI app designed to support pregnant women and new moms with timely, accurate, and compassionate guidance. Powered by Gemma 3n, running locally via Ollama, NANI AI provides week-by-week milestones, health tips, interactive baby care features, and mindful wellness affirmations — all in a privacy-first environment that doesn't rely on constant internet connectivity.

🚀 Built for: Google Gemma 3n Impact Challenge Hackathon
Track: Ollama Special Prize + Overall Impact Track

Live Demo Video: https://youtu.be/t4KXFZkFy20?si=YLPdvmYD51oNhgYS

GitHub Repository: [Your Repo Link Here]

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
  
