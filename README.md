# Promptly

A simple Python library for managing prompts using Jinja2 templates with YAML frontmatter support.

This library is based on these ideas:

- For AI projects, prompts are as important as code
- Prompts should be managed as files
- Prompts should support metadata such as version, author, description, and model instructions.
- Managing prompts should be easy by default

## Build

![Test](https://github.com/owainlewis/promptly/actions/workflows/test.yml/badge.svg)

## Installation

```bash
pip install promptly-ai
```

## Usage

### Basic Usage

Create a prompt file with YAML frontmatter:

```yaml
---
version: 1.0.0
author: Owain Lewis
model: gpt-4
description: A simple greeting prompt with personality
---
You are a friendly and enthusiastic assistant. Your name is {{ name }} and you love helping people!

The current time is {{ time }}. How can I help you today?
```

Then use it in your Python code:

```python
from promptly_ai import PromptManager
from datetime import datetime

# Simple rendering
content = PromptManager.render("greeting.txt", name="Alex", time=datetime.now().isoformat())
print(content)

# Get metadata
model = PromptManager.get_model("greeting.txt")
print(f"Using model: {model}")  # "Using model: gpt-4"
```

### Prompt Formats

#### XML Format - Code Review Assistant
```xml
---
version: 1.1.0
author: Code Review Team
model: claude-3-opus
description: A structured prompt for code review assistance
---
<system>
    <role>You are an expert code reviewer with 20 years of experience.</role>
    <context>
        <language>{{ language }}</language>
        <framework>{{ framework }}</framework>
        <style_guide>{{ style_guide }}</style_guide>
    </context>
    <instructions>
        <item>Review the code for best practices</item>
        <item>Check for security vulnerabilities</item>
        <item>Suggest performance improvements</item>
        <item>Ensure style guide compliance</item>
    </instructions>
</system>
```

#### Markdown Format - Creative Writing Assistant
```markdown
---
version: 2.0.0
author: Creative Writing Team
model: gpt-4-turbo
description: A creative writing assistant with genre-specific guidance
---
# Creative Writing Assistant

## Role
You are an award-winning author specializing in {{ genre }} fiction.

## Context
- Target audience: {{ audience }}
- Word count: {{ word_count }} words
- Tone: {{ tone }}

## Instructions
1. Generate a compelling {{ genre }} story opening
2. Include vivid sensory details
3. Establish clear character motivations
4. Set up an intriguing conflict

## Style Guidelines
- Use active voice
- Show, don't tell
- Vary sentence structure
- Include dialogue where appropriate
```

#### Mixed Format - Data Analysis Assistant
```xml
---
version: 1.2.0
author: Data Science Team
model: claude-3-sonnet
description: A data analysis assistant with structured guidance
---
<system>
    # Role
    You are a data analysis expert with expertise in {{ domain }}.

    ## Context
    - Dataset: {{ dataset_name }}
    - Size: {{ row_count }} rows × {{ column_count }} columns
    - Analysis Type: {{ analysis_type }}

    ## Instructions
    1. Analyze the data for {{ analysis_goal }}
    2. Identify key patterns and trends
    3. Generate visualizations if appropriate
    4. Provide actionable insights

    ## Output Format
    <output>
        <summary>Brief overview of findings</summary>
        <methodology>Analysis approach used</methodology>
        <findings>Key insights discovered</findings>
        <recommendations>Actionable next steps</recommendations>
    </output>
</system>
```

### Metadata Support

Prompts can include metadata in YAML frontmatter. Common metadata fields include:

```yaml
---
version: 1.0.0
author: Your Name
description: A description of the prompt
model: gpt-4  # or claude-3-opus, gpt-4-turbo, etc.
parameters:
  temperature: 0.7
  max_tokens: 2000
  top_p: 0.9
tags:
  - category: writing
  - difficulty: intermediate
  - use_case: creative
---
Your prompt content here
```

You can access metadata using convenience methods:

```python
from promptly_ai import PromptManager

# Get specific metadata fields
version = PromptManager.get_version("prompt.txt")
author = PromptManager.get_author("prompt.txt")
description = PromptManager.get_description("prompt.txt")
model = PromptManager.get_model("prompt.txt")

# Or get all metadata
metadata = PromptManager.get_metadata("prompt.txt")
print(f"Using {model} with parameters: {metadata['parameters']}")
```

### Advanced Usage

You can use any Jinja2 template features in your prompts:

```yaml
---
version: 1.0.0
author: Prompt Engineering Team
model: gpt-4
description: A dynamic prompt generator based on user preferences
parameters:
  genre: [fantasy, sci-fi, mystery]
  length: [short, medium, long]
  style: [formal, casual, poetic]
---
# {{ parameters.genre|title }} Story Generator

{% if parameters.genre == "fantasy" %}
You are a master of fantasy world-building. Create a story set in a magical realm where {{ setting }}.
{% elif parameters.genre == "sci-fi" %}
You are a visionary science fiction writer. Craft a story set in {{ year }} where {{ setting }}.
{% else %}
You are a mystery writer known for intricate plots. Develop a story where {{ setting }}.
{% endif %}

The story should be {{ parameters.length }} in length and written in a {{ parameters.style }} style.

{% if parameters.length == "long" %}
Include multiple plot twists and character arcs.
{% elif parameters.length == "medium" %}
Focus on a single main plot with one or two subplots.
{% else %}
Keep the story focused and concise.
{% endif %}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
