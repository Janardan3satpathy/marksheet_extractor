from pydantic import BaseModel, Field
from typing import List, Optional

class MarksheetSubject(BaseModel):
    subject_name: str = Field(..., description="Name of the subject")
    max_marks: Optional[float] = Field(None, description="Maximum marks")
    obtained_marks: Optional[float] = Field(None, description="Marks obtained")
    grade: Optional[str] = Field(None, description="Grade letter")
    confidence_score: float = Field(..., description="0-1 confidence score based on clarity")

class CandidateDetails(BaseModel):
    name: Optional[str] = Field(None, description="Candidate's full name")
    roll_no: Optional[str] = Field(None, description="Roll number")
    registration_no: Optional[str] = Field(None, description="Registration number")
    dob: Optional[str] = Field(None, description="Date of Birth (YYYY-MM-DD)")
    father_name: Optional[str] = None
    mother_name: Optional[str] = None
    exam_year: Optional[str] = None
    institution: Optional[str] = None

class ExtractionResponse(BaseModel):
    candidate: CandidateDetails
    results: List[MarksheetSubject]
    overall_grade: Optional[str] = Field(None, description="Final Result/Division")
    issue_date: Optional[str] = None
    extraction_confidence: float = Field(..., description="Overall confidence score")