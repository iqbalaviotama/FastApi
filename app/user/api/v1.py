from fastapi import APIRouter


from app.user.api.getUser import getUser

router = APIRouter(
    prefix="/user/v1",
    tags=["User"]
)


@router.get("/getUser")
async def get_user(i_id: str):
    return getUser(i_id)
