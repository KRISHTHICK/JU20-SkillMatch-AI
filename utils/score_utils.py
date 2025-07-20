def calculate_match_score(resume_text, jd_text):
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())
    common = resume_words & jd_words
    return round((len(common) / len(jd_words)) * 100, 2)

def find_skill_gaps(resume_text, jd_text):
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())
    return list(jd_words - resume_words)
