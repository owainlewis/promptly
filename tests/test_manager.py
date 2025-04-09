from promptly import render
import pytest
import os
import tempfile


def test_render_template():
    # Create a temporary file with a template
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("Hello, {{ name }}!")
        temp_path = f.name

    try:
        # Test loading and rendering the template
        result = render(temp_path, name="World")
        assert result == "Hello, World!"
    finally:
        # Clean up
        os.unlink(temp_path)


def test_template_not_found():
    with pytest.raises(FileNotFoundError):
        render("nonexistent.txt", name="World")


def test_invalid_template():
    # Create a temporary file with an invalid template
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("Hello, {{ name ")  # Missing closing brace
        temp_path = f.name

    try:
        with pytest.raises(ValueError):
            render(temp_path, name="World")
    finally:
        # Clean up
        os.unlink(temp_path)
