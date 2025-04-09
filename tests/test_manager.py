from promptly_ai import PromptManager
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
        result = PromptManager.render(temp_path, name="World")
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
        result = PromptManager.render(temp_path, name="World")
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
        result = PromptManager.render(temp_path, name="World")
        assert result == "Hello, World! This template was created by Test Author."
    finally:
        # Clean up
        os.unlink(temp_path)


def test_template_not_found():
    with pytest.raises(FileNotFoundError):
        PromptManager.render("nonexistent.txt", name="World")


def test_invalid_template():
    # Create a temporary file with an invalid template
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("Hello, {{ name ")  # Missing closing brace
        temp_path = f.name

    try:
        with pytest.raises(ValueError):
            PromptManager.render(temp_path, name="World")
    finally:
        # Clean up
        os.unlink(temp_path)


def test_render():
    content = PromptManager.render("examples/prompts/hello.j2", time="2024-01-01")
    assert "2024-01-01" in content


def test_get_metadata():
    metadata = PromptManager.get_metadata("examples/prompts/hello.j2")
    assert "description" in metadata


def test_render_with_metadata():
    content, metadata = PromptManager.render_with_metadata(
        "examples/prompts/hello.j2", time="2024-01-01"
    )
    assert "2024-01-01" in content
    assert "description" in metadata


def test_get_version():
    # Create a temporary file with version metadata
    with tempfile.NamedTemporaryFile(mode="w", suffix=".j2", delete=False) as f:
        f.write("""---
version: 1.0.0
---
Hello, {{ name }}!""")
        temp_path = f.name

    try:
        version = PromptManager.get_version(temp_path)
        assert version == "1.0.0"
    finally:
        os.unlink(temp_path)


def test_get_author():
    # Create a temporary file with author metadata
    with tempfile.NamedTemporaryFile(mode="w", suffix=".j2", delete=False) as f:
        f.write("""---
author: Test Author
---
Hello, {{ name }}!""")
        temp_path = f.name

    try:
        author = PromptManager.get_author(temp_path)
        assert author == "Test Author"
    finally:
        os.unlink(temp_path)


def test_get_description():
    # Create a temporary file with description metadata
    with tempfile.NamedTemporaryFile(mode="w", suffix=".j2", delete=False) as f:
        f.write("""---
description: A test prompt
---
Hello, {{ name }}!""")
        temp_path = f.name

    try:
        description = PromptManager.get_description(temp_path)
        assert description == "A test prompt"
    finally:
        os.unlink(temp_path)


def test_get_model():
    # Create a temporary file with model metadata
    with tempfile.NamedTemporaryFile(mode="w", suffix=".j2", delete=False) as f:
        f.write("""---
model: gpt-4
---
Hello, {{ name }}!""")
        temp_path = f.name

    try:
        model = PromptManager.get_model(temp_path)
        assert model == "gpt-4"
    finally:
        os.unlink(temp_path)


def test_metadata_not_found():
    # Create a temporary file without metadata
    with tempfile.NamedTemporaryFile(mode="w", suffix=".j2", delete=False) as f:
        f.write("Hello, {{ name }}!")
        temp_path = f.name

    try:
        # All metadata getters should return None when metadata is not found
        assert PromptManager.get_version(temp_path) is None
        assert PromptManager.get_author(temp_path) is None
        assert PromptManager.get_description(temp_path) is None
        assert PromptManager.get_model(temp_path) is None
    finally:
        os.unlink(temp_path)


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        PromptManager.get_version("nonexistent.txt")
    with pytest.raises(FileNotFoundError):
        PromptManager.get_author("nonexistent.txt")
    with pytest.raises(FileNotFoundError):
        PromptManager.get_description("nonexistent.txt")
    with pytest.raises(FileNotFoundError):
        PromptManager.get_model("nonexistent.txt")


def test_xml_prompt():
    # Create a temporary file with XML content
    with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as f:
        f.write("""---
version: 1.0.0
model: gpt-4
---
<system>
    <role>You are a helpful assistant.</role>
    <context>The current time is {{ time }}.</context>
</system>""")
        temp_path = f.name

    try:
        content = PromptManager.render(temp_path, time="2024-01-01")
        assert "<system>" in content
        assert "2024-01-01" in content
        assert PromptManager.get_model(temp_path) == "gpt-4"
    finally:
        os.unlink(temp_path)


def test_markdown_prompt():
    # Create a temporary file with Markdown content
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write("""---
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
3. Be accurate""")
        temp_path = f.name

    try:
        content = PromptManager.render(temp_path, time="2024-01-01")
        assert "# System Prompt" in content
        assert "2024-01-01" in content
        assert "## Instructions" in content
        assert PromptManager.get_model(temp_path) == "gpt-4"
    finally:
        os.unlink(temp_path)


def test_mixed_format_prompt():
    # Create a temporary file with mixed XML and Markdown
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("""---
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
</system>""")
        temp_path = f.name

    try:
        content = PromptManager.render(temp_path, time="2024-01-01")
        assert "<system>" in content
        assert "# Role" in content
        assert "2024-01-01" in content
        assert "## Instructions" in content
        assert PromptManager.get_model(temp_path) == "gpt-4"
    finally:
        os.unlink(temp_path)
