FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -qqy gcc && \
    rm -rf /var/lib/apt/lists

RUN useradd --create-home \
    --home-dir /home/recipebook \
    -c "The recipe book app user" \
    recipebook && \
    mkdir /opt/recipebook && \
    chown recipebook:recipebook -R /opt/recipebook

USER recipebook
WORKDIR /opt/recipebook/

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
ENV PATH=/home/recipebook/.local/bin:$PATH

COPY .flaskenv \
    config.py \
    recipebook.py \
    ./
COPY app/ ./app
COPY migrations/ ./migrations

EXPOSE 5001

CMD ["flask", "run"]
