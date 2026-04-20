import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Initialize Models
# Groq (Llama 3) for speed/JSON extraction
groq_llm = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=os.getenv("GROQ_API_KEY"))

# Gemini 1.5 Flash for Big Picture context
gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", google_api_key=os.getenv("GOOGLE_API_KEY"))

def analyze_resume(resume_text, jd_text):
    # 1. Groq: Extract Specific Skills (JSON Strike)
    skill_prompt = f"""
    Extract technical skills from this Resume: {resume_text}
    Compare them with this JD: {jd_text}
    Output ONLY a valid JSON with keys: "matched_skills", "missing_skills", "match_percentage".
    """
    skill_analysis = groq_llm.invoke(skill_prompt)

    # 2. Gemini: The "Recruiter" Persona (Big Picture)
    recruiter_prompt = f"""
    You are an expert Technical Recruiter. 
    Analyze this resume against the JD. 
    Resume: {resume_text}
    JD: {jd_text}
    Provide: 
    1. A brief summary of the candidate's fit.
    2. Three specific "ATS Optimizations" to improve the resume for this role.
    """
    general_analysis = gemini_llm.invoke(recruiter_prompt)
    
    return skill_analysis.content, general_analysis.content

def generate_roadmap(missing_skills):
    if not missing_skills:
        return "You already have all the core skills! Focus on your projects."
    
    prompt = f"""
    Acting as a Senior Technical Mentor, create a concise 4-week learning roadmap 
    to master these missing skills: {', '.join(missing_skills)}.
    Keep it actionable with specific topics to cover each week.
    """
    roadmap = gemini_llm.invoke(prompt)
    return roadmap.content