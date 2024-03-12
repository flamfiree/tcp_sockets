# Имя цели по умолчанию
.DEFAULT_GOAL := run

# Переменные
ifeq ($(OS),Windows_NT)
PYTHON := python
else
PYTHON := python3
endif

SCRIPT := src/main.py

# setup: requirements.txt
# 	pip install -r requirements.txt

# Цель для запуска скрипта
run:
	$(PYTHON) $(SCRIPT)

clean:
	rm -rf src/__pycache__