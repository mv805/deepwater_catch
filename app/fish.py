import pygame
from typing import Literal, Tuple
from typing import TYPE_CHECKING
from app.state_machine import State, StateMachine

if TYPE_CHECKING:
    # need this to forward reference the typing.
    from app.fishing_hook import FishingHook


class CaughtState(State):

    def enter(self, fish: "Fish", *args, **kwargs):
        fish._stop_swimming()

    def update(self, fish: "Fish", hook: "FishingHook", *args, **kwargs):
        # Follow hook position
        fish._move_fish_to_hook(hook)


class SwimmingState(State):

    def update(self, fish: "Fish", dt: float, hook: "FishingHook", *args, **kwargs):
        # Update position based on velocity
        fish.pos.x += fish.velocity.x * dt
        fish._rect.center = fish.pos

        # Check for collision with hook
        if pygame.sprite.collide_rect(fish, hook):
            fish._set_fish_caught(hook)


class Fish(pygame.sprite.Sprite):

    def __init__(
        self,
        start_pos: Tuple[int, int],
        fish_sprite: pygame.Surface,
        facing_direction: Literal["left", "right"],
        movement_speed: int,
    ):
        if movement_speed <= 0:
            raise ValueError("movement_speed must be > 0")
        super().__init__()
        self._movement_speed = movement_speed
        self._pos: pygame.math.Vector2 = pygame.math.Vector2(*start_pos)
        self._velocity = pygame.math.Vector2(self._movement_speed, 0)  # going right by default
        self._image: pygame.Surface = fish_sprite
        self._face_fish_if_left(facing_direction)
        self._rect: pygame.Rect = self._image.get_rect(center=(self._pos.x, self._pos.y))

        self._state_machine = StateMachine(self)
        self._state_machine.transition_to(SwimmingState())

    @property
    def pos(self) -> pygame.math.Vector2:
        return self._pos

    @property
    def velocity(self) -> pygame.math.Vector2:
        return self._velocity

    @property
    def image(self) -> pygame.Surface:
        return self._image

    @property
    def rect(self) -> pygame.Rect:
        return self._rect

    def _face_fish_if_left(self, direction: Literal["left", "right"]):
        if direction == "left":
            self._velocity = pygame.math.Vector2(-self._movement_speed, 0)
            self._image = pygame.transform.flip(self._image, True, False)

    def _move_fish_to_hook(self, hook: "FishingHook"):
        """moves the fish to the given hook"""
        self._pos = pygame.math.Vector2(hook.rect.center)
        self._rect.center = self._pos

    def _stop_swimming(self) -> None:
        """Stop movement of the fish"""
        self._velocity = pygame.math.Vector2(0, 0)

    def _set_fish_caught(self, hook) -> None:
        """Change to caught state"""
        self._state_machine.transition_to(CaughtState(), self)
        self._move_fish_to_hook(hook)

    def update(self, dt: float, hook: "FishingHook"):
        self._state_machine.update(dt=dt, hook=hook)
