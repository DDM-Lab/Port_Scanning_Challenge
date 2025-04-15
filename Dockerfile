FROM python:3.8-slim AS challenge

RUN mkdir /challenge && chmod 700 /challenge

WORKDIR /app

COPY main.py /app/main.py

RUN pip install --no-cache-dir argparse

RUN apt-get update && apt-get install -y --no-install-recommends socat && rm -rf /var/lib/apt/lists/*

# Copy start.sh to /opt/
COPY start.sh /opt/
RUN chmod +x /opt/start.sh

# Expose the port socat will listen on
EXPOSE 5555

# Start the service using start.sh
CMD ["/opt/start.sh"]

