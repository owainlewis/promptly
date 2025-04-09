from typing import Any
from jinja2 import Environment, select_autoescape
from jinja2.exceptions import TemplateError
import os


class Promptly:
    """
    A simple template loader and renderer using Jinja2.
    """

    _env = Environment(autoescape=select_autoescape())

    @classmethod
    def render(cls, path: str, **variables: Any) -> str:
        """
        Load and render a template from a file.

        Args:
            path: Path to the template file
            **variables: Variables to pass to the template

        Returns:
            Rendered template string

        Raises:
            FileNotFoundError: If template file doesn't exist
            ValueError: If template rendering fails
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"Template file not found: {path}")

        with open(path, "r") as f:
            template_content = f.read()

        try:
            template = cls._env.from_string(template_content)
            return template.render(**variables)
        except TemplateError as e:
            raise ValueError(f"Error rendering template '{path}': {str(e)}")
