# =====================================
# models.py — Data Processing & Business Logic
# =====================================


# =====================================
# FITNESS PROCESSOR
# =====================================
class FitnessProcessor:

    def __init__(self, calorie_goal=500):
        self._calorie_goal = calorie_goal

    def process(self, workouts):

        if not workouts:
            return {
                "name": "Unknown",
                "bmi": 0,
                "bmi_category": "N/A",
                "details": [],
                "total_calories": 0,
                "goal": self._calorie_goal,
                "goal_status": "Goal Not Achieved"
            }

        results = []
        total = 0

        name = workouts[0]["name"]
        weight = workouts[0]["weight"]
        height = workouts[0]["height"]

        bmi = self._calculate_bmi(weight, height)
        bmi_category = self._bmi_category(bmi)

        for w in workouts:

            calories = self._calculate_calories(
                w["duration"],
                w["calories_per_min"]
            )

            results.append({
                "exercise": w["exercise"],
                "duration": w["duration"],
                "calories": calories
            })

            total += calories

        goal_status = self._check_goal(total)

        return {
            "name": name,
            "bmi": bmi,
            "bmi_category": bmi_category,
            "details": results,
            "total_calories": total,
            "goal": self._calorie_goal,
            "goal_status": goal_status
        }

    # =========================
    # PRIVATE METHODS
    # =========================

    def _calculate_bmi(self, weight, height_cm):
        height_m = height_cm / 100
        return weight / (height_m ** 2)

    def _calculate_calories(self, duration, calories_per_min):
        return duration * calories_per_min

    def _bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def _check_goal(self, total):
        if total >= self._calorie_goal:
            return "Goal Achieved"
        else:
            return "Goal Not Achieved"


# =====================================
# UNIT TESTS
# =====================================

def test_bmi_calculation():
    processor = FitnessProcessor()
    bmi = processor._calculate_bmi(70, 175)
    assert round(bmi, 2) == 22.86, f"Expected 22.86, got {round(bmi, 2)}"
    print("test_bmi_calculation PASSED")


def test_calorie_total():
    processor = FitnessProcessor()
    workouts = [
        {
            "name": "John",
            "weight": 70,
            "height": 175,
            "exercise": "Running",
            "duration": 30,
            "calories_per_min": 10
        }
    ]
    result = processor.process(workouts)
    assert result["total_calories"] == 300, f"Expected 300, got {result['total_calories']}"
    print("test_calorie_total PASSED")


def test_goal_status():
    processor = FitnessProcessor(calorie_goal=200)
    workouts = [
        {
            "name": "John",
            "weight": 70,
            "height": 175,
            "exercise": "Running",
            "duration": 30,
            "calories_per_min": 10
        }
    ]
    result = processor.process(workouts)
    assert result["goal_status"] == "Goal Achieved", f"Expected 'Goal Achieved', got {result['goal_status']}"
    print("test_goal_status PASSED")


if __name__ == "__main__":
    test_bmi_calculation()
    test_calorie_total()
    test_goal_status()
    print("\nAll tests passed.")
