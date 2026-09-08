"""Generate instruction Markdown from the structured instruction sources."""

import pathlib
import re

import yaml


BASE_DIR = pathlib.Path(__file__).resolve().parent
INSTRUCTION_DATA_DIR = BASE_DIR / "instruction-data"
DOCS_DIR = BASE_DIR / "docs"
IMAGE_PREFIX = "/assets/images/web/"


def _load_source(source_path):
    """Load one structured YAML instruction source."""
    with source_path.open(encoding="utf-8") as source_file:
        document = yaml.safe_load(source_file)
    if not isinstance(document, dict):
        raise ValueError(f"Expected a mapping in {source_path}")
    return document


def render_markdown(markdown):
    """Expand color shorthand in Markdown content."""
    replacements = {
        ".rcir.": ":red_circle:",
        ".ocir.": ":orange_circle:",
        ".gcir.": ":green_circle:",
        ".bcir.": ":blue_circle:",
        ".pcir.": ":purple_circle:",
    }
    for line in markdown.splitlines():
        if line.startswith("    "):
            line = line[4:]
        line = re.sub(
            r"(!\[.*?\]\()(?!/|https?://)([^)]+\.png)(\))",
            rf"\g<1>{IMAGE_PREFIX}\g<2>\g<3>",
            line,
        )
        for source, target in replacements.items():
            line = line.replace(source, target)
        yield line


def render_step(step, step_number):
    lines = [f"###**Step {step_number}** {step.get('title', '')}", ""]
    images = step.get("images", [])
    if images:
        lines.append('<div class="grid cards" markdown>')
        for image_number, image in enumerate(images):
            hidden = ".hidden " if image_number else ""
            prefix = "- " if image_number == 0 else "    "
            lines.append(
                f'{prefix}![](/assets/images/web/{image}.png){{{hidden}data-gallery="step{step_number}"}}'
            )
        body_lines = list(render_markdown(step.get("body", "")))
        if body_lines:
            lines.append("")
            lines.append(f"- {body_lines[0]}")
            lines.extend(
                f"    {line}" if line else ""
                for line in body_lines[1:]
            )
        lines.extend(["", "</div>"])
        for image_style in step.get("image_styles", []):
            image_id = image_style["id"]
            classes = image_style.get("classes", "")
            classes = ' '.join(map(lambda c: '.'+c if not c.startswith('.') else c, classes.split()))
            class_attribute = f".sm {classes}".rstrip()
            lines.append(
                f'![](/assets/images/web/{image_id}.png){{{class_attribute} '
                f'data-gallery="step{step_number}-sm"}}'
            )
    elif step.get("body"):
        lines.append("\n".join(render_markdown(step["body"])))
    return "\n".join(lines)


def render_instruction_sources():
    for source_path in sorted((INSTRUCTION_DATA_DIR / "instructions").glob("*.yaml")):
        document = _load_source(source_path)
        metadata = "\n".join(
            f"{key}: {str(value).lower() if isinstance(value, bool) else value}"
            for key, value in document["metadata"].items()
        )
        sections = [document.get("before", "")]
        sections.extend(
            render_step(step, number)
            for number, step in enumerate(document["steps"], start=1)
        )
        sections.append(document.get("after", ""))
        content = "\n\n".join(section for section in sections if section)
        rendered = f"---\n{metadata}\n---\n\n{content}\n"
        output_path = DOCS_DIR / document["output"]
        output_path.parent.mkdir(parents=True, exist_ok=True)
        existing = output_path.read_text(encoding="utf-8") if output_path.exists() else None
        if existing != rendered:
            output_path.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    render_instruction_sources()