from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class HealthResponse(BaseModel):
    status: str
    service: str


class DemoLoginResponse(BaseModel):
    demo: bool
    user_id: str
    display_name: str
    application_id: str
    message: str


class ApplicationResponse(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    application_id: str
    service_name: str
    claim_type: str
    status: str
    submitted_date: date
    current_stage: str
    issue: str
    documents_status: str
    next_action: str


class ClaimExplanationResponse(BaseModel):
    application_id: str
    status: str
    what_happened: str
    why: str
    what_now: list[str]
    demo: bool


class GrievanceDraftResponse(BaseModel):
    application_id: str
    subject: str
    message: str
    demo: bool


class GrievanceSubmitRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    application_id: str = Field(min_length=1)
    subject: str = Field(min_length=1, max_length=200)
    message: str = Field(min_length=1, max_length=2_000)


class GrievanceSubmissionResponse(BaseModel):
    reference_number: str
    application_id: str
    status: str
    message: str
    demo: bool
