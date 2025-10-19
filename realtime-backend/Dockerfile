# backend/Dockerfile

# Step 1: Use an official lightweight Python image
FROM python:3.11-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Install system dependencies (for psycopg2 etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Copy dependency file
COPY requirements.txt .

# Step 5: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the FastAPI source code
COPY ./ ./app

# Step 7: Expose port for FastAPI
EXPOSE 8000

# Step 8: Start FastAPI using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
