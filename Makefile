.PHONY: check test drift audit build demo

check: test drift audit
	@echo "✓ make check green"

demo:
	python3 scripts/webapp.py

test:
	python3 -m pytest -q

drift:
	python3 scripts/build.py --check

audit:
	python3 scripts/ainative.py --gate 90

build:
	python3 scripts/build.py
