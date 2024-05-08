from argparse import ArgumentParser

import uvicorn
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html, get_swagger_ui_oauth2_redirect_html
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--env', type=str, default='dev', help='load one of these [dev,stage,prod] .envs')
    args = parser.parse_args()
    print(args.env)
    from core.service_app.configs.Settings import load_settings

    load_settings(args.env)
    from core.service_app import app
    from core.service_app.configs.Settings import settings

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.mount("/.static", StaticFiles(directory=".static"), name="static")
    swagger_js_url = "/.static/swagger/swagger-ui-bundle.js"
    swagger_css_url = "/.static/swagger/swagger-ui.css"


    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url=swagger_js_url,
            swagger_css_url=swagger_css_url,
        )


    @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()


    @app.get("/redoc", include_in_schema=False)
    async def redoc_html():
        return get_redoc_html(
            openapi_url=app.openapi_url,
            title=app.title + " - ReDoc",
            redoc_js_url="/static/redoc.standalone.js",
        )


    print(settings.PORT)

    uvicorn.run(app, host="0.0.0.0", port=3000, reload=False, workers=1)
