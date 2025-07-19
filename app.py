import streamlit as st
#from PIL import Image

# ----- Page Config -----
st.set_page_config(page_title="NASA NEO Hazard Predictor", layout="centered")

# ----- Background Styling -----
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1588167101412-e014af974c40?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ----- Header -----
st.markdown("<h1 style='text-align: center;'>☄️ NASA NEO Hazard Predictor</h1>", unsafe_allow_html=True)

cols = st.columns(2)
with cols[0]:
    st.link_button("🔗 GitHub Repository", "https://github.com/yourrepo")  # Replace later
with cols[1]:
    st.link_button("🎥 View Presentation", "https://your-presentation-link.com")  # Replace later

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

