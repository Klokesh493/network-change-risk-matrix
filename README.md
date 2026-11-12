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

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Business problem

A network change that touches multiple regions or lacks tested rollback needs more scrutiny than a small, reversible change.

## Project walkthrough

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

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 change_risk.py sample_changes.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.

## Development and security

See the [developer setup, tool roles, and security checks](docs/DEVELOPMENT.md).

[Local check results](reports/devsecops.md)
