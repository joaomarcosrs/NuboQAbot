FROM python:3.12-slim

RUN apt-get update && apt-get install -y build-essential curl\
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh

WORKDIR /app

COPY . .

RUN pip install poetry


RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

EXPOSE 11434


CMD ["poetry", "run", "python", "-m", "nuboqabot.main"]