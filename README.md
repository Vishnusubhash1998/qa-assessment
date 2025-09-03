# QA Assessment (PyTest)

This project contains two functions to test:
- `is_password_strong(password)` in **passwords.py**
- `is_discount_valid(discount, cart_total, applied_codes, now)` in **discounts.py**

Tests live in **tests/** and are parameterized with `@pytest.mark.parametrize`.

## Quickstart (Windows + IntelliJ Idea)
1) Install **Python 3.11+**. During setup, check **"Add python.exe to PATH"**.
2) Open **IntelliJ IDEA** → **File → Settings → Plugins → Marketplace** → install **Python** plugin by JetBrains → restart.
3) **Get the project**: open this folder in IntelliJ (**File → Open**).
4) Create a **virtual environment** in terminal at project root:
   ```bat
   py -3.11 -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
5) Configure PyTest in IntelliJ:
   - **File → Settings → Tools → Python Integrated Tools**
   - Testing framework: **pytest**
   - Default test runner: **pytest**
6) Run tests:
   - Terminal: `pytest -q`
   - IntelliJ: Right-click the `tests` folder → **Run 'pytest in tests'**.
7) (Optional) Coverage in terminal: `pytest --cov=. --cov-report=term-missing`

## Mac/Linux commands (zsh/bash)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Git workflow (basic)
```bash
git init
git checkout -b feat/assessment-tests
git add .
git commit -m "Add parameterized tests for password and discount validation"
# connect to your GitHub remote, then push and open a PR
```
