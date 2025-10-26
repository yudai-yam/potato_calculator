from fastapi import APIRouter
from starlette import status
from fastapi.responses import JSONResponse
from potato.calculator import calculate_price

router = APIRouter()


@router.get("/calculate", status_code=status.HTTP_200_OK)
async def calculate(
    grams: float,
):
    """
    calculate the price of potatoes based on user input

    Parameters:
        input: user input
    """
    result = calculate_price(grams)
    return {"price": result}
