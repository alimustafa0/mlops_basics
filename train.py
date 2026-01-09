import os
import yaml

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    config["environment"] = os.getenv("ENVIRONMENT", config["environment"])
    return config

def validate_config(config):
    print("Validating config...")
    assert "training" in config
    assert "paths" in config

def prepare_data(config):
    print("Preparing data...")

def train_model(config):
    print("Training model...")

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
