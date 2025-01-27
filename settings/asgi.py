import os
from django.core.asgi import get_asgi_application
from interface.socket import app as fastapi_app  # Import FastAPI app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")

django_application = get_asgi_application()


class CombinedApplication:
    def __init__(self, django_app, fastapi_app):
        self.django_app = django_app
        self.fastapi_app = fastapi_app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http" and scope["path"].startswith("/api"):
            await self.fastapi_app(scope, receive, send)
        else:
            await self.django_app(scope, receive, send)

application = CombinedApplication(django_application, fastapi_app)
