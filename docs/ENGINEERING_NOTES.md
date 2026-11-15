# Skills and verification

## What this repository demonstrates

A change-risk classifier that scores device count, regional scope, missing rollback tests, and enterprise-customer exposure. Scores map to low, medium, or high risk.

## Reproduce the result

The fixture classifies chg-100 as medium and chg-200 as high. Reproduce the primary fixture with `python3 change_risk.py sample_changes.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The score supports a change review. Inspect dependencies and verify rollback evidence independently.

For higher scores, verify the rollback rehearsal and change scope before seeking approval.

[change_risk.py](../change_risk.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
