# Promptly

Promptly is a simple Python library for managing AI prompts.

## Build

![Test](https://github.com/owainlewis/promptly/actions/workflows/test.yml/badge.svg)

## Installation (WIP)

```bash
pip install promptly
```

## Quick Start

Create a prompt 

```
---
version: 1.0.0
author: Owain Lewis
description: Example prompt to demonstrate the use of the Promptly library
model: gpt-4o
---
You are a helpful assistant.

The time is {{ time }}.
```

Render it using Promptly

```python
from promptly_ai import render
from datetime import datetime

system_prompt = render("examples/prompts/hello.j2", time=datetime.now().isoformat())

print(system_prompt)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
