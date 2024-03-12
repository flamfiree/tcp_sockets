# Имя цели по умолчанию
.DEFAULT_GOAL := run

# Переменные
ifeq ($(OS),Windows_NT)
PYTHON := python
else
PYTHON := python3
endif

SCRIPT := src/main.py

run:
	$(PYTHON) $(SCRIPT)

clean:
	rm -rf src/__pycache__