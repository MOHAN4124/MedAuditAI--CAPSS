# 🩺 MedAuditAI - Medical Prescription Compliance Checker

MedAuditAI is a secure, local AI-powered auditing tool that verifies whether a patient’s prescription aligns with nephrology medical guidelines. Built with Streamlit and locally running LLMs (via Ollama), it helps automate clinical audits and ensure safe, guideline-compliant treatment.

---

## 🚀 Features

* 🧠 Uses local LLMs (e.g., Phi, Gemma via Ollama) — no cloud data exposure
* 📑 Accepts multiple medical guideline PDFs
* 📋 Upload prescription and checklist (PDF/DOCX)
* ✅ Returns compliance report: checklists, deviations, score, and recommendations
* 🔐 No data leaves your system (privacy-focused)
* 🧾 Downloadable audit report

---

## 📁 Project Structure

```
MedAuditAI/
├── app.py                         # Main Streamlit app
├── requirements.txt              # Python dependencies
├── README.md                     # Project overview
│
├── pdfs/                         # Uploaded input files
│   ├── KDIGO-Guideline.pdf
│   └── Sample_Prescription.docx
│
├── outputs/                      # Audit results
│   └── result_report.txt
│
├── prompts/                      # LLM prompt templates
│   └── audit_prompt_template.txt
│
├── modules/                      # Helper modules
│   ├── pdf_parser.py             # PDF/DOCX text extractor
│   ├── prompt_engine.py          # Prompt builder logic
│   ├── ollama_runner.py          # LLM communication (Ollama)
│   └── utils.py                  # Misc utilities
│
└── data/                         # Placeholder for fine-tuning dataset
    └── training_dataset.jsonl
```

---

## 🛠️ Setup Instructions


### 1. Create and activate virtual environment

```bash
python -m venv venv     # On Windows
# Or
source venv/bin/activate   # On Linux/Mac
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install and start Ollama (for local LLM)

Go to [https://ollama.com](https://ollama.com) and install for your OS.
Then pull a model:

```bash
ollama pull phi
ollama serve
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

OR

 Local URL: http://localhost:8501
  Network URL: http://192.168.86.200:8501

---

## 📌 How It Works

1. Upload multiple **nephrology guidelines** in PDF format
2. Upload the **prescription audit** (PDF/DOCX)
3. Upload the **prescription checklist** (PDF/DOCX)
4. Click **Run Compliance Audit**
5. The LLM compares everything and outputs:

   * Checklist with ✅/❌/⚠️
   * Compliance Score
   * Deviations & Safety Risks
   * Final Verdict + Recommendations

---

## ✅ Technologies Used

* 🧠 LLM via [Ollama](https://ollama.com/) (e.g., Phi, Gemma, Mistral)
* 🐍 Python 3.11+
* 📊 Streamlit
* 📄 PyMuPDF (for PDF parsing)
* 📑 python-docx (for DOCX parsing)

---

## 🔒 Data Privacy

This app does **not** send any data to the cloud. Everything runs **locally** on your machine.
Perfect for medical environments with strict compliance requirements (HIPAA, GDPR, etc.).

---

## 📧 Contact / Contributions

* Developed by: `Mohan A.`
* For suggestions, improvements, or forks — feel free to contribute!

---

