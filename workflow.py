from config import COURSE_FEES

questions = [
    "What is the fee for AI202?",
    "What is the total fee for CS101 and AI202 after a 10% scholarship?",
    "What is the difference between DS303 and CS101?",
    "Write a two-line welcome message for our course."
]

for question in questions:
    q = question.lower()

    if "fee for ai202" in q:
        answer = f"AI202 fee is ₹{COURSE_FEES['AI202']}."

    elif "cs101 and ai202" in q and "10%" in q:
        total = COURSE_FEES["CS101"] + COURSE_FEES["AI202"]
        after_scholarship = total * 0.90
        answer = f"Total fee after 10% scholarship is ₹{after_scholarship:.0f}."

    elif "difference between ds303 and cs101" in q:
        difference = COURSE_FEES["DS303"] - COURSE_FEES["CS101"]
        answer = f"The fee difference is ₹{difference}."

    else:
        answer = "No rule available for this question."

    print("Question:", question)
    print("Answer:", answer)
    print("-" * 50)