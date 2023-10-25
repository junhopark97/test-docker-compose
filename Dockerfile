FROM python:3.11.6

# linux update
RUN apt update

# poetry install
#RUN curl -sSL https://install.python-poetry.org | python3 -
#ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# https://fastapi.tiangolo.com/deployment/docker/
