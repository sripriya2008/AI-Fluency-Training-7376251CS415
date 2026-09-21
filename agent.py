import json

from config import client, MODEL
from tools import get_course_fee, calculator


questions = [
    "What is the fee for AI202?",
    "What is the total fee for CS101 and AI202 after a 10% scholarship?",
    "What is the difference between DS303 and CS101?",
    "Write a two-line welcome message for our course."
]


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get the fee of a course using its course code.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "Course code such as CS101, AI202, or DS303"
                    }
                },
                "required": ["course_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A mathematical expression such as 12000 + 18000"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


for question in questions:

    messages = [
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(5):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            print("Question:", question)
            print("Answer:", message.content)
            print("-" * 50)
            break

        for tool_call in message.tool_calls:

            name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            if name == "get_course_fee":
                result = get_course_fee(arguments["course_code"])

            elif name == "calculator":
                result = calculator(arguments["expression"])

            else:
                result = "Unknown tool"

            print("Tool used:", name)
            print("Tool result:", result)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                }
            )