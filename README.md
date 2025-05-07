# SHL Assessment Recommender

An intelligent RAG-based (Retrieval-Augmented Generation) system that leverages SHL assessment data to recommend relevant evaluations for roles or skill profiles. This project uses OpenRouter (LLM), pandas, NumPy, FAISS for vector search, and provides both an API and a Streamlit-based user interface.

---

## 🧠 Project Overview

This system is designed to streamline and automate the recommendation of SHL assessments based on user queries or job descriptions. It processes structured CSV data (`assessments.csv`) and uses vector embeddings to match semantic similarity.

---

## 📁 Directory Structure

shl_assessment/
│
├── api/ # FastAPI service for backend processing
│ └── index.py
│
├── rag_recommender/ # Core logic and data
│ ├── data/
│ │ ├── assessment.csv # Main CSV dataset
│ │ └── assessments.csv
│ ├── modules/
│ │ ├── .gitignore
│ │ ├── LICENSE
│ │ ├── embeddings.npy # Pre-computed embedding vectors
│ │ └── main.py # Entry-point for internal logic
│ ├── templates/
│ │ ├── README.md
│ │ ├── app.py # Streamlit UI
│ │ ├── embeddings.npy
│ │ ├── requirements.txt
│ │ ├── test_adc.py
│ │ ├── vector.index
│ │ └── vector.json
│ ├── app.py # Global entry-point (CLI / launcher)
│ ├── main.py # Launches and manages modules
│ ├── run_indexing.py # Embedding + vector indexing pipeline
│ └── openrouter_api.py # Integration with OpenRouter LLM API
│
├── vector_texts.pkl # Pickled vector text info
├── vercel.json # Configuration for Vercel deployment
├── requirements.txt # Dependencies
└── README.md # You're here

yaml
Copy
Edit

---

## 🚀 Features

- 🔍 **RAG-based Retrieval**: Finds contextually relevant SHL assessments from a CSV source.
- 💬 **LLM Integration (OpenRouter)**: Uses OpenRouter API to generate semantically rich embeddings and responses.
- 🧩 **Modular Components**: Includes separate FastAPI backend and Streamlit frontend.
- ⚡ **Local Vector Indexing**: Embedding vectors managed via FAISS or NumPy.
- 🧪 **Testing & Debugging**: Comes with `test_adc.py` for system validation.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/agrawal-sneha/shl_assessment.git
cd shl_assessment
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Prepare the Data
Ensure assessments.csv is properly formatted and placed under rag_recommender/data/.

4. Index the Dataset
bash
Copy
Edit
python rag_recommender/run_indexing.py
5. Run the API (FastAPI)
bash
Copy
Edit
uvicorn api.index:app --reload
6. Run the Streamlit UI
bash
Copy
Edit
streamlit run rag_recommender/templates/app.py
🧠 How it Works
User Query → sent via UI or API

Embedding → query is converted into a vector using OpenRouter

Vector Search → similarity match against pre-indexed assessments.csv data

Contextual Output → recommended SHL assessments are returned

🔐 Environment Variables
Create a .env file in the root with:

env
Copy
Edit
OPENROUTER_API_KEY=your_openrouter_api_key
🧪 Testing
bash
Copy
Edit
python rag_recommender/templates/test_adc.py
📊 Sample Data Format
assessments.csv

csv
Copy
Edit
Role,Assessment Title,Category,Skills Measured,Level
Data Scientist,Cognitive Ability,Logic/Numeracy,Reasoning,Advanced
Software Engineer,Code Comprehension,Technical,Programming,Basic
🧩 Customization
New Data Source: Replace or update rag_recommender/data/assessments.csv.

Embedding Model: Update openrouter_api.py to switch between OpenRouter-supported models.

UI Changes: Modify Streamlit layout in templates/app.py.

Backend Logic: Extend main.py and index.py for custom recommendation logic.

📦 Deployment (Vercel)
Configure deployment for the Streamlit frontend or FastAPI backend using vercel.json.
