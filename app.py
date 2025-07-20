import streamlit as st
from utils.extract_text import extract_text
from agent.matcher_agent import get_match_report

st.set_page_config(page_title="SkillMatch AI", layout="wide")
st.title("🧠 SkillMatch AI – Resume vs JD Matcher")

resume_file = st.file_uploader("📄 Upload your Resume", type=["pdf", "docx"])
jd_file = st.file_uploader("📝 Upload Job Description", type=["pdf", "docx"])

if resume_file and jd_file:
    resume_text = extract_text(resume_file)
    jd_text = extract_text(jd_file)

    with st.spinner("Analyzing match..."):
        report = get_match_report(resume_text, jd_text)
    
    st.subheader("🔢 Match Score")
    st.metric(label="Resume-JD Match %", value=f"{report['match_score']}%")

    st.subheader("📌 Skill Gaps")
    st.write(report['skill_gaps'])

    st.subheader("📝 LLM Feedback")
    st.write(report['llm_feedback'])
