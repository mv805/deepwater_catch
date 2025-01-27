import pygame
from typing import Literal, Tuple
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fishing_hook import FishingHook


class FishState(Enum):
    SWIMMING = "swimming"
    CAUGHT = "caught"


class Fish(pygame.sprite.Sprite):
    def __init__(
        self,
        start_pos: Tuple[int, int],
        fish_sprite: pygame.Surface,
        facing_direction: Literal["left", "right"],
        movement_speed: int,
        screen: pygame.Surface,
    ):
        super().__init__()
        self.movement_speed = movement_speed
        self.image: pygame.Surface = fish_sprite
        self.velocity = pygame.math.Vector2(self.movement_speed, 0)  # going right by default
        self.face_fish_if_left(facing_direction)
        self.pos = pygame.math.Vector2(*start_pos)
        self.rect: pygame.Rect = self.image.get_rect(center=(self.pos.x, self.pos.y))
        # self.OFFSCREEN_KILL_RANGE = 200
        self.screen = screen
        self.state = FishState.SWIMMING

    def face_fish_if_left(self, direction: Literal["left", "right"]):
        if direction == "left":
            self.velocity = pygame.math.Vector2(-self.movement_speed, 0)
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self, dt: float, hook_pos: pygame.math.Vector2, hook: "FishingHook"):

        if self.state == FishState.SWIMMING:
            # Move the fish left and right
            self.pos.x += self.velocity.x * dt

            # Kill if off screen
            if self.velocity.x < 0 and self.rect.topright[0] < 0:  # Moving left
                self.kill()
            elif self.velocity.x > 0 and self.rect.topleft[0] > self.screen.get_width():  # Moving right
                self.kill()

        if self.state == FishState.CAUGHT:
            self.pos = hook_pos
            self.rect.midtop = hook_pos
        else:
            self.rect.center = self.pos

        # check for collision with hook
        if self.state == FishState.SWIMMING:
            if pygame.sprite.collide_rect(self, hook):
                self.state = FishState.CAUGHT
                self.velocity = pygame.math.Vector2(0, 0)  # stop moving
