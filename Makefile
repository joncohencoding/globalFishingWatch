# Define variables
PIPENV=pipenv
PYTHON=$(PIPENV) run python

# Default target
.PHONY: all
all: install run

# Install dependencies
.PHONY: install
install:
	$(PIPENV) install

# Run the application
.PHONY: run
run:
	@echo "Executing main..."
	$(PYTHON) src/main.py