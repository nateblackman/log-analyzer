from collections import defaultdict

def detect_bruteforce(events, threshold=5):
    attempts = defaultdict(list)
    alerts = []

    for event in events:
        if event["status"] == "failed":
            attempts[event["ip"]].append(event)
        
    for ip, failures in attempts.items():
        if len(failures) >= threshold:
            alerts.append({
                "type": "Brute force",
                "ip": ip,
                "attempts": len(failures)
                "target_users": list(set(f["username"] for f in failures))
            })
    return alerts
