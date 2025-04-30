FROM python:3.8-slim AS challenge

RUN mkdir /challenge && chmod 700 /challenge

WORKDIR /app
COPY main.py flag.txt ./
COPY start.sh /opt/
RUN chmod +x /opt/start.sh

RUN pip install --no-cache-dir argparse

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    socat \
    && rm -rf /var/lib/apt/lists/*

RUN echo "{\"flag\":\"$(cat flag.txt)\"}" > /challenge/metadata.json

# Copy start.sh to /opt/
COPY start.sh /opt/
RUN chmod +x /opt/start.sh

# The start.sh script starts a socat listener on port 5555, that connects to the
# python script.
EXPOSE 5555
# PUBLISH 5555 AS socat
CMD ["/opt/start.sh"]

