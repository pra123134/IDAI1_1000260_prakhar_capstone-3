import streamlit as st
import google.generativeai as genai

# ✅ Configure API Key securely
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
else:
    st.error("⚠️ API Key is missing. Go to Streamlit Cloud → Settings → Secrets and add your API key.")
    st.stop()

# ✅ AI Response Generator
def get_ai_response(prompt, fallback_message="⚠️ AI response unavailable. Please try again later."):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text.strip() if hasattr(response, "text") and response.text.strip() else fallback_message
    except Exception as e:
        return f"⚠️ AI Error: {str(e)}\n{fallback_message}"

# ✅ Streamlit UI Configuration
st.set_page_config(page_title="Gamified Smart Restaurant Management", layout="wide")

st.title("🏆 Gamified Smart Restaurant Management with Gemini 1.5 Pro")
st.write("🚀 AI-driven gamification for managers, staff, customers, and system performance optimization.")

# 🎯 **Manager Gamification**
st.header("📊 Manager Challenges")
manager_task = st.selectbox("Select a Manager Challenge:", [
    "Gamified Decision-Making",
    "AI-Generated Scenario Simulations",
    "AI-Driven Sustainability Challenges",
    "Dynamic AI Adjustments for Peak Hours"
])
if st.button("🚀 Generate Manager Challenge"):
    prompt = f"Generate a challenge for restaurant managers related to {manager_task}. Provide actionable insights and reward criteria."
    st.text_area("📋 Manager Challenge:", get_ai_response(prompt), height=300)

# 👨‍🍳 **Staff Gamification**
st.header("👨‍🍳 Staff Training & Challenges")
staff_task = st.selectbox("Select a Staff Gamification Feature:", [
    "AI-Powered Training Modules",
    "Team Challenges"
])
if st.button("🎯 Generate Staff Challenge"):
    prompt = f"Create a {staff_task} challenge for restaurant staff. Include learning objectives and reward mechanisms."
    st.text_area("🏆 Staff Challenge:", get_ai_response(prompt), height=300)

# 🍽️ **Customer Gamification**
st.header("🎁 Customer Engagement & Rewards")
customer_task = st.selectbox("Select a Customer Gamification Feature:", [
    "AI-Powered Personalized Challenges",
    "Digital Loyalty Program with AI Suggestions",
    "AI-Generated Food Challenges",
    "Social Engagement & Rewards",
    "Personalized AI Chatbot Games"
])
if st.button("🎉 Generate Customer Challenge"):
    prompt = f"Develop a {customer_task} for restaurant customers. Provide engagement strategies and reward structures."
    st.text_area("🏆 Customer Challenge:", get_ai_response(prompt), height=300)

# 🖥️ **System Optimization Gamification**
st.header("⚙️ AI-Driven System Performance")
system_task = st.selectbox("Select a System Gamification Feature:", [
    "AI-Based System Monitoring Gamification",
    "AI-Powered Predictive Challenges",
    "AI-Driven Energy & Waste Reduction Gamification",
    "Dynamic AI Adjustments for Peak Hours",
    "Self-Learning AI Model Training Leaderboard"
])
if st.button("🔧 Generate System Optimization Task"):
    prompt = f"Create an AI-driven {system_task} for restaurant system optimization. Include KPIs and performance tracking methods."
    st.text_area("📊 System Optimization Task:", get_ai_response(prompt), height=300)

# ✅ Footer
st.write("🚀 Powered by Gemini 1.5 Pro with GenAI")
