from fastapi import FastAPI
import uvicorn
import logging
from potato.conf import settings
from potato.routes import router
from fastapi.middleware.cors import CORSMiddleware


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    root_path="/api",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


def dev():
    try:
        logger.info("Starting development server...")
        uvicorn.run(
            "potato.main:app",
            host=settings.host,
            port=settings.port,
            log_level="info",
        )
    except Exception as e:
        logger.error(f"Error starting server: {e}")
        