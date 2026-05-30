# 🏃 FitTracker — Personal Fitness Report Generator

A Python terminal application that tracks your workouts, calculates your BMI, monitors your calorie burn, and generates a personal fitness report — either printed on screen or saved to a file.

---

## 📁 Project Structure

```
fitness-app/
├── main.py          # Entry point — starts the app and connects all the parts
├── models.py        # Fitness logic — BMI, calorie, and goal calculations
├── io_handlers.py   # Input and output — reads user data, writes results
└── fitness_ui.py    # Terminal UI — styled step-by-step interface (optional)
```

---

## ▶️ How to Run

Make sure you have **Python 3.7 or higher** installed. No third-party libraries are required.

### Basic version
```bash
python3 main.py
```

### Styled terminal UI version
```bash
python3 fitness_ui.py
```

---

## 💡 How It Works

The app follows a simple three-step flow:

1. **Input** — You enter your name, weight, height, and workout details (exercise name, duration, and calories burned per minute).
2. **Process** — The app calculates your BMI, total calories burned, and checks whether you hit your daily calorie goal.
3. **Output** — The results are displayed on screen or saved to a text file.

---

## ✨ Features

- **BMI Calculation** — Computes your Body Mass Index from weight and height, and classifies it as Underweight, Normal, Overweight, or Obese.
- **Calorie Tracking** — Calculates total calories burned across all exercises in a session.
- **Goal Monitoring** — Compares your total calories burned against your personal daily goal and tells you whether you achieved it.
- **Multiple Output Options** — Print results to the screen or save them to a `.txt` file. You can also do both.
- **Multiple Exercises** — Log as many exercises as you performed in one session.
- **Styled Terminal UI** — `fitness_ui.py` provides a colour-coded, step-by-step interface with visual BMI and calorie progress bars.

---

## 🖥️ Example Output

```
===== FITNESS REPORT =====
User: Maria Santos
BMI: 24.80 (Normal)

Running - 30 min - 300 calories
Cycling - 20 min - 160 calories
--------------------------
Total Calories Burned: 460
Goal: 500 calories
Status: Goal Not Achieved
==========================
```

---

## 💾 Saving to a File

To save the report to a file instead of printing it, open `main.py` and swap the writer:

```python
# Change this:
writer = ScreenOutput()

# To this:
writer = FileOutput("fitness_report.txt")
```

The report will be saved as `fitness_report.txt` in the same folder.

---

## 🧪 Running the Tests

Unit tests are included inside `models.py`. Run them with:

```bash
python3 models.py
```

Expected output:
```
test_bmi_calculation PASSED
test_calorie_total PASSED
test_goal_status PASSED

All tests passed.
```

The tests cover BMI calculation accuracy, total calorie computation, and goal status evaluation.

---

## 🏗️ Design Overview

The app is built around three core features that are kept separate from each other:

| Feature | File | What it does |
|---|---|---|
| App Entry | `main.py` | Starts the program and connects all the pieces together |
| Input / Output | `io_handlers.py` | Handles where data comes from and where results go |
| Fitness Logic | `models.py` | Performs all health calculations |

This separation makes the code easy to maintain. For example, you can add a new output method (such as saving to a CSV or sending an email) without touching the calculation logic at all.

---

## 🔧 Customising the Calorie Goal

The default calorie goal is set to **500 calories**. You can change it in `main.py`:

```python
processor = FitnessProcessor(calorie_goal=300)  # change to any value you want
```

---

## 📋 Requirements

- Python 3.7+
- No external libraries needed — uses only the Python standard library
