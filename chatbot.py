from config import client, MODEL

questions = [
    "What is the fee for AI202?",
    "What is the total fee for CS101 and AI202 after a 10% scholarship?",
    "What is the difference between DS303 and CS101?",
    "Write a two-line welcome message for our course."
]

for question in questions:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": question}
        ]
    )

    print("Question:", question)
    print("Answer:", response.choices[0].message.content)
    print("-" * 50)