import re

LOG_PATTERN = re.compile(
    r"Failed password for (\w+) from ([\d\.]+) | Accepted password for (\w+) from ([\d\.]+)"
)

def parse_log(file_path):
    events = []

    with open(file_path, 'r') as file:
        for line in file:
            match = LOG_PATTERN.search(line)
            if match:
                if match.group(1):
                    events.append({
                        "username": match.group(1),
                        "ip": match.group(2),
                        "status": "failed"
                    })
                else:
                    events.append({
                        "username": match.group(3),
                        "ip": match.group(4),
                        "status": "successful"
                    })
    return events
