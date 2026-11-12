PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -v
	$(PYTHON) change_risk.py sample_changes.csv

.PHONY: replay
replay:
	$(PYTHON) tools/replay_examples.py --report reports/replay.md
