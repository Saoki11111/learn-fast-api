from fastapi import APIRouter

router = APIRouter()


@router.put("/tasks/{task_id}")
async def update_task_as_done():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task_as_done():
    pass
