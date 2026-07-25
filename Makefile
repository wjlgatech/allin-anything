.PHONY: check test drift audit build

check: test drift audit
	@echo "✓ make check green"

test:
	python3 -m pytest -q

drift:
	python3 scripts/build.py --check

audit:
	python3 scripts/ainative.py --gate 90

build:
	python3 scripts/build.py
