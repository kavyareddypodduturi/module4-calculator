
# **Professional Calculator Application**

A command-line calculator application built in Python, demonstrating object-oriented design, unit testing with pytest, and continuous integration with GitHub Actions.

This project supports arithmetic operations, handles invalid input, maintains calculation history, and enforces 100% test coverage.

---

## 🚀 Features

✔ Add, Subtract, Multiply, Divide
✔ Handles division-by-zero errors
✔ REPL (interactive console)
✔ History of performed calculations
✔ Full unit tests with pytest
✔ Continuous integration using GitHub Actions
✔ 100% test coverage enforced

---

## 🛠️ Technologies Used

| Technology     | Purpose                |
| -------------- | ---------------------- |
| Python         | Programming language   |
| pytest         | Testing framework      |
| pytest-cov     | Coverage reporting     |
| GitHub Actions | Continuous integration |
| dataclasses    | Structured data model  |

---

## 📁 Project Structure

```
module4-calculator/
├── app/
│   ├── calculation/
│   │   ├── calculation.py
│   │   └── factory.py
│   ├── calculator/
│   │   └── repl.py
│   ├── operation/
│   │   └── operations.py
│   └── main.py
├── tests/
│   ├── test_calculations.py
│   ├── test_operations.py
│   ├── test_repl.py
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── python-app.yml
├── .venv/
├── pyproject.toml
└── README.md
```

---

## 📥 Installation

1. Clone the repository:

```bash
git clone https://github.com/kavyareddypodduturi/module4-calculator.git
cd module4-calculator
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install pytest pytest-cov
```

---

## ▶️ Running the Application

Run the calculator in REPL mode:

```bash
python -m app.main
```

Example commands inside the REPL:

```
> add 10 5
15.0

> multiply 2 3
6.0

> history
add 10.0 5.0 = 15.0
multiply 2.0 3.0 = 6.0

> exit
Goodbye!
```

---

## 🔍 Testing

Run all tests:

```bash
pytest
```

Combined with coverage:

```bash
pytest --cov=app --cov-branch
```

Expected coverage report:

```
TOTAL coverage: 100%
```

---

## 📦 GitHub Actions (CI)

This project uses a GitHub Actions workflow (`.github/workflows/python-app.yml`) to:

✔ Install dependencies
✔ Run tests
✔ Check coverage
✔ Fail the build if coverage < 100%

---

## 💡 Usage Examples

From the REPL:

```
help
history
add 2 3
divide 10 2
multiply 5 6
```

---

## 🧠 Notes

* Error handling is implemented using both LBYL (Look Before You Leap) and EAFP (Easier to Ask Forgiveness than Permission).
* The `CalculationFactory` implements a factory pattern to construct calculation objects.
* History of calculations is stored in memory during REPL session.

---


## 📄 License

This project is for educational purposes and does not include a specific license.

