import json
import os

def save_alerts(alerts, output_path="reports/alerts.json"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w') as file:
        json.dump(alerts, file, indent=4)
