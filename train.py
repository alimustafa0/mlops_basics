import os
import yaml
from pathlib import Path
import shutil
import pandas as pd
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils.data_monitor import log_data_stats

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    config["environment"] = os.getenv("ENVIRONMENT", config["environment"])
    return config

def validate_config(config):
    print("Validating config...")
    required_keys = ["training", "paths", "environment"]
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required config key: {key}")

def prepare_data(config):
    print("Preparing data...")
    # Mocking data for this step - in reality, you'd load your CSV/SQL here
    data = pd.DataFrame({
        'feature_1': [10, 20, 30, 40],
        'feature_2': [0.1, 0.2, 0.5, 0.1]
    })
    
    # Call the monitor
    log_data_stats(data)
    data_path = Path(config["paths"]["data_dir"])
    data_path.mkdir(exist_ok=True)

    prepared_file = data_path / "prepared.flag"
    if prepared_file.exists():
        print("Data already prepared — skipping")
        return

    # Simulate preparation
    prepared_file.touch()
    print("Data preparation completed")

def train_model(config):
    print("Training model...")
    model_dir = Path(config["paths"]["model_dir"])
    model_dir.mkdir(exist_ok=True)

    model_file = model_dir / "model.bin"
    if model_file.exists():
        print("Model already trained — skipping")
        return

    # Simulate training
    model_file.write_text("trained-model")
    print("Model training completed")

def evaluate_model(config):
    print("Evaluating model...")

def save_artifacts(config):
    print("Saving model artifacts...")
    
    # Define our source (where the model was trained) 
    # and destination (the 'vault' for our artifacts)
    model_src = Path(config["paths"]["model_dir"]) / "model.bin"
    artifact_dir = Path("artifacts")
    artifact_dest = artifact_dir / "model_final.bin"

    # 1. Create the artifact directory if it doesn't exist
    artifact_dir.mkdir(exist_ok=True)

    # 2. Idempotency Guard: If the final artifact already exists, don't move it again
    if artifact_dest.exists():
        print(f"Artifact {artifact_dest.name} already exists in the vault — skipping.")
        return

    # 3. Safety Check: Ensure the source model actually exists before trying to save it
    if not model_src.exists():
        raise FileNotFoundError(f"Missing source model at {model_src}. Did training fail?")

    # 4. Atomic 'Save': Copy the model to the artifact vault
    shutil.copy(model_src, artifact_dest)
    
    # 5. Metadata logging (Standard MLOps practice)
    print(f"✅ Successfully saved model to {artifact_dest}")
    with open(artifact_dir / "metadata.txt", "w") as f:
        f.write(f"Environment: {config['environment']}\n")
        f.write(f"Model Version: 1.0.0\n")

def detect_drift(current_stats, baseline_stats, threshold=0.2):
    drift_alerts = {}

    for feature, base_mean in baseline_stats["mean"].items():
        current_mean = current_stats["mean"].get(feature)
        if current_mean is None:
            continue

        change = abs(current_mean - base_mean) / base_mean
        if change > threshold:
            drift_alerts[feature] = change

    if drift_alerts:
        print("⚠️ DRIFT DETECTED:", drift_alerts)
    else:
        print("✅ No significant drift detected")

    return drift_alerts

def main():
    print("Pipeline started")
    config = load_config()
    validate_config(config)
    prepare_data(config)
    detect_drift(
        current_stats={"mean": {"feature_1": 35, "feature_2": 0.15}},
        baseline_stats={"mean": {"feature_1": 25, "feature_2": 0.2}},
        threshold=0.2
    )
    train_model(config)
    evaluate_model(config)
    save_artifacts(config)
    print("Pipeline completed successfully")

if __name__ == "__main__":
    main()
