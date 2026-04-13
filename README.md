# 🏥 Multi-Agent Medical AI Assistant

> An AI-powered medical assistant that uses specialized agents to answer medical questions, check symptoms, and identify drug interactions — built with Mixtral-8x7B, LangChain, and Streamlit.

---

## 📌 Project Overview

This project implements a **multi-agent AI architecture** for medical information retrieval. Instead of a single generalist model, it routes queries to purpose-built agents — one for disease/treatment lookup, one for symptom checking, and one for drug interaction analysis — delivering more accurate, context-aware responses.

Designed with conversational memory so the assistant understands follow-up questions within the same session.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🔍 Medical Info Retrieval | Queries about diseases, symptoms, treatments, and medications |
| 🩺 Symptom Checker | Identifies possible conditions based on described symptoms |
| 💊 Drug Interaction Checker | Flags potential interactions between medications |
| 🧠 Conversational Memory | Maintains context across the full chat session |
| 📋 Real-time Logging | Tracks response times and outputs for performance monitoring |
| ⚡ High-Speed Inference | Powered by Mixtral-8x7B running on Groq's ultra-fast inference API |

---

## 🚀 Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.8+ |
| LLM | Mixtral-8x7B-32768 (via Groq) |
| Agent Framework | LangChain |
| Frontend | Streamlit |
| Memory | LangChain Conversational Memory |
| Logging | Python `logging` module |
| Config | python-dotenv |

---

## 🏗️ Multi-Agent Architecture

```
User Query
    ↓
LangChain Agent Orchestrator
    ↓
┌─────────────────┬──────────────────┬──────────────────────┐
│ Medical Info    │ Symptom Checker  │ Drug Interaction     │
│ Retrieval Agent │ Agent            │ Checker Agent        │
└─────────────────┴──────────────────┴──────────────────────┘
    ↓
Mixtral-8x7B on Groq (Fast Inference)
    ↓
Context-Aware Response (with Conversation Memory)
```

---

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/multi-agent-medical-ai-assistant.git
cd multi-agent-medical-ai-assistant
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:
```bash
GROQ_API_KEY=your_groq_api_key_here
```
> Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 5. Run the application
```bash
streamlit run app.py
```
Visit `http://localhost:8501` in your browser.

---

## 📂 Project Structure

```
multi-agent-medical-ai-assistant/
│
├── app.py              # Streamlit frontend — chat UI and session management
├── agents.py           # Agent definitions, tool logic, and memory management
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed to version control)
└── README.md           # Project documentation
```

---

## 📋 Logging & Monitoring

The app uses Python's built-in `logging` module to track:
- Agent routing decisions
- Model response content
- Response latency per query

Logs are printed to the console with timestamps and log levels for easy debugging.

---

## ⚠️ Disclaimer

> This tool is intended for **informational purposes only** and does not constitute medical advice. Always consult a qualified healthcare professional for medical decisions.

---

## 💡 Key Learnings & Takeaways

- Architected a **multi-agent system** with tool-use and dynamic routing via LangChain
- Integrated **Groq's low-latency inference API** for near real-time LLM responses
- Implemented **conversational memory** to maintain context across multi-turn dialogues
- Built a production-ready chat UI with **Streamlit** including session state management

---

## 🙏 Acknowledgements

- [LangChain](https://www.langchain.com/) — Agent orchestration framework
- [Groq](https://groq.com/) — Ultra-fast LLM inference
- [Streamlit](https://streamlit.io/) — Rapid frontend development

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

*Exploring multi-agent AI design patterns and LLM orchestration for domain-specific applications.*
