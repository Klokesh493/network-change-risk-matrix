# Network Change Risk Matrix walkthrough

## Business problem

Scores network changes by device count, region count, rollback maturity, and customer tier.

## Reproduce the workflow

Run `python3 change_risk.py sample_changes.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
chg-100 medium
chg-200 high
```

The sample supplies these fields. `change_id`, `devices`, `regions`, `rollback_tested`, `customer_tier`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
