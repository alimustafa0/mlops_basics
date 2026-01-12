import numpy as np
from utils.alerting import send_alert
def log_prediction_stats(predictions):
    """Analyzes the model's output behavior."""
    # Convert to numpy array if it isn't one already
    preds = np.array(predictions)
    
    stats = {
        "mean": float(np.mean(preds)),
        "std": float(np.std(preds)),
        "positive_rate": float(np.mean(preds > 0.5))
    }

    print(f"--- Prediction Monitoring ---")
    print("PREDICTION_STATS:", stats)
    
    # Simple Threshold Alerting
    if stats["positive_rate"] > 0.90 or stats["positive_rate"] < 0.10:
        send_alert(
        level="CRITICAL",
        message="Prediction distribution unstable - model behavior highly biased",
        context=stats
    )
    else:
        print("✅ Prediction distribution looks healthy.")
        
    return stats