# =====================================
# io_handlers.py — Input Readers & Output Writers
# =====================================

from abc import ABC, abstractmethod


# =====================================
# INPUT READER INTERFACE
# =====================================
class InputReader(ABC):

    @abstractmethod
    def read_data(self):
        pass


# =====================================
# CONSOLE INPUT READER
# =====================================
class ConsoleInputReader(InputReader):

    def read_data(self):

        workouts = []

        name = input("Enter your name: ")
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (cm): "))

        count = int(input("How many exercises did you perform? "))

        for i in range(count):

            print(f"\nExercise {i+1}")

            exercise = input("Exercise name: ")
            duration = int(input("Duration (minutes): "))
            calories = int(input("Calories burned per minute: "))

            workouts.append({
                "name": name,
                "weight": weight,
                "height": height,
                "exercise": exercise,
                "duration": duration,
                "calories_per_min": calories
            })

        return workouts


# =====================================
# OUTPUT WRITER INTERFACE
# =====================================
class OutputWriter(ABC):

    @abstractmethod
    def write(self, data):
        pass


# =====================================
# SCREEN OUTPUT
# =====================================
class ScreenOutput(OutputWriter):

    def write(self, data):

        print("\n===== FITNESS REPORT =====")

        print(f"User: {data['name']}")
        print(f"BMI: {data['bmi']:.2f} ({data['bmi_category']})\n")

        for item in data["details"]:
            print(
                f"{item['exercise']} - "
                f"{item['duration']} min - "
                f"{item['calories']} calories"
            )

        print("--------------------------")
        print(f"Total Calories Burned: {data['total_calories']}")
        print(f"Goal: {data['goal']} calories")
        print(f"Status: {data['goal_status']}")
        print("==========================\n")


# =====================================
# FILE OUTPUT (Polymorphism example)
# =====================================
class FileOutput(OutputWriter):

    def __init__(self, filename):
        self._filename = filename

    def write(self, data):

        with open(self._filename, "w") as file:

            file.write("FITNESS REPORT\n\n")

            file.write(f"User: {data['name']}\n")
            file.write(f"BMI: {data['bmi']:.2f} ({data['bmi_category']})\n\n")

            for item in data["details"]:
                file.write(
                    f"{item['exercise']} - "
                    f"{item['duration']} min - "
                    f"{item['calories']} calories\n"
                )

            file.write("\n---------------------\n")
            file.write(f"Total Calories: {data['total_calories']}\n")
            file.write(f"Goal: {data['goal']}\n")
            file.write(f"Status: {data['goal_status']}\n")
