from typing import Any, Dict, Tuple, Optional
from jinja2 import Environment, select_autoescape
from jinja2.exceptions import TemplateError
import os
import yaml


class PromptManager:
    """
    A simple template loader and renderer using Jinja2.
    """

    _env = Environment(autoescape=select_autoescape())

    @classmethod
    def _parse_frontmatter(cls, content: str) -> Tuple[Dict[str, Any], str]:
        """
        Parse YAML frontmatter from the template content.

        Args:
            content: The template content with optional frontmatter

        Returns:
            Tuple of (metadata dict, template content)
        """
        if not content.startswith("---\n"):
            return {}, content

        # Split the content into frontmatter and template
        parts = content.split("---\n", 2)
        if len(parts) != 3:
            return {}, content

        frontmatter, template = parts[1], parts[2]
        try:
            metadata = yaml.safe_load(frontmatter)
            return metadata or {}, template
        except yaml.YAMLError:
            return {}, content

    @classmethod
    def get_version(cls, path: str) -> Optional[str]:
        """
        Get the version from a template's metadata.

        Args:
            path: Path to the template file

        Returns:
            Version string or None if not specified
        """
        metadata = cls.get_metadata(path)
        return metadata.get("version")

    @classmethod
    def get_author(cls, path: str) -> Optional[str]:
        """
        Get the author from a template's metadata.

        Args:
            path: Path to the template file

        Returns:
            Author string or None if not specified
        """
        metadata = cls.get_metadata(path)
        return metadata.get("author")

    @classmethod
    def get_description(cls, path: str) -> Optional[str]:
        """
        Get the description from a template's metadata.

        Args:
            path: Path to the template file

        Returns:
            Description string or None if not specified
        """
        metadata = cls.get_metadata(path)
        return metadata.get("description")

    @classmethod
    def get_model(cls, path: str) -> Optional[str]:
        """
        Get the model from a template's metadata.

        Args:
            path: Path to the template file

        Returns:
            Model string or None if not specified
        """
        metadata = cls.get_metadata(path)
        return metadata.get("model")

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
            # Parse frontmatter and get template content
            metadata, template_content = cls._parse_frontmatter(template_content)

            # Add metadata to variables
            variables["metadata"] = metadata

            template = cls._env.from_string(template_content)
            return template.render(**variables)
        except TemplateError as e:
            raise ValueError(f"Error rendering template '{path}': {str(e)}")

    @classmethod
    def get_metadata(cls, path: str) -> Dict[str, Any]:
        """
        Get the metadata from a template file without rendering it.

        Args:
            path: Path to the template file

        Returns:
            Dictionary containing the template metadata

        Raises:
            FileNotFoundError: If template file doesn't exist
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"Template file not found: {path}")

        with open(path, "r") as f:
            template_content = f.read()

        metadata, _ = cls._parse_frontmatter(template_content)
        return metadata

    @classmethod
    def render_with_metadata(
        cls, path: str, **variables: Any
    ) -> Tuple[str, Dict[str, Any]]:
        """
        Load and render a template from a file, returning both the rendered content and metadata.

        Args:
            path: Path to the template file
            **variables: Variables to pass to the template

        Returns:
            Tuple of (rendered template string, metadata dictionary)

        Raises:
            FileNotFoundError: If template file doesn't exist
            ValueError: If template rendering fails
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"Template file not found: {path}")

        with open(path, "r") as f:
            template_content = f.read()

        try:
            # Parse frontmatter and get template content
            metadata, template_content = cls._parse_frontmatter(template_content)

            # Add metadata to variables
            variables["metadata"] = metadata

            template = cls._env.from_string(template_content)
            rendered_content = template.render(**variables)
            return rendered_content, metadata
        except TemplateError as e:
            raise ValueError(f"Error rendering template '{path}': {str(e)}")
