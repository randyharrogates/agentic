from fastapi import FastAPI
from routers import pm_router, dev_router, qa_router, ba_router

app = FastAPI()

# Include routers
app.include_router(pm_router.router)
app.include_router(dev_router.router)
app.include_router(qa_router.router)
app.include_router(ba_router.router)


@app.get("/")
async def root():
    return {"message": "Multi-Agent Workflow Application"}
