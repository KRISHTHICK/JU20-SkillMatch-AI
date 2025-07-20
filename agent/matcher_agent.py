import os
import openai
from utils.score_utils import calculate_match_score, find_skill_gaps

openai.api_key = os.getenv("OPENAI_API_KEY")  # Set this in your env

def get_match_report(resume_text, jd_text):
    score = calculate_match_score(resume_text, jd_text)
    gaps = find_skill_gaps(resume_text, jd_text)
    
    prompt = f"""You are a hiring AI. Review this resume and job description.
    
    Resume:
    {resume_text[:1500]}

    Job Description:
    {jd_text[:1500]}

    Based on this, give feedback on how the candidate can improve their resume to match the JD.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "match_score": score,
        "skill_gaps": gaps[:20],
        "llm_feedback": response.choices[0].message.content.strip()
    }
