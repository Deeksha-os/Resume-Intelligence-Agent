# Resume Intelligence Agent
### **ATS Optimization & Career Pathing for Students**

The **Resume Intelligence Agent** is an AI-powered recruitment tool designed to help job seekers bridge the gap between their current skills and industry requirements. By leveraging a **Hybrid Multi-LLM architecture**, the tool provides deep semantic analysis, real-time ATS scoring, and personalized upskilling roadmaps.

---

## Features
* **Hybrid AI Engine:** Orchestrates **Llama 3.3 (via Groq)** for high-speed data extraction and **Gemini 2.5 Flash Lite** for expert recruiter reasoning.
* **ATS Match Scoring:** Calculates a real-time match percentage based on Job Description (JD) requirements.
* **Automated Skill Gap Analysis:** Identifies specific missing technologies and provides strategic "ATS Optimizations."
* **4-Week 'Path to Hired' Roadmap:** Generates a week-by-week study plan to master missing competencies.
* **Professional PDF Export:** Allows users to download a full intelligence report for offline review or mentoring.

---

## Architecture & Workflow
The project follows a modular **Agentic Workflow**:
1. **Extraction:** `PyPDF2` parses the raw text from the uploaded Resume.
2. **Analysis Agent (Groq):** Extracts structured data (JSON) regarding matched and missing skills with sub-second latency.
3. **Recruiter Agent (Gemini):** Performs deep contextual analysis to provide strategic feedback and career roadmaps.
4. **UI/UX (Streamlit):** Visualizes results through a modern, responsive dashboard.

---

## Tech Stack
* **Framework:** [LangChain](https://www.langchain.com/)
* **Frontend:** [Streamlit](https://streamlit.io/)
* **LLMs:** * Llama-3.3-70b-versatile (via Groq)
    * Gemini-2.5-Flash-Lite (via Google AI)
* **Libraries:** `PyPDF2`, `fpdf`, `python-dotenv`, `google-generativeai`

---

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/your-username/Resume-Intelligence-Agent.git](https://github.com/your-username/Resume-Intelligence-Agent.git)
   cd Resume-Intelligence-Agent
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Environment Variable**
   Create a .env file in the root directory (refer to .env.example):
   GROQ_API_KEY=your_groq_api_key
   GOOGLE_API_KEY=your_google_api_key
4. **Run the Application:**
   ```bash
   streamlit run app.py

**Link of working Streamlit:** https://resume-intelligence-agentgit-y5inoyxdykqetrks6vdqio.streamlit.app/
   
