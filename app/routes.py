from fastapi import APIRouter, HTTPException

router = APIRouter()

users = []
@router.get("/health")
def health_check():
    return {"status": "ok"}
@router.post("/users")
def create_user(user: dict):
    if "name" not in user:
        raise HTTPException(status_code=400, detail="Name required")
    
    user["id"] = len(users) + 1
    users.append(user)
    return user
@router.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
