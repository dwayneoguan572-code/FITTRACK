# =====================================
# main.py — Application Controller & Entry Point
# =====================================

from io_handlers import ConsoleInputReader, ScreenOutput, FileOutput
from models import FitnessProcessor


# =====================================
# APPLICATION CONTROLLER
# =====================================
class FitnessApp:

    def __init__(self, reader, processor, writer):
        self._reader = reader
        self._processor = processor
        self._writer = writer

    def run(self):
        workouts = self._reader.read_data()
        results = self._processor.process(workouts)
        self._writer.write(results)


# =====================================
# MAIN PROGRAM
# =====================================
if __name__ == "__main__":

    reader = ConsoleInputReader()

    processor = FitnessProcessor(calorie_goal=500)

    # Polymorphism example — swap writers without changing any other code:
    writer = ScreenOutput()
    # writer = FileOutput("fitness_report.txt")

    app = FitnessApp(reader, processor, writer)

    app.run()
