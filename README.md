# Network Change Risk Matrix

Scores network changes by device count, region count, rollback maturity, and customer tier.

Focus: Telecom DevOps change management.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 change_risk.py sample_changes.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```
