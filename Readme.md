# ScholarScope: AI-Powered Academic Research Assistant

A Streamlit-based application that helps researchers and students discover, summarize, and generate project ideas from the latest academic papers across multiple domains using state-of-the-art AI.

## 🚀 Key Features

* **Paper Fetching**: Retrieve up-to-date research papers from ArXiv and Semantic Scholar by keyword or topic.
* **AI Summarization**: Generate clear, concise summaries in plain English for complex academic texts.
* **Project Idea Generator**: Create practical project or experiment suggestions based on summarized content.
* **Multi-Domain Support**: Works across AI, psychology, education, healthcare, and more.
* **Flexible Output**: Export results as PDF, email reports, or view directly in the web interface.
* **Telegram Bot Integration**: Optionally receive summaries and ideas via a Telegram bot for on-the-go access.
* **File Upload & Export**: Upload PDF manuscripts or exported results as downloadable files.

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/ScholarScope.git
   cd ScholarScope
   ```
2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\\Scripts\\activate  # Windows
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure API Keys**

   * `OPENAI_API_KEY`: OpenAI API key for GPT summarization.
   * `ARXIV_API_KEY` (optional): Your ArXiv API key.
   * `S2_API_KEY` (optional): Semantic Scholar API key.
     Set these in your environment or in a `.env` file.

## 💡 Usage

### Local Web Interface (Streamlit)

```bash
streamlit run app.py
```

* Open your browser at `http://localhost:8501`.
* Enter a topic or upload a PDF to start.

### Command-Line Interface

```bash
python scholar_scope.py \
  --query "deep learning optimization" \
  --summarize \
  --generate-ideas
```

### Telegram Bot

1. Set `TELEGRAM_TOKEN` in your environment.
2. Run:

   ```bash
   python bot.py
   ```
3. Interact with the bot: `/search quantum computing`

## 🛣️ Roadmap

* [ ] Add support for batch downloads
* [ ] Integrate email notifications
* [ ] Domain-specific customization templates
* [ ] Dashboard for tracking saved summaries and ideas

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.

---

*Created with ❤️ by ScholarScope Team*
