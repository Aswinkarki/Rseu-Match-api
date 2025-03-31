# Define skill weights (you can modify based on job importance)
SKILL_WEIGHTS = {
    "Python": 10,
    "Django": 8,
    "React": 9,
    "Machine Learning": 7,
    "SQL": 8,
    "Docker": 6,
    "Flask": 5,
    "AWS": 7,
    "Git": 4,
    "TensorFlow": 6
}

def score_resume(resume_skills, job_skills):
    matched_skills = set(resume_skills).intersection(set(job_skills))

    # Calculate weighted match score
    weighted_score = sum(SKILL_WEIGHTS.get(skill, 1) for skill in matched_skills)
    
    # Normalize the score (total possible score / total job skill weight)
    total_possible_score = sum(SKILL_WEIGHTS.get(skill, 1) for skill in job_skills)
    match_percentage = (weighted_score / total_possible_score) * 100 if total_possible_score > 0 else 0

    return match_percentage, list(matched_skills)

# Education Matching
REQUIRED_EDUCATION = ["Bachelor's", "Computer Science", "Engineering", "Information Technology"]

def check_education(resume_text):
    for degree in REQUIRED_EDUCATION:
        if degree.lower() in resume_text.lower():
            return True
    return False

# Experience Matching
import re

def check_experience(resume_text, required_experience_years=2):
    experience_match = re.search(r"(\d+)\s+years?\s+of\s+experience", resume_text.lower())
    if experience_match:
        years_of_experience = int(experience_match.group(1))
        if years_of_experience >= required_experience_years:
            return True
    return False

# Certification Matching
REQUIRED_CERTIFICATIONS = ["AWS Certified", "Google Cloud Certified", "Microsoft Certified"]

def check_certifications(resume_text):
    for cert in REQUIRED_CERTIFICATIONS:
        if cert.lower() in resume_text.lower():
            return True
    return False

# Full Resume Evaluation Function
def evaluate_resume(resume_text, resume_skills, job_skills, required_experience_years=2):
    # Step 1: Score resume based on skills
    match_percentage, matched_skills = score_resume(resume_skills, job_skills)

    # Step 2: Check if resume meets education requirements
    education_match = check_education(resume_text)

    # Step 3: Check if resume meets experience requirements
    experience_match = check_experience(resume_text, required_experience_years)

    # Step 4: Check if resume meets certification requirements
    certification_match = check_certifications(resume_text)

    # Step 5: Calculate overall score based on all criteria
    overall_score = match_percentage
    if education_match:
        overall_score += 5  # Add a bonus for matching education
    if experience_match:
        overall_score += 5  # Add a bonus for meeting experience requirements
    if certification_match:
        overall_score += 5  # Add a bonus for certifications

    return {
        "score": overall_score,
        "skills": matched_skills,
        "education_match": education_match,
        "experience_match": experience_match,
        "certification_match": certification_match
    }
