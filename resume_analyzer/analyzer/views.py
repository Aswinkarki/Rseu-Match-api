import re
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import ResumeSerializer
from .skills_extractor import extract_skills
from .resume_scoring import score_resume, check_education, check_experience

class ResumeUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = ResumeSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

            # Extract text from the uploaded resume
            resume_text = file_serializer.instance.text

            # Extract skills from the resume
            resume_skills = extract_skills(resume_text)

            # Get job description dynamically from the request
            job_description = request.data.get("job_description", "").strip()

            if not job_description:
                return Response({"error": "Job description is required."}, status=status.HTTP_400_BAD_REQUEST)

            # Extract job skills dynamically
            job_skills = extract_skills(job_description)

            # Extract required education from job description
            education_requirements = self.extract_education_requirements(job_description)

            # Extract required experience from job description
            required_experience_years = self.extract_experience_years(job_description)

            # Score the resume based on skills
            score, matched_skills = score_resume(resume_skills, job_skills)

            # Check education and experience match
            education_match = check_education(resume_text) if education_requirements else True
            experience_match = check_experience(resume_text, required_experience_years)

            # Final scoring adjustments
            if education_match:
                score += 5  # Bonus for education match
            if experience_match:
                score += 5  # Bonus for experience match

            return Response({
                "resume_data": file_serializer.data,
                "extracted_skills": resume_skills,
                "job_description": job_description,
                "job_description_skills": job_skills,
                "required_experience_years": required_experience_years,
                "education_requirements": education_requirements,
                "resume_score": score,
                "matched_skills": matched_skills,
                "education_match": education_match,
                "experience_match": experience_match
            }, status=status.HTTP_201_CREATED)

        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def extract_experience_years(self, job_description):
        """Extract required years of experience from job description."""
        experience_match = re.search(r"(\d+)\s+years?\s+of\s+experience", job_description.lower())
        return int(experience_match.group(1)) if experience_match else 0

    def extract_education_requirements(self, job_description):
        """Extract required education degrees from job description."""
        education_keywords = ["Bachelor's", "Master's", "PhD", "Computer Science", "Engineering", "Information Technology"]
        found_education = [edu for edu in education_keywords if edu.lower() in job_description.lower()]
        return found_education if found_education else None
