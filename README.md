Professional Calculator Command-Line Application
Overview
This project is a modular command-line calculator developed in Python using object-oriented programming principles.
It supports arithmetic operations, maintains calculation history, includes full unit testing, and uses GitHub Actions to enforce 100% test coverage.
The goal of this assignment is to demonstrate:
Clean project architecture
Error handling strategies (LBYL & EAFP)
Automated testing with pytest
Continuous integration with GitHub Actions
Features
Calculator Functionality
Addition, subtraction, multiplication, and division
Division-by-zero error handling
Input validation for numeric values
REPL Interface
Continuous Read-Eval-Print Loop
Built-in commands:
help → shows usage instructions
history → displays previous calculations
exit → quits the program
Software Engineering Practices
Modular folder structure
DRY principle and reusable classes
Calculation data model with computation logic
CalculationFactory for creating calculation objects
Testing & Coverage
Unit tests written using pytest
Parameterized tests for multiple input cases
Edge cases tested:
Invalid numbers
Unsupported operations
Division by zero
100% test coverage achieved using pytest-cov
Continuous Integration (CI)
GitHub Actions automatically:
Installs dependencies
Runs all tests
Checks coverage ≥ 100%
Fails the build if coverage drops
This ensures code quality on every push.
Project Structure
app/
 ├── calculation/
 │    ├── calculation.py
 │    └── factory.py
 ├── calculator/
 │    └── repl.py
 ├── operation/
 │    └── operations.py
 └── main.py

tests/
 ├── test_calculations.py
 ├── test_operations.py
 ├── test_repl.py
 └── test_main.py
Setup Instructions
1. Clone the repository
git clone https://github.com/kavyareddypodduturi/module4-calculator.git
cd module4-calculator
2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install pytest pytest-cov
Running the Calculator
python -m app.main
Example usage:
> add 2 3
5.0

> history
add 2.0 3.0 = 5.0
Running Tests
pytest
Coverage must show:
TOTAL coverage: 100%
Learning Outcomes
This project demonstrates:
Object-oriented programming in Python
Clean modular design
Robust error handling
Automated testing and CI pipelines
> Technologies Used

Python, pytest, pytest-cov, Git, GitHub, GitHub Actions

License

This project is developed for academic purposes as part of coursework
