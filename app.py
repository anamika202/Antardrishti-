import streamlit as st
from google import genai

# Page config
st.set_page_config(
    page_title="Antardrishti AI",
    page_icon="👁️",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; font-weight: 700; color: #1E88E5; }
    .tagline { font-size: 1rem; color: #555; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">👁️ Antardrishti AI</div>', unsafe_allow_html=True)
st.markdown('<div class="tagline">Empowering Insights & Accessible Intelligence</div>', unsafe_allow_html=True)

# Fetch API Key securely
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("API Key configure nahi hai! Streamlit Cloud Settings > Secrets me GEMINI_API_KEY add karein.")
    st.stop()

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

# App Modes
mode = st.radio(
    "Select Mode:",
    ["Text & Reasoning Analysis", "Multimodal / Image Insight"],
    horizontal=True
)

if mode == "Text & Reasoning Analysis":
    user_prompt = st.text_area("Enter context, inquiry, or document summary:", placeholder="Type here...")
    
    if st.button("Generate Insight", type="primary"):
        if not user_prompt.strip():
            st.warning("Kripya input provide karein.")
        else:
            with st.spinner("Analyzing with Gemini..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=user_prompt
                    )
                    st.success("Analysis Complete")
                    st.markdown("### Output Insight:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error generating response: {e}")

elif mode == "Multimodal / Image Insight":
    uploaded_file = st.file_uploader("Upload an image for analysis:", type=["jpg", "jpeg", "png"])
    image_prompt = st.text_input("Prompt for image:", value="Analyze this image and describe its key elements clearly.")
    
    if uploaded_file and st.button("Analyze Image", type="primary"):
        with st.spinner("Processing visual data..."):
            try:
                import PIL.Image
                img = PIL.Image.open(uploaded_file)
                st.image(img, caption="Uploaded Image", use_container_width=True)
                
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=[img, image_prompt]
                )
                st.success("Visual Analysis Complete")
                st.markdown("### Output Insight:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
              
