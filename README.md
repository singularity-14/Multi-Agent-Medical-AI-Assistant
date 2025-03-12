# Multi-Agent-Medical-AI-Assistant

## Overview

The Multi-Agent-Medical-AI-Assistant Assistant is a powerful tool designed to provide AI-powered responses to medical questions. It leverages advanced language models and multiple specialized agents to retrieve medical information, check symptoms, and identify drug interactions. This project is built using Streamlit for the frontend and LangChain for the backend AI functionalities.

## Features

- **Medical Information Retrieval**: Retrieve medical information about diseases, symptoms, treatments, and drugs.
- **Symptom Checker**: Check symptoms and identify possible medical conditions.
- **Drug Interaction Checker**: Check for interactions between drugs.
- **Conversational Memory**: Maintain conversation history to provide context-aware responses.
- **Real-time Logging**: Monitor responses and response times for better performance tracking.
- **LLM**: ```mixtral-8x7b-32768```

## Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment (optional but recommended)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/medical-ai-assistant.git
   cd medical-ai-assistant
   ```

2. **Create a virtual environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root and add your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

### Running the Application

1. **Start the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Access the application**:
   Open your web browser and navigate to `http://localhost:8501`.

### Interacting with the Assistant

- **Ask Medical Questions**: Enter your medical questions in the chat input box.
- **View Responses**: The assistant will provide AI-powered responses based on the input.
- **Chat History**: The conversation history is displayed in the chat interface.

## Project Structure

- **`agents.py`**: Contains the backend logic for the AI agent, including tool definitions, memory management, and agent execution.
- **`app.py`**: Contains the Streamlit frontend code for the chat interface.
- **`.env`**: Environment variables file (not included in the repository for security reasons).
- **`requirements.txt`**: List of Python dependencies.

## Logging

The application uses Python's built-in `logging` module to monitor responses and response times. Logs are printed to the console with timestamps, log levels, and messages.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Groq](https://groq.com/)

---
