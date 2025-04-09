"""
Promptly - A Python package for managing prompts using Jinja2 templates.
"""

__version__ = "0.1.0"

from .manager import Promptly

render = Promptly.render

__all__ = ["render"]
