from enum import Enum
from typing import Tuple


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    hex_color = hex_color.lstrip("#")

    # Explicitly split into 3 components to ensure tuple size
    return (int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))


class Colors(Enum):
    HIGHLIGHT_TAN = hex_to_rgb("#f6d6bd")
    MIDTONE_RED = hex_to_rgb("#816271")
