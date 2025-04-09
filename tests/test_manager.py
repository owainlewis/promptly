from promptly_ai import render
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


def test_render_template_with_metadata():
    # Create a temporary file with a template and metadata
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("""---
version: 1.0.0
author: Test Author
description: Test template
---
Hello, {{ name }}!""")
        temp_path = f.name

    try:
        # Test loading and rendering the template
        result = render(temp_path, name="World")
        assert result == "Hello, World!"
    finally:
        # Clean up
        os.unlink(temp_path)


def test_render_template_with_metadata_access():
    # Create a temporary file with a template and metadata
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("""---
version: 1.0.0
author: Test Author
---
Hello, {{ name }}! This template was created by {{ metadata.author }}.""")
        temp_path = f.name

    try:
        # Test loading and rendering the template with metadata access
        result = render(temp_path, name="World")
        assert result == "Hello, World! This template was created by Test Author."
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
