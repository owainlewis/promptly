from promptly_ai import render
from datetime import datetime

system_prompt = render("examples/prompts/hello.j2", time=datetime.now().isoformat())

print(system_prompt)
