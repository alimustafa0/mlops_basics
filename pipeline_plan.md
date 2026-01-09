Task: validate_config
Inputs: config.yaml
Outputs: Validated Dictionary
Failure Behavior: Raise ValueError & Stop
Retry-safe: Yes

Task: prepare_data
Inputs: raw data path
Outputs: prepared.flag
Failure Behavior: Stop & Alert
Retry-safe: Yes (via flag check)

Task: train_model
Inputs: prepared.flag
Outputs: model.bin
Failure Behavior: Fail Loudly
Retry-safe: Yes (via model check)

Task: evaluate_model
Inputs: model.bin
Outputs: Metrics/Logs
Failure Behavior: Log Error
Retry-safe: Yes

Task: save_artifacts
Inputs: model.bin
Outputs: artifacts/model_final.bin
Failure Behavior: Raise FileNotFound
Retry-safe: Yes (via dest check)