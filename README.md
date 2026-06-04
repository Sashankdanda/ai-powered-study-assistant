# 🎓 AI-Powered Multi-Persona Study Assistant

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/sashankdanda00/StudyAssistant)

A production-deployed backend system that orchestrates a Large Language Model (LLM) to dynamically alter its tone, depth, and presentation structure based on 4 popular student/professional target personas.

🚀 **Live Production Demo:** [Try the App Natively on Hugging Face Spaces](https://huggingface.co/spaces/sashankdanda00/StudyAssistant)

<img width="1438" height="786" alt="Screenshot 2026-06-04 at 7 06 52 PM" src="https://github.com/user-attachments/assets/9feea825-909a-4e24-bc76-60fdf6847b2c" />


## 🛠️ Tech Stack & Architecture
* **Language:** Python 3
* **LLM Engine:** Google GenAI SDK (`gemini-2.5-flash`)
* **Interface Tier:** Gradio Web UI framework
* **Cloud Infrastructure:** Hugging Face Spaces Containerization

## 🧠 Architectural Highlights
* **Deterministic Guardrails:** Implemented rigid string configuration parsing inside the `GenerateContentConfig` context layer to restrict output blocks strictly to 3–4 paragraph structures, eliminating mid-sentence API responses.
* **Hyperparameter Calibration:** Maintained the execution runtime at a strict **0.4 Temperature** rating to ensure consistent accuracy while preventing model hallucinations during intricate system-design questions.
* **Network Binding:** Bound the web interface execution block to host layer `0.0.0.0` to handle public continuous cloud routing without internal container drops.
