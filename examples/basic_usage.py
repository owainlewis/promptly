from promptly_ai import PromptManager
from datetime import datetime

content = PromptManager.render(
    "examples/prompts/hello.j2", time=datetime.now().isoformat()
)

metadata = PromptManager.get_metadata("examples/prompts/hello.j2")
