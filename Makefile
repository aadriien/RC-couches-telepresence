# RC Couches Telepresence Zulip Bot

POETRY ?= poetry
VENV_DIR = .venv
PYTHON_VERSION = python3

.PHONY: setup run-launch run-close run-server clean 

all: setup run-server 

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
	@$(POETRY) run python zulip-bot/bot.py --launch

# Run bot client (close) script as one-off instance
run-close:
	@$(POETRY) run python zulip-bot/bot.py --close

# Run bot server 24/7 to listen & respond 
run-server:
	@$(POETRY) run python zulip-bot/bot.py --server

clean:
	@echo "Removing virtual environment..."
	@rm -rf .venv

