from config import COURSE_FEES


def get_course_fee(course_code):
    return COURSE_FEES.get(course_code.upper(), "Course not found")


def calculator(expression):
    try:
        allowed = set("0123456789+-*/(). ")
        if not all(char in allowed for char in expression):
            return "Invalid expression"

        return eval(expression, {"__builtins__": {}}, {})
    except Exception:
        return "Calculation error"


if __name__ == "__main__":
    print("AI202 fee:", get_course_fee("AI202"))
    print("Calculation:", calculator("12000 + 18000"))