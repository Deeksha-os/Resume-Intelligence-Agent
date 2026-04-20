import PyPDF2

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

import re

def clean_json_string(text):
    # This regex finds everything between ```json and ``` or just ``` and ```
    match = re.search(r'```json?\s*(.*?)\s*```', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()

from fpdf import FPDF

def create_pdf_report(score, matched, missing, feedback):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Resume Intelligence Report", ln=True, align='C')
    
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"ATS Match Score: {score}%", ln=True)
    
    pdf.ln(5)
    pdf.cell(200, 10, txt="Matched Skills: " + ", ".join(matched), ln=True)
    pdf.cell(200, 10, txt="Missing Skills: " + ", ".join(missing), ln=True)
    
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt="Recruiter Feedback:\n" + feedback)
    
    # Save to a temporary file
    report_path = "Analysis_Report.pdf"
    pdf.output(report_path)
    return report_path