FROM python:3.11-slim

# Work in /app
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

#copy source code
COPY . .

WORKDIR /app/src

# Run app
CMD ["python", "main.py"]
