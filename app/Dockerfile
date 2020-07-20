# Build Stage
FROM python:3.8.4-alpine3.11 as builder
RUN apk add --update python3-dev
COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install --upgrade pip; pip install --user -r requirements.txt
COPY . app/
COPY notes.py notes.py

# put-it-all-together Stage
FROM python:3.8.4-alpine3.11 as app
ENV FLASK_APP notes.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY --from=builder /root/.local /root/.local
COPY --from=builder /code/ /code/
WORKDIR /code
ENV PATH=/root/.local/bin:$PATH
CMD ["flask", "run"]