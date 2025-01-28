release: bash scripts/setup_alsa.sh
web: gunicorn settings.asgi:application --worker-class uvicorn.workers.UvicornWorker