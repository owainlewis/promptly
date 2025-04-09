# Promptly

Promptly is a simple Python package for rendering Jinja2 templates from files. It provides a clean and straightforward way to load and render template files.

## Installation

```bash
pip install promptly
```

## Quick Start

```python
from promptly import render

# Create a template file
with open("template.txt", "w") as f:
    f.write("Hello, {{ name }}! Welcome to {{ platform }}.")

# Render the template
result = render("template.txt", name="Alice", platform="Promptly")
print(result)  # Output: Hello, Alice! Welcome to Promptly.
```

## Features

- Simple, single-function interface
- Jinja2 template support
- File-based template loading
- Clean error handling
- Type hints included

## Documentation

For detailed documentation, please visit [the documentation page](https://github.com/yourusername/promptly#readme).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 