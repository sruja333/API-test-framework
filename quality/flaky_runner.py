import subprocess
import json
from collections import defaultdict

RUNS = 3
FLAKY_THRESHOLD = 0  # number of flaky tests allowed

results = defaultdict(list)

for i in range(RUNS):
    print(f"Running test iteration {i + 1}")
    completed = subprocess.run(
        ["pytest", "-q"],
        capture_output=True,
        text=True
    )

    output = completed.stdout.splitlines()

    for line in output:
        if line.startswith("FAILED") or line.startswith("PASSED"):
            test_name = line.split(" ")[1]
            status = line.split(" ")[0]
            results[test_name].append(status)

report = {}
flaky_count = 0

for test, statuses in results.items():
    unique = set(statuses)
    is_flaky = len(unique) > 1
    report[test] = {
        "runs": statuses,
        "flaky": is_flaky
    }
    if is_flaky:
        flaky_count += 1

with open("quality/report.json", "w") as f:
    json.dump(report, f, indent=2)

print("Flaky tests:", flaky_count)

if flaky_count > FLAKY_THRESHOLD:
    print("Quality gate failed due to flaky tests")
    exit(1)

print("Quality gate passed")
