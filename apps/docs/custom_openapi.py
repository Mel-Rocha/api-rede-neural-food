from fastapi.openapi.utils import get_openapi


def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="API - food rede neural",
        version="1.0.0",
        description="Esta é a documentação da de integração com o projeto django rede neural",
        routes=app.routes,
    )

    # Defina o esquema de segurança para exigir autenticação Bearer Token em todas as rotas
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "API_KEY"  # Pode ser alterado conforme necessário
        }
    }

    # Defina os requisitos de segurança para exigir autenticação Bearer Token em todas as rotas
    openapi_schema["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema
