# ⚖️ LawMindAI — AI Legal Assistant

An AI-powered multi-agent legal assistant built for **Indian law**. Describe your legal issue in plain English, and LawMindAI will analyze your case, identify applicable IPC sections, research legal precedents, and draft a formal legal document.

## ✨ Features

- **Case Intake & Analysis** — Classifies legal issues into structured categories (case type, legal domain, jurisdiction)
- **IPC Section Lookup** — Searches a vector database of Indian Penal Code sections to find relevant statutes
- **Legal Precedent Research** — Finds similar past court judgments from trusted Indian legal sources
- **Legal Document Drafting** — Generates formal complaints, FIRs, or legal notices

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| AI Framework | [CrewAI](https://crewai.com/) (Multi-Agent Orchestration) |
| LLM | Google Gemini 2.0 Flash |
| Vector Database | ChromaDB + HuggingFace Embeddings |
| Legal Search | Tavily API (indiankanoon.org) |
| Frontend | Streamlit |

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- API keys for Gemini, Tavily

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/LawMindAI.git
cd LawMindAI

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key  # Optional
PERSIST_DIRECTORY_PATH=./chromvector_db
IPC_COLLECTION_NAME=ipc_sections
```

### Run the App

```bash
streamlit run app.py
```

### CLI Mode

```bash
python main.py
```

## 🏗️ Architecture

```
LawMindAI/
├── app.py                    # Streamlit web interface
├── main.py                   # CLI entry point
├── crew.py                   # CrewAI orchestration
├── Agents/
│   ├── case_intake_agent.py  # Analyzes & classifies legal issues
│   ├── ipc_section_agent.py  # Finds relevant IPC sections
│   ├── legal_precedents_agent.py  # Researches case law
│   └── legal_drafter_agent.py     # Drafts legal documents
├── tasks/
│   ├── case_intake_task.py
│   ├── ipc_section_task.py
│   ├── legal_precedent_task.py
│   └── legal_drafter_task.py
├── tools/
│   ├── ipc_sections_search_tool.py    # ChromaDB vector search
│   └── legal_precedent_search_tool.py # Tavily web search
├── chromvector_db/           # Pre-built IPC vector database
├── ipc.json                  # Raw IPC sections data
└── ipc_vectordb_builder.py   # Script to rebuild vector DB
```

## 🌐 Deployment (Streamlit Cloud)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Connect your GitHub repository
4. Set the main file to `app.py`
5. Add your API keys in **Advanced Settings → Secrets**:
   ```toml
   GEMINI_API_KEY = "your_key"
   TAVILY_API_KEY = "your_key"
   PERSIST_DIRECTORY_PATH = "./chromvector_db"
   IPC_COLLECTION_NAME = "ipc_sections"
   ```
6. Deploy!

## ⚠️ Disclaimer

This tool provides AI-generated legal analysis for **informational purposes only**. It does not constitute legal advice. Please consult a qualified lawyer for professional guidance.

## 📄 License

MIT License
