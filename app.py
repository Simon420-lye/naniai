import streamlit as st
from tabs import cry_analyzer
import tabs.home as home
import tabs.ask_ai as ask_ai
import tabs.milestone_tracker as milestone_tracker

import tabs.about as about
import tabs.milestone_tracker as milestone
import tabs.bedtime as bedtime
from tabs import brain_boost

st.set_page_config(page_title="NANIAI", layout="wide")

TABS = st.tabs([
    "🏠 Home",
    "🧠 Ask AI",
    "📆 Milestone Tracker",
    "🛌 Bedtime Stories & Music",
    "🔊 Baby Cry Analyzer",
    "🧠Parenting Brain Booster",
    "ℹ️ About"
])



with TABS[0]: home.run()
with TABS[1]: ask_ai.run()
with TABS[2]: milestone.show_milestone_tracker()
with TABS[3]: bedtime.run()
with TABS[4]: cry_analyzer.run()
with TABS[5]: brain_boost.run()
with TABS[6]: about.run()

