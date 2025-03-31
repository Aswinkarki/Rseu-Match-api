from textblob import TextBlob

# Define a list of common tech skills (you can expand this later)
SKILL_KEYWORDS = {
    "Python", "Django", "Flask", "Machine Learning", "Data Science",
    "React", "JavaScript", "TypeScript", "Node.js", "SQL", "PostgreSQL",
    "MongoDB", "Docker", "Git", "AWS", "TensorFlow", "PyTorch", "FastAPI",
    "Redux", "API Development", "NLP", "Deep Learning", "Keras", "GraphQL"
}

def extract_skills(text):
    extracted_skills = set()

    # Create a TextBlob object
    blob = TextBlob(text)

    # Extract noun phrases from the text
    noun_phrases = blob.noun_phrases

    for phrase in noun_phrases:
        # Check if the noun phrase contains any of the skill keywords
        for skill in SKILL_KEYWORDS:
            if skill.lower() in phrase.lower():
                extracted_skills.add(skill)

    return list(extracted_skills)
