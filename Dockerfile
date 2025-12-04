# Base image with Python and GCC
FROM python:3.10-slim

# Install necessary tools
RUN apt-get update && apt-get install -y g++ curl

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install fastapi uvicorn

# Compile the C++ program
RUN g++ wisp2.cpp -o wisp_interpreter

# Expose required ports
EXPOSE 5001

# Start the FastAPI server
CMD ["sh", "-c", "./wisp_interpreter && uvicorn server:app --host 0.0.0.0 --port 5001"]

