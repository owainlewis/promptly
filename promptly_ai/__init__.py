"""
PromptManager - A Python package for managing prompts using Jinja2 templates.
"""

from .manager import PromptManager

render = PromptManager.render
get_metadata = PromptManager.get_metadata
render_with_metadata = PromptManager.render_with_metadata

# Metadata accessors
get_version = PromptManager.get_version
get_author = PromptManager.get_author
get_description = PromptManager.get_description
get_model = PromptManager.get_model

__all__ = [
    "PromptManager",
    "render",
    "get_metadata",
    "render_with_metadata",
    "get_version",
    "get_author",
    "get_description",
    "get_model",
]
