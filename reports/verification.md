# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 change_risk.py sample_changes.csv
chg-100 medium
chg-200 high
test_classifies_large_unproven_change_high (test_change_risk.ChangeRiskTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
