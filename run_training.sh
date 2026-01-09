#!/bin/bash
set -e

echo "--- MLOps Pipeline Initialized ---"
echo "Step 1: Running the training script..."
python3 train.py
echo "Step 2: Training complete. Logging results..." 
echo "--- Pipeline Finished Successfully ---"