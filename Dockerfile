FROM python:3.8-slim

WORKDIR /app

COPY main.py /app/main.py

RUN pip install --no-cache-dir argparse

CMD ["python3", "main.py", "--treatment"]
