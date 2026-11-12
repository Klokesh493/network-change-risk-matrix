# Network Change Risk Matrix architecture

Scores network changes by device count, region count, rollback maturity, and customer tier.

```mermaid
flowchart LR
    N0["sample_changes.csv"]
    N1["change_risk.py"]
    N2["score / classify"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
