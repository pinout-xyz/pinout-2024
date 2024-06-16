.PHONY: usage check pytest qa build-deps check
usage:
	@echo "Usage: make <target>, where target is one of:\n"
	@echo "dev-deps:     install Python dev dependencies"
	@echo "check:        perform basic integrity checks on the codebase"
	@echo "shellcheck:   perform check on shell scripts"
	@echo "qa:           run linting and package QA"
	@echo "pytest:       run Python test fixtures"

dev-deps:
	python3 -m pip install -r requirements-dev.txt
	sudo apt install dos2unix shellcheck

check:
	@bash check.sh

shellcheck:
	shellcheck *.sh

qa:
	tox -e qa

pytest:
	tox -e py
