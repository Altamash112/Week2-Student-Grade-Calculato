# Student Grade Calculator

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Outstanding Performance! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good Job! You can do even better! 😊"
    elif marks >= 60:
        return "D", "Nice Effort! Keep practicing! 💪"
    else:
        return "F", "Don't give up! Practice and try again! 📚"


name = input("Enter student name: ")

while True:
    marks = int(input("Enter marks (0-100): "))

    if 0 <= marks <= 100:
        break
    else:
        print("❌ Invalid Marks! Please enter marks between 0 and 100.")

grade, message = calculate_grade(marks)

print("\n📊 RESULT FOR", name.upper())
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")