FROM python:3.11-slim

# Work in /app
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

WORKDIR /app/src

# Run your app
CMD ["python", "main.py"]
