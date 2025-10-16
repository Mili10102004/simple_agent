# Task 1 — Structured Response Agent

Simple Flask agent that asks an LLM to return structured JSON for user queries.

## Run locally
1. Create virtualenv: python -m venv .venv
2. Activate: Windows: .venv\Scripts\activate ; mac/linux: source .venv/bin/activate
3. Install: pip install -r requirements.txt
4. Configure backend:
   - OpenAI: export OPENAI_API_KEY="sk-..." and optionally OPENAI_MODEL
   - OR Ollama: export OLLAMA_BASE_URL="http://localhost:11434" and OLLAMA_MODEL="your-model"
5. Start: python app.py
6. Open: http://127.0.0.1:5000

## Notes
- System prompt forces the model to reply with a single JSON object; backend parses it strictly.
- If model returns extra commentary, the parser attempts to extract the JSON substring.
