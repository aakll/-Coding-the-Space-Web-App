import streamlit as st
#from PIL import Image

# ----- Page Config -----
st.set_page_config(page_title="NASA NEO Hazard Predictor", layout="centered")

# ----- Background Styling -----
# Using Streamlit's safer theming approach instead of unsafe HTML
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
        color: white;
    }
    .main-header {
        text-align: center;
        color: #ffffff;
        padding: 20px 0;
    }
    </style>
""")

# ----- Header -----
st.markdown("<h1 class='main-header'>☄️ NASA NEO Hazard Predictor</h1>", unsafe_allow_html=False)

cols = st.columns(2)
with cols[0]:
    # Provide a working GitHub link or disable if not ready
    if st.button("🔗 GitHub Repository"):
        st.info("GitHub repository link will be available soon!")
with cols[1]:
    # Provide a working presentation link or disable if not ready  
    if st.button("🎥 View Presentation"):
        st.info("Presentation will be available soon!")

st.markdown("---")

# ----- File Upload Section -----
st.markdown("### 🛰️ Upload Near-Earth Object CSV Data")

uploaded_file = st.file_uploader("Upload your CSV file here", type=["csv"])
if uploaded_file:
    st.info("✅ File uploaded successfully! (Prediction model not yet connected)")

if st.button("🚀 Predict Hazard Status"):
    st.warning("⚠️ Prediction feature is not connected yet. Waiting for model.")

st.markdown("---")

# ----- Team Section -----
st.markdown("## 👥 Meet Our Team")

team = [
    {
        "name": "Ali Kawar",
        "role": "Web Developer",
        "linkedin": "https://linkedin.com/in/alikawar",
        "image": "https://avatars.githubusercontent.com/u/placeholder"  # You can replace with real link or local file
    },
    {
        "name": "Teammate A",
        "role": "Data Cleaning & Feature Engineering",
        "linkedin": "https://linkedin.com/in/teammatea",
        "image": "https://avatars.githubusercontent.com/u/placeholder"
    },
    {
        "name": "Teammate B",
        "role": "Model Development",
        "linkedin": "https://linkedin.com/in/teammateb",
        "image": "https://avatars.githubusercontent.com/u/placeholder"
    }
]

cols = st.columns(len(team))
for idx, member in enumerate(team):
    with cols[idx]:
        st.image(member["image"], width=150)
        st.markdown(f"**{member['name']}**")
        st.markdown(f"*{member['role']}*")
        st.markdown(f"[LinkedIn]({member['linkedin']})")

st.markdown("---")
st.markdown("Made with 🖤 by Team NASA NEO")

