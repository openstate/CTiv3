# Python runtime
FROM python:3.7.3-alpine

# Set working directory
WORKDIR /home

# Copy source
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Open port
EXPOSE 5000

# Execute command
CMD ["python", "applicatie.py"]
