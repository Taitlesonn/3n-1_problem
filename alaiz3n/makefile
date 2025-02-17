VENV_DIR=3n_projekt

# Wykrywanie systemu: dla Windows zmienna OS ma wartość Windows_NT
ifeq ($(OS),Windows_NT)
    PYTHON=$(VENV_DIR)\Scripts\python.exe
else
    PYTHON=$(VENV_DIR)/bin/python
endif

# Nazwa Twojego pliku .py (umieszczonego w tym samym folderze)
SCRIPT=analiza.py

run:
	$(PYTHON) $(SCRIPT)
