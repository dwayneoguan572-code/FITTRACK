# 🏃 FitTracker — Personal Fitness Report Generator

## Application Description

FitTracker is a standalone Python terminal application designed to help users monitor their physical fitness by tracking workouts, calculating health metrics, and generating a personal fitness report.

The application allows users to:
- Enter personal profile information including name, weight, and height.
- Log multiple exercises per session, including duration and calories burned per minute.
- Automatically calculate BMI and classify it as Underweight, Normal, Overweight, or Obese.
- Track total calories burned across all exercises and compare them against a personal daily goal.
- View a complete fitness report displayed on screen or exported to a `.txt` file.

Built for the terminal, the application emphasizes simplicity and accessibility. It operates entirely offline and follows a structured **Input → Process → Output** model, ensuring reliable performance without relying on external databases or internet connectivity.

Through this application, users can monitor their fitness progress, stay accountable to their calorie goals, and keep a record of their workout sessions in a single, easy-to-use platform.

---

## OOP Concepts Used

This project demonstrates core Object-Oriented Programming principles:

- **Encapsulation:** Private attributes using `_variable` (e.g., `_calorie_goal`, `_filename`)
- **Abstraction:** `InputReader` and `OutputWriter` abstract classes define standard methods without revealing internal implementation
- **Polymorphism:** `ScreenOutput` and `FileOutput` both implement the same `write()` method from `OutputWriter` but behave differently
- **Modularity:** Code is separated into models, I/O handlers, and entry point files

---

## Technologies Used

- Python (core programming language)
- Terminal / Command-line interface
- File handling for saving and retrieving fitness reports
- `abc` module for abstract base classes

---

## Project Structure

```
FitTracker/
│
├── models.py              # Fitness logic — BMI, calorie, and goal calculations
├── io_handlers.py         # Input readers and output writers
├── main.py                # Entry point — starts the app and connects all parts
├── fitness_ui.py          # Styled terminal UI with visual progress bars
│
└── fitness_report.txt     # Generated after export (optional)
```

---

## How to Run

**Requirements:**
- Python 3.7 or higher
- No external libraries needed — uses only the Python standard library

**Clone this repository:**
```bash
git clone https://github.com/placeholder/fittracker.git
```

**Navigate to the project folder:**
```bash
cd fittracker
```

**Run the application:**
```bash
python main.py
```

**Or run the styled terminal UI:**
```bash
python fitness_ui.py
```

---

## Running Tests

Unit tests are included inside `models.py`. Run them directly with:

```bash
python models.py
```

Or run using pytest:
```bash
py -m pytest -v
```

Expected output:
```
test_bmi_calculation PASSED
test_calorie_total PASSED
test_goal_status PASSED

All tests passed.
```

---

## Export Report

To save the fitness report to a file, open `main.py` and swap the writer:

```python
# Change this:
writer = ScreenOutput()

# To this:
writer = FileOutput("fitness_report.txt")
```

Output file will be saved as:
```
fitness_report.txt
```

---

## Authors

Developed as a school project by:

- Dwayne Anthony J. Oguan ([GitHub Profile of Oguan](https://github.com/dwayneoguan572-code))
- Lian Joseph A. Gamba ([GitHub Profile of Gamba](https://github.com/liangamba-design))
- Gerard Hermo ([GitHub Profile of Hermo](https://github.com/gxrard))

In Partial Fulfillment of the Requirements for the Subject CC103 Computer Programming 2 Under the Course of Bachelor of Science in Information Technology at Sorsogon State University Bulan Campus. With the Supervision of our Professor John Mark Gabrentina.

---

### Notes

- Basic input validation only (`strip()` checks and `try/except` for numeric inputs)
- Focus is on OOP structure, not advanced error handling
- Designed for educational purposes
