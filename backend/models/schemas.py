from pydantic import BaseModel


class UserInput(BaseModel):
    requirements: str


class ValidationResult(BaseModel):
    input: str
    is_valid: bool
    feedback: str | None = None
