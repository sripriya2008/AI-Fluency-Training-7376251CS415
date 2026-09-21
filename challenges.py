import json

from config import client, MODEL
from tools import get_course_fee, calculator


question = """
I can pay Rs. 30,000.
The available courses are CS101, AI202, and DS303.
Use the course fee tool to check the fee of each course.
Then use the calculator to find which pair of two different courses has a total of Rs. 30,000 or less.
Give me the course names and total fee.
"""

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
                        "description": "A mathematical expression"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


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