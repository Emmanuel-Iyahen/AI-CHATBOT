# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy backend requirements and install
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend folder code
COPY ./ /app

# Expose the port your FastAPI app runs on (default 8000)
EXPOSE 8000

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
