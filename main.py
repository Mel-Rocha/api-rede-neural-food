import os

from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from apps.docs import routes as docs_router
from apps.auth.middlewares import AuthMiddleware
from apps.docs.custom_openapi import custom_openapi
from apps.nutrition import routes as nutrition_router

load_dotenv()


def init_db(instance: FastAPI) -> None:
    register_tortoise(
        instance,
        db_url=os.getenv("DATABASE_URL"),
        modules={"models": ["apps.nutrition.models", "aerich.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )


def create_application() -> FastAPI:
    application = FastAPI()

    application.add_middleware(AuthMiddleware)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=[
            "DELETE",
            "GET",
            "OPTIONS",
            "PATCH",
            "POST",
            "PUT",
        ],
        allow_headers=["*"]
    )

    application.include_router(docs_router.router, tags=['nutrition'])
    application.include_router(nutrition_router.router, prefix="/nutrition", tags=['nutrition'])

    return application


app = create_application()

app.openapi = lambda: custom_openapi(app)


@app.on_event('startup')
async def startup_event():
    init_db(app)
