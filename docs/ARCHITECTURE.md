# Network Change Risk Matrix architecture

Scores network changes by device count, region count, rollback maturity, and customer tier.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
