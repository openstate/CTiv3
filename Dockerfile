# Python runtime
FROM python:3.7.3-alpine

# Set working directory
WORKDIR /app

VOLUME ["/app"]

ADD requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Open port
EXPOSE 5000

# Execute command
CMD ["python", "/app/applicatie.py"]
