# app.py

import streamlit as st
import os
from modules.pdf_parser import extract_file_text
from modules.prompt_engine import build_audit_prompt
from modules.ollama_runner import query_ollama

st.set_page_config(page_title="🩺 MedAuditAI - Prescription Compliance Checker", layout="wide")

st.title("🩺 MedAuditAI")
st.subheader("Check if a prescription follows medical guidelines 🔍")

st.markdown("---")

# File upload
col1, col2 = st.columns(2)

with col1:
    guideline_files = st.file_uploader("📘 Upload Guidelines (PDF)", type=["pdf"], accept_multiple_files=True)

with col2:
    checklist_file = st.file_uploader("📋 Upload Prescription Checklist (PDF / DOCX)", type=["pdf", "docx"])
    prescription_file = st.file_uploader("🧾 Upload Patient Prescription Audit (PDF / DOCX)", type=["pdf", "docx"])


if st.button("🧠 Run Compliance Audit") and guideline_files and checklist_file and prescription_file:

    with st.spinner("📚 Extracting and analyzing..."):

                # Save and extract multiple guideline files
       guideline_texts = []
for file in guideline_files:
    file_path = os.path.join("pdfs", file.name)
    with open(file_path, "wb") as f:
        f.write(file.getvalue())

    extracted_text = extract_file_text(file_path)
    guideline_texts.append(extracted_text)

    # 👇 Print to terminal for debugging
    print(f"\n📄 Extracted text from: {file.name}\n{'='*60}")
    print(extracted_text[:3000])  # Print first 3000 characters
    print("="*60)


        # Save and extract prescription file

prescription_path = os.path.join("pdfs", prescription_file.name)
    with open(prescription_path, "wb") as f:
        f.write(prescription_file.getvalue())
    prescription_text = extract_file_text(prescription_path)

        # Save and extract checklist
        checklist_path = os.path.join("pdfs", checklist_file.name)
        with open(checklist_path, "wb") as f:
            f.write(checklist_file.getvalue())
        checklist_text = extract_file_text(checklist_path)

        # Build enhanced prompt
        full_prompt = build_audit_prompt(guideline_texts, prescription_text, checklist_text)


        # Get LLM response
        result = query_ollama(full_prompt)

        # Save output
        os.makedirs("outputs", exist_ok=True)
        with open("outputs/result_report.txt", "w", encoding="utf-8") as f:
            f.write(result)

    st.success("✅ Audit Completed!")
    st.markdown("### 📋 Compliance Report:")
    st.code(result, language="markdown")

    st.download_button("📥 Download Result", data=result, file_name="audit_report.txt")

elif st.button("🧠 Run Compliance Audit"):
    st.warning("⚠️ Please upload both files before running.")
