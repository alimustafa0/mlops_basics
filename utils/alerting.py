def send_alert(level, message, context=None):
    """Centralized alerting function for the ML system."""
    
    # In a real company, this would trigger PagerDuty or Slack
    print("\n" + "="*30)
    print(f"🚨 ALERT [{level.upper()}]: {message}")
    if context:
        print(f"📋 Context Details: {context}")
    print("="*30 + "\n")

    # Example of a 'Playbook' action
    if level == "CRITICAL":
        print("🛑 SYSTEM ACTION: Flagging pipeline for manual review. Deployment blocked.")