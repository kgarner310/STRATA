from __future__ import annotations

from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader


class PromptEngine:
    def __init__(self) -> None:
        template_dir = Path(__file__).parent.parent.parent / "prompts"
        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            autoescape=False,
        )

    def render(self, template_path: str, **context: Any) -> str:
        template = self.env.get_template(template_path)
        return template.render(**context)


prompt_engine = PromptEngine()
