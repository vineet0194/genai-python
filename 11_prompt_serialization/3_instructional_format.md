<!-- INST formatting is a prompt format introduced by Llama 2 Chat models.
It wraps the user's instruction inside special tags so the model can distinguish the instruction
from the rest of the conversation. -->

<!-- The basic format is:

<s>[INST] User instruction [/INST]
Assistant response
</s> -->

<!-- example: -->

<s>[INST] <<SYS>>
You are a Senior Software Engineer.
Generate clean, production-ready code.
<</SYS>>

Write a JavaScript function to check if a string is a palindrome.
[/INST]

<!-- ----------------------------------------------------------------------------------------------------

## Why does it exist?

Llama 2 Chat was fine-tuned on data in this exact format. During training, the model learned that:

- `<<SYS>> ... <</SYS>>` contains system instructions.
- `[INST] ... [/INST]` contains the user's request.
- Everything after `[/INST]` is the assistant's response.

Using the expected format helps the model follow instructions more reliably. -->