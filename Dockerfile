# 1. Base image (Python + Linux)
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy dependency contract
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy project files
COPY train.py config.yaml ./
COPY utils/ ./utils/

# 6. Default command
CMD ["python", "train.py"]
