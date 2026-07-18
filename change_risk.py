import csv
import sys


def score(row):
    value = int(row["devices"]) + int(row["regions"]) * 3
    if row["rollback_tested"].lower() != "yes":
        value += 8
    if row["customer_tier"].lower() == "enterprise":
        value += 5
    return value


def classify(row):
    value = score(row)
    return "high" if value >= 20 else "medium" if value >= 10 else "low"


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            print(f"{row['change_id']} {classify(row)}")


if __name__ == "__main__":
    main(sys.argv[1])
