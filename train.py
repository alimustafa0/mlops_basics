import os
import yaml
from pathlib import Path

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

def main():
    print("Pipeline started")
    config = load_config()
    validate_config(config)
    prepare_data(config)
    train_model(config)
    evaluate_model(config)
    save_artifacts(config)
    print("Pipeline completed successfully")

if __name__ == "__main__":
    main()
