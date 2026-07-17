<!-- ChatML (Chat Markup Language) is a message format developed by OpenAI to structure conversations by explicitly
separating messages into roles such as system, user, and assistant.

Instead of writing one long prompt, you send a list of messages, each with a defined role. -->

<!-- Roles in ChatML
System → Defines the assistant's behavior, personality, constraints, or goals.
User → Contains the user's request.
Assistant → Previous assistant responses (used to provide conversation history). -->

<!-- example: -->

messages = [
    {
        "role": "system",
        "content": "You are a Senior Software Engineer."
    },
    {
        "role": "user",
        "content": "Write a JavaScript function to check if a number is prime."
    },
    {
        "role": "assistant",
        "content": "Sure! Here's an efficient implementation..."
    },
    {
        "role": "user",
        "content": "Now write the Python version."
    }
]

<!-- Even though your SYSTEM_PROMPT contains persona and few-shot examples, the overall prompting style is ChatML,
because you're communicating through role-based messages rather than a single monolithic text prompt. -->


<!-- for the most part, you will be using this style formatting only, except you encounter a model
that explicitly expects inputs in that particualr format -->