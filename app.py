import streamlit as st
import json
import os
from utils import extract_text_from_pdf, clean_json_string, create_pdf_report
from agent_logic import analyze_resume, generate_roadmap

# 1. Page Configuration
st.set_page_config(
    page_title="Resume Intelligence Agent",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS to make it look modern
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header Section
st.title("🤖 Resume Intelligence Agent")
st.subheader("ATS Optimization & Career Pathing for CSE Students")
st.markdown("---")

# 3. Input Section (Two Columns)
col1, col2 = st.columns(2)

with col1:
    st.header("📄 1. Upload Resume")
    resume_file = st.file_uploader("Upload your Resume (PDF format)", type="pdf")
    st.info("Tip: Ensure your PDF text is selectable (not a scanned image).")

with col2:
    st.header("📝 2. Job Description")
    jd_text = st.text_area("Paste the target Job Description (JD) here...", height=215)

# 4. Analysis Logic
if st.button("🚀 Run Intelligence Analysis", use_container_width=True):
    if resume_file and jd_text:
        with st.spinner("Our AI Agents are collaborating on your profile..."):
            
            # Step A: Extraction
            resume_text = extract_text_from_pdf(resume_file)
            
            # Step B: LLM Analysis
            # Returns: (Raw JSON from Groq, Expert Tips from Gemini)
            skills_json_raw, feedback = analyze_resume(resume_text, jd_text)
            
            # Step C: Cleaning & Parsing
            cleaned_json = clean_json_string(skills_json_raw)
            
            try:
                data = json.loads(cleaned_json)
                
                # --- DASHBOARD DISPLAY ---
                st.success("Analysis Complete!")
                
                # Big Match Score
                score = data.get("match_percentage", 0)
                st.metric(label="Overall ATS Match Score", value=f"{score}%")
                
                # Matched vs Missing Skills
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown("### ✅ Matched Skills")
                    matched_list = data.get("matched_skills", [])
                    if matched_list:
                        for skill in matched_list:
                            st.success(f"**{skill}**")
                    else:
                        st.write("No direct matches found.")
                
                with c2:
                    st.markdown("### 🚩 Missing Skills")
                    missing_list = data.get("missing_skills", [])
                    if missing_list:
                        for skill in missing_list:
                            st.error(f"**{skill}**")
                    else:
                        st.write("You have all the required skills!")

                # --- EXPERT FEEDBACK SECTION ---
                st.markdown("---")
                st.header("👔 Recruiter Feedback & ATS Tips")
                st.info(feedback)

                # --- LEARNING ROADMAP SECTION ---
                st.markdown("---")
                st.header("🚀 4-Week 'Path to Hired' Roadmap")
                with st.expander("View Your Personalized Study Plan", expanded=True):
                    roadmap = generate_roadmap(missing_list)
                    st.markdown(roadmap)

                # --- PDF EXPORT SECTION ---
                st.markdown("---")
                # Generate the PDF file
                report_path = create_pdf_report(score, matched_list, missing_list, feedback)
                
                with open(report_path, "rb") as f:
                    st.download_button(
                        label="📥 Download Full Intelligence Report (PDF)",
                        data=f,
                        file_name=f"Resume_Analysis_Score_{score}.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
                
                # Cleanup: Optional - remove file after download if needed
                # os.remove(report_path)

            except Exception as e:
                st.error("The Agent encountered a formatting error. Here is the raw output:")
                st.code(skills_json_raw)
                st.exception(e)
    else:
        st.warning("Please provide both your Resume and the Job Description to start the analysis.")

# 5. Footer
st.markdown("---")
st.caption("Powered by Gemini 2.5 Flash Lite & Llama 3.3 via Groq | Built by Deeksha D Shenoy")