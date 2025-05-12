from fastapi import APIRouter

router: APIRouter = APIRouter()


@router.post("/")
async def add_user():
    pass
