FROM python:3.9 as builder

COPY requirements.txt .
RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copying only required files to run the application
WORKDIR /opt/recipebook/
COPY requirements.txt \
    .flaskenv \
    config.py \
    recipebook.py \
    ./
COPY app/ ./app
COPY migrations/ ./migrations

FROM python:3.9-slim-buster

WORKDIR /opt/recipebook

COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /opt/recipebook /opt/recipebook

ENV PATH="/opt/venv/bin:$PATH"

CMD ["flask", "run"]
