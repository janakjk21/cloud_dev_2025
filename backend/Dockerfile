# backend/Dockerfile

# 1. Base image
FROM python:3.10-slim

# 2. Set a working directory
WORKDIR /app

# 3. Copy & install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of your application code
COPY . .

# 5. Expose the port your app runs on
EXPOSE 8000

# 6. Launch Uvicorn on 0.0.0.0:8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
