import argparse
from parser import parse_log
from detector import detect_bruteforce
from alerts import save_alerts

def main():
    parser = argparse.ArgumentParser(description="Security Log Analyzer")
    parser.add_argument("--log", required=True, help="Path to log file")
    parser.add_argument("--threshold", type=int, default=5, help="Brute force threshold")

    args = parser.parse_args()

    events = parse_log(args.log)
    alerts = detect_bruteforce(events, args.threshold)

    if alerts:
        print("\n🚨 Alerts Detected:")
        for alert in alerts:
            print(f"[{alert['type']}] IP: {alert['ip']} | Attempts: {alert['attempts']}")
        save_alerts(alerts)
        print("\nAlerts saved to reports/alerts.json")
    else:
        print("No suspicious activity detected.")

if __name__ == "__main__":
    main()
