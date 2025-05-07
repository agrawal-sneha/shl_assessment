# 🧠 SHL Assessment Recommender

[![Streamlit UI](https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![FastAPI Backend](https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![OpenRouter LLM](https://img.shields.io/badge/OpenRouter-LLM-blueviolet?style=for-the-badge)](https://openrouter.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](./LICENSE)

---

## 🌟 Overview

This project is a **Retrieval-Augmented Generation (RAG)** system to recommend **[SHL](https://www.shl.com/en/assessments/)** assessments based on job roles, skill descriptions, or natural language queries.

🔍 **Semantic search**  
⚙️ **FastAPI backend** + 🧠 **LLM integration**  
🖥️ **Streamlit-powered UI**  
📁 **CSV-based data source** (no database needed)

---

## 📊 System Flowchart

The following diagram illustrates the architecture of the system from query input to recommendation:

![SHL Flowchart](docs/shl_assessment_flowchart.png)

> 🗂 **Place this image at:** `docs/shl_assessment_flowchart.png`

---

## 📁 Directory Structure

```
shl_assessment/
├── api/                          # FastAPI service
│   └── index.py
├── rag_recommender/             # Core RAG logic
│   ├── data/
│   │   ├── assessment.csv
│   │   └── assessments.csv
│   ├── modules/
│   ├── embeddings.npy
│   ├── main.py
│   ├── run_indexing.py
│   └── openrouter_api.py
├── templates/
│   └── README.md
├── app.py                        # Launch Streamlit UI
├── test_adc.py                   # Test file
├── vector.index
├── vector.json
├── vector_texts.pkl
├── vercel.json
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 Quickstart

### 📥 1. Clone the Repository

```bash
git clone https://github.com/agrawal-sneha/shl_assessment.git
cd shl_assessment
```

### ⚙️ 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 📂 3. Add Your Data

Place your `assessments.csv` inside:

```bash
rag_recommender/data/
```

---

## 🧠 Generate Vector Index

```bash
python rag_recommender/run_indexing.py
```

---

## 🌐 Run the Application

### 🔌 FastAPI Backend

```bash
uvicorn api.index:app --reload
```

### 🖥️ Streamlit UI

```bash
streamlit run app.py
```

---

## 🧪 Testing

Run test validation:

```bash
python test_adc.py
```

---

## 🌍 Resources

- 🔗 [SHL Official Site](https://www.shl.com/en/assessments/)
- 🤖 [OpenRouter](https://openrouter.ai)
- 🎈 [Streamlit](https://streamlit.io)
- ⚡ [FastAPI](https://fastapi.tiangolo.com/)

---

## 📝 License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE).

---

## 👩‍💻 Maintainer

**Sneha Agrawal**  
GitHub: [@agrawal-sneha](https://github.com/agrawal-sneha)

---
