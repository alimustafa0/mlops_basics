import yaml

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()

    print("Environment:", config["environment"])
    print("Training epochs:", config["training"]["epochs"])
    print("Model directory:", config["paths"]["model_dir"])

if __name__ == "__main__":
    main()
