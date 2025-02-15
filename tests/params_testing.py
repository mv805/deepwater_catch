from dataclasses import dataclass
import json

with open("assets/sprite_sheet.json", "r") as f:
    sprite_data = json.load(f)


@dataclass(frozen=True)
class SpriteDimensions:
    width: int
    height: int


@dataclass(frozen=True)
class TestParams:
    """Different parameters used in the testing files.
    The objective is to base some of the variables on real sizing to
    be more realistic and allow changes to graphics over time,
    as well as reduce the usage of magic numbers."""

    HOOK_SPRITE: SpriteDimensions = SpriteDimensions(
        sprite_data["frames"]["Hook"]["frame"]["w"], sprite_data["frames"]["Hook"]["frame"]["h"]
    )

    FISH_SPRITE: SpriteDimensions = SpriteDimensions(
        sprite_data["frames"]["Fish"]["frame"]["w"], sprite_data["frames"]["Fish"]["frame"]["h"]
    )
