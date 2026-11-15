# Network Change Risk Matrix

A network change that touches multiple regions or lacks tested rollback needs more scrutiny than a small, reversible change.

[Skills and verification](docs/ENGINEERING_NOTES.md)

## What I built

I built a change-risk classifier that scores device count, regional scope, missing rollback tests, and enterprise-customer exposure. Scores map to low, medium, or high risk.

## How it works

```mermaid
flowchart LR
    A["Network change CSV"]
    B["Score devices, regions, rollback test, and customer tier"]
    C["Compare score to 10 and 20"]
    D["Medium or high risk"]
    E["Low risk below 10"]
    A --> B --> C
    C --> D
    C --> E
```

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [change_risk.py](change_risk.py) implements the CLI and decision rules. Uses `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 change_risk.py sample_changes.csv
```

The fixture classifies chg-100 as medium and chg-200 as high. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 change_risk.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

The score supports a change review. Inspect dependencies and verify rollback evidence independently.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
