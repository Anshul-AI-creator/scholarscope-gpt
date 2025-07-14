import os
import streamlit as st
import fitz  # PyMuPDF
import openai
import json
from dotenv import load_dotenv
from flask import Flask, request

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Constants
MAX_FILES_FREE = 3
MAX_WORDS_FREE = 10000
CHUNK_WORDS = 1500

# 🎨 UI Header
st.title("📚 ScholarScope GPT")
st.markdown("""
👋 Welcome to **ScholarScope GPT** – your AI-powered academic research assistant.

📄 Upload up to **3 papers**, and get:
- 🔍 Bullet-point summaries
- 💡 Project ideas you can build
- 🧠 Support for GPT-3.5 or GPT-4 (currently free)
""")

# 🎛️ Sidebar
st.sidebar.markdown("### 🧠 Scholar Settings")
st.sidebar.markdown("Choose model, check file count, and start exploring academic gold! ✨")
model_choice = st.sidebar.selectbox("Choose GPT Model", ["gpt-3.5-turbo (Free)", "gpt-4 (Pro)"])
model = "gpt-3.5-turbo" if "3.5" in model_choice else "gpt-4"

# 📈 Optional Support Section
st.sidebar.markdown("---")
st.sidebar.markdown("### ❤️ Support ScholarScope")
st.sidebar.markdown("This tool is currently free. If it helps you, consider supporting with ₹10!")
st.sidebar.link_button("☕ Buy me a coffee (₹10)", "https://rzp.io/rzp/4Do4JMBW")

# 📄 File Upload
st.divider()
st.subheader("📄 Upload Papers")
uploaded_files = st.file_uploader("Upload up to 3 PDF or TXT files", type=["pdf", "txt"], accept_multiple_files=True)

# 🧠 Prompt template
prompt_template = """
You are a helpful academic tutor.

A student has uploaded a research paper and is feeling overwhelmed. Your job is to:

1. Summarize the following excerpt in plain English using bullet points.
2. Suggest one realistic, beginner-friendly project idea based on the research.

Text:
{}
"""

# 🤩 Processing and Display
if uploaded_files:
    if len(uploaded_files) > MAX_FILES_FREE:
        st.error("❌ Free version allows only 3 files.")
    else:
        total_text = ""
        for file in uploaded_files:
            ext = file.name.split(".")[-1]
            if ext == "pdf":
                with fitz.open(stream=file.read(), filetype="pdf") as doc:
                    for page in doc:
                        total_text += page.get_text()
            elif ext == "txt":
                total_text += file.read().decode("utf-8")

        word_count = len(total_text.split())
        if word_count > MAX_WORDS_FREE:
            st.warning("⚠️ Truncating to 10,000 words (free tier).")
            total_text = " ".join(total_text.split()[:MAX_WORDS_FREE])

        final_prompt = prompt_template.format(total_text)

        if st.button("🚀 Run ScholarScope GPT"):
            words = total_text.split()
            chunks = [" ".join(words[i:i+CHUNK_WORDS]) for i in range(0, len(words), CHUNK_WORDS)]
            all_outputs = ""

            for i, chunk in enumerate(chunks):
                st.info(f"Processing chunk {i+1}/{len(chunks)}")
                prompt = prompt_template.format(chunk)
                try:
                    response = openai.ChatCompletion.create(
                        model=model,
                        messages=[
                            {"role": "system", "content": "You are a helpful academic tutor."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.7,
                        max_tokens=700
                    )
                    result = response.choices[0].message.content.strip()
                    all_outputs += f"\n\n📍 Chunk {i+1}:\n{result}"
                except Exception as e:
                    st.error(f"⚠️ API Error: {e}")
                    break

            st.subheader("📟 Summary Output")
            st.text_area("📋 Result", value=all_outputs.strip(), height=400)
            st.download_button("📎 Download", all_outputs, file_name="ScholarScope_Summary.txt")

else:
    st.info("📅 Upload your files to begin.")

# 📟 Footer
st.markdown("""
---
Made with ❤️ by Anshul Rai • Powered by OpenAI + Streamlit
""")

# 🪝 Razorpay Webhook Flask Server (separate service)
app = Flask(__name__)

@app.route('/razorpay-webhook', methods=['POST'])
def razorpay_webhook():
    data = request.json
    # Example: Log the event
    with open("payment_log.txt", "a") as f:
        f.write(json.dumps(data) + "\n")
    return '', 200

# Note: You must host this Flask app separately (e.g., on Render, Railway or locally with ngrok)
# Then register the webhook URL in Razorpay Dashboard > Settings > Webhooks
