import os
import yaml

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        config = yaml.safe_load(f)

    # Override environment from ENV VAR if present
    config["environment"] = os.getenv("ENVIRONMENT", config["environment"])
    return config

def main():
    config = load_config()
    print("Environment:", config["environment"])
    print("Training epochs:", config["training"]["epochs"])
    print("Model directory:", config["paths"]["model_dir"])
    print("Training started...")
    print("Training finished successfully.")

if __name__ == "__main__":
    main()
