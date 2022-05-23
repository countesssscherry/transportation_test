from fastapi import FastAPI

from .transport.router import router as sync_router

app = FastAPI()
# this is a section with endpoints for managing transportations
app.include_router(sync_router)
# here can also be added section for working with packages, drivers etc


@app.get("/")
def read_root() -> dict:
    """
    healthcheck
    """
    return {"alive": True}
