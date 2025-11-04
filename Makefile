# RC Couches Telepresence Zulip Bot

POETRY ?= poetry
VENV_DIR = .venv
PYTHON_VERSION = python3

ACTIVATE_VENV = source $(VENV_DIR)/bin/activate &&

.PHONY: setup run-launch run-close run-service clean format

all: setup run-service 

# Install Poetry dependencies & set up venv
setup:
	@which poetry > /dev/null || (echo "Poetry not found. Installing..."; curl -sSL https://install.python-poetry.org | $(PYTHON_VERSION) -)
	@$(POETRY) config virtualenvs.in-project true  # Ensure virtualenv is inside project folder
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Creating..."; \
		$(POETRY) env use $(PYTHON_VERSION); \
		$(POETRY) install --no-root --quiet; \
	fi

# Run bot client (launch) script as one-off instance
run-launch:
	@$(ACTIVATE_VENV) $(POETRY) run python zulip-bot/bot.py --launch

# Run bot client (close) script as one-off instance
run-close:
	@$(ACTIVATE_VENV) $(POETRY) run python zulip-bot/bot.py --close

# Run bot service 24/7 to listen & respond 
run-service:
	@$(ACTIVATE_VENV) $(POETRY) run python zulip-bot/bot.py --service

clean:
	@echo "Removing virtual environment..."
	@rm -rf .venv

format:
	@echo "Formatting repo..."
	@pre-commit run --all-files
	
