from fastapi import APIRouter
from backend.models.schemas import UserInput
from backend.controllers.ba_controller import run_ba_workflow

router = APIRouter(prefix="/ba_workflow", tags=["BA Workflow"])


@router.post("/input", response_model=UserInput)
async def ba_workflow(input: UserInput):
    inputs = input.model_dump()
    result = run_ba_workflow(inputs)

    return {"result": result}
