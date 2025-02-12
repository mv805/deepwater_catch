import pygame
from typing import Literal, Tuple
from typing import TYPE_CHECKING
from app.state_machine import State, StateMachine

if TYPE_CHECKING:
    # need this to forward reference the typing.
    from app.fishing_hook import FishingHook


class CaughtState(State):

    def enter(self, fish: "Fish", *args, **kwargs):
        fish.stop_swimming()

    def update(self, fish: "Fish", hook: "FishingHook", *args, **kwargs):
        # Follow hook position
        fish.move_fish_to_hook(hook)


class SwimmingState(State):

    def update(self, fish: "Fish", dt: float, hook: "FishingHook", screen_width: int, *args, **kwargs):
        # Update position based on velocity
        fish.pos.x += fish.velocity.x * dt
        fish.rect.center = fish.pos

        # Check screen boundaries
        if fish.velocity.x < 0 and fish.rect.topright[0] < 0:
            fish.kill()
        elif fish.velocity.x > 0 and fish.rect.topleft[0] >= screen_width:
            fish.kill()

        # Check for collision with hook
        if pygame.sprite.collide_rect(fish, hook):
            fish.set_fish_caught(hook)


class Fish(pygame.sprite.Sprite):

    def __init__(
        self,
        start_pos: Tuple[int, int],
        fish_sprite: pygame.Surface,
        facing_direction: Literal["left", "right"],
        movement_speed: int,
        screen: pygame.Surface,
    ):
        if movement_speed <= 0:
            raise ValueError("movement_speed must be > 0")
        super().__init__()
        self._screen_width = screen.get_width()
        self._movement_speed = movement_speed
        self._pos: pygame.math.Vector2 = pygame.math.Vector2(*start_pos)
        self._velocity = pygame.math.Vector2(self._movement_speed, 0)  # going right by default
        self.image: pygame.Surface = fish_sprite
        self._face_fish_if_left(facing_direction)
        self.rect: pygame.Rect = self.image.get_rect(center=(self._pos.x, self._pos.y))

        self._state_machine = StateMachine(self)
        self._state_machine.transition_to(SwimmingState())

    @property
    def pos(self) -> pygame.math.Vector2:
        return self._pos

    @property
    def velocity(self) -> pygame.math.Vector2:
        return self._velocity

    def _face_fish_if_left(self, direction: Literal["left", "right"]):
        if direction == "left":
            self._velocity = pygame.math.Vector2(-self._movement_speed, 0)
            self.image = pygame.transform.flip(self.image, True, False)

    def move_fish_to_hook(self, hook: "FishingHook"):
        """moves the fish to the given hook"""
        self._pos = pygame.math.Vector2(hook.rect.center)
        self.rect.center = self._pos

    def stop_swimming(self) -> None:
        """Stop movement of the fish"""
        self._velocity = pygame.math.Vector2(0, 0)

    def set_fish_caught(self, hook) -> None:
        """Change to caught state"""
        self._state_machine.transition_to(CaughtState(), self)
        self.move_fish_to_hook(hook)

    def update(self, dt: float, hook: "FishingHook", screen_width: int):
        self._state_machine.update(dt=dt, hook=hook, screen_width=screen_width)
