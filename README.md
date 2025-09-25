# Professional Calculator (Command-Line Application)

This is a modular, professional-grade command-line calculator application built with Python.  
It supports addition, subtraction, multiplication, and division with a REPL (Read-Eval-Print Loop) interface.  

The project emphasizes:
- Clean code structure
- Object-oriented design
- Error handling using EAFP and LBYL
- 100% test coverage
- Continuous integration using GitHub Actions

---

## How to Set Up and Run

### 1. Clone the Repository

```bash
git clone https://github.com/Mikev2002/professional-calculator.git
cd professional-calculator


2. Create and Activate Virtual Environment

# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Or (macOS/Linux)
source venv/bin/activate


3. Install Dependencies

pip install -r requirements.txt


4. Run the Application

python main.py


Available Commands (Inside the App)

When you run the app, it will enter interactive mode (REPL):
Available commands:
  add, subtract, multiply, divide
  history  - show all previous calculations
  help     - show this message
  exit     - quit the calculator


5. Running Tests

All logic is tested using pytest with 100% test coverage.
To run tests:
pytest --cov=app tests/

To see a detailed coverage report:
coverage report

