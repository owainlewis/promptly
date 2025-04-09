# Promptly

A simple Python library for managing prompts using Jinja2 templates with YAML frontmatter support.

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
title: Greeting Prompt
description: A simple greeting prompt
tags: [greeting, basic]
---
Hello, {{ name }}! How are you today?
```

Then use it in your Python code:

```python
from promptly_ai import PromptManager

# Simple rendering
content = PromptManager.render("greeting.txt", name="World")
print(content)  # "Hello, World! How are you today?"

# Get metadata
metadata = PromptManager.get_metadata("greeting.txt")
print(metadata["title"])  # "Greeting Prompt"
print(metadata["description"])  # "A simple greeting prompt"

# Get both content and metadata
content, metadata = PromptManager.render_with_metadata("greeting.txt", name="World")
```

### Prompt Formats

#### XML Format
```xml
---
version: 1.0.0
model: gpt-4
---
<system>
    <role>You are a helpful assistant.</role>
    <context>The current time is {{ time }}.</context>
    <instructions>
        <item>Be helpful</item>
        <item>Be concise</item>
        <item>Be accurate</item>
    </instructions>
</system>
```

#### Markdown Format
```markdown
---
version: 1.0.0
model: gpt-4
---
# System Prompt

You are a helpful assistant.

## Context
The current time is {{ time }}.

## Instructions
1. Be helpful
2. Be concise
3. Be accurate
```

#### Mixed Format
```xml
---
version: 1.0.0
model: gpt-4
---
<system>
    # Role
    You are a helpful assistant.

    ## Context
    The current time is {{ time }}.

    ## Instructions
    1. Be helpful
    2. Be concise
    3. Be accurate
</system>
```

### Metadata Support

Prompts can include metadata in YAML frontmatter. Common metadata fields include:

```yaml
---
version: 1.0.0
author: Your Name
description: A description of the prompt
model: gpt-4
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
```

### Advanced Usage

You can use any Jinja2 template features in your prompts:

```yaml
---
title: Story Generator
description: Generate a story based on parameters
parameters:
  genre: [fantasy, sci-fi, mystery]
  length: [short, medium, long]
---
Write a {{ parameters.genre }} story that is {{ parameters.length }} in length.

{% if parameters.genre == "fantasy" %}
Include magical elements and mythical creatures.
{% elif parameters.genre == "sci-fi" %}
Include futuristic technology and space exploration.
{% else %}
Include suspense and plot twists.
{% endif %}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
