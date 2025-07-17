# modules/prompt_engine.py

def build_audit_prompt(guideline_texts, prescription_audit_text, prescription_checklist_text):
    combined_guidelines = "\n\n".join(guideline_texts)

    prompt = f"""
You are a highly skilled medical auditor specializing in nephrology. Your task is to ensure that a prescription audit aligns strictly with standard medical guidelines.

You are provided with:
- 📘 Multiple nephrology guideline documents (combined below)
- 📄 A prescription audit
- ✅ A prescription audit checklist format

Your responsibilities:
1. Act as an expert in nephrology and understand the guidelines deeply.
2. Review the prescription audit against the combined guidelines.
3. Use the checklist format to verify each item as:
   - ✅ Compliant
   - ❌ Non-Compliant
   - ⚠️ Missing but Optional
4. Fill the checklist in the same order as provided.
5. Highlight any deviations, medical risks, or missing data.
6. Calculate and display the compliance percentage.
7. End with a Final Verdict: ✅ Safe | ⚠️ Needs Review | ❌ Risky.

---
📘 Medical Guidelines:
{combined_guidelines}

📄 Prescription Audit:
{prescription_audit_text}

✅ Checklist Format:
{prescription_checklist_text}
---

🧾 Respond in this format ONLY:

📋 Checklist:
1. [✅] Item 1: ...
2. [❌] Item 2: ...
3. [⚠️] Item 3: ...

📊 Compliance Score: 92%

🚨 Deviations / Issues:
- Drug X was not found in guidelines
- Dosage Y is above safe limit for Class IV patients

✅ Recommendations:
- Replace Drug X with Drug Y
- Lower dosage to 25 mg

🔚 Final Verdict: "Needs Review"
"""
    return prompt.strip()
