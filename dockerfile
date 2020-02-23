FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt && rm -Rf /root/.cache && rm -Rf /tmp/pip-install*
COPY ./app /app
