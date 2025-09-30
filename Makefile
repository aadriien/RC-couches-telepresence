# RC Couches Telepresence Zulip Bot

POETRY ?= poetry
VENV_DIR = .venv
PYTHON_VERSION = python3

.PHONY: setup run clean 

all: setup run 

# Install Poetry dependencies & set up venv
setup:
	@which poetry > /dev/null || (echo "Poetry not found. Installing..."; curl -sSL https://install.python-poetry.org | $(PYTHON_VERSION) -)
	@$(POETRY) config virtualenvs.in-project true  # Ensure virtualenv is inside project folder
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Creating..."; \
		$(POETRY) env use $(PYTHON_VERSION); \
		$(POETRY) install --no-root --quiet; \
	fi

run: 
	@$(POETRY) run python zulip-bot/bot.py

clean:
	@echo "Removing virtual environment..."
	@rm -rf .venv

