def log_data_stats(data):
    stats = {
        "rows": len(data),
        "null_rate": data.isnull().mean().to_dict(),
        "mean": data.mean(numeric_only=True).to_dict(),
        "std": data.std(numeric_only=True).to_dict()
    }
    print("DATA_STATS:", stats)
    return stats
