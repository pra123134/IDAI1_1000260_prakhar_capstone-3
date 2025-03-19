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
st.set_page_config(page_title="AI Gamified Smart Restaurant Management", layout="wide")

st.title("🍽️ AI Gamified Smart Restaurant Management with Gemini 1.5 Pro")
st.write("🚀 Optimize management, training, and customer engagement through AI-driven gamification.")

# 🎯 **Manager Gamification**
st.header("🏆 Manager Decision-Making Challenges")

decision_challenge = st.text_area("🧠 Enter a business challenge (e.g., High Waste, Low Sales)")
if st.button("⚡ Generate Optimization Challenge"):
    prompt = f"""
    Provide an AI-driven decision-making challenge for a restaurant manager.
    Challenge: {decision_challenge}
    Include:
    - Optimization strategies
    - Performance tracking
    - Points system for improvements
    """
    st.text_area("🎯 AI Challenge:", get_ai_response(prompt), height=300)

# 📊 **Staff Training & Performance**
st.header("📚 AI-Powered Staff Training & Challenges")

training_type = st.selectbox("📖 Select Training Type", ["Peak Hour Handling", "Waste Reduction", "Efficient Table Management"])
if st.button("🚀 Start Training Challenge"):
    prompt = f"""
    Generate an AI-powered training module for restaurant staff.
    Training Type: {training_type}
    Include:
    - Key skills
    - Interactive challenge
    - Performance leaderboard criteria
    """
    st.text_area("🎓 Training Module:", get_ai_response(prompt), height=300)

# 🍽️ **Customer Engagement Gamification**
st.header("🎮 AI-Powered Customer Challenges")

customer_challenge = st.selectbox("🎯 Select a Customer Challenge", ["Try 3 New Dishes", "Rate Dishes for Points", "Order a Mystery Dish", "Social Media Engagement"])
if st.button("🎁 Generate Customer Challenge"):
    prompt = f"""
    Create an AI-powered customer challenge to enhance engagement.
    Challenge: {customer_challenge}
    Include:
    - Rewards system
    - Challenge description
    - AI-driven personalization
    """
    st.text_area("🏆 Customer Challenge:", get_ai_response(prompt), height=300)

# 🔄 **System Gamification & AI Performance Monitoring**
st.header("📡 AI-Driven System Optimization & Monitoring")

system_metric = st.selectbox("⚙️ Select System Metric", ["Order Processing Speed", "Inventory Efficiency", "Energy & Waste Reduction"])
if st.button("📈 Generate AI System Monitoring Challenge"):
    prompt = f"""
    Develop an AI-based system gamification challenge.
    Metric: {system_metric}
    Include:
    - AI tracking mechanisms
    - Performance scoring
    - Self-optimization recommendations
    """
    st.text_area("📊 System Challenge:", get_ai_response(prompt), height=300)

# 🚀 **Top 10 AI Features in Smart Restaurant Management**
st.header("🔟 Top 10 AI Gamification Features")

top_ai_features = """
1️⃣ AI Decision-Making Challenges for Managers
2️⃣ Predictive AI Bottleneck Simulations
3️⃣ Sustainability Challenges for Managers
4️⃣ AI-Powered Peak Hour Insights
5️⃣ Staff Training Modules with AI-Based Evaluation
6️⃣ Real-Time Staff Performance Challenges
7️⃣ AI-Powered Personalized Customer Challenges
8️⃣ AI-Based System Performance Monitoring
9️⃣ AI-Driven Predictive System Challenges
🔟 AI Self-Learning & Leaderboard Tracking
"""
st.text_area("🌟 Top AI Features:", top_ai_features, height=300)

# ✅ Footer
st.write("🚀 Powered by Gemini 1.5 Pro with GenAI")
