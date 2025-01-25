import pygame
from enum import Enum
from typing import Tuple


class PlayerState(Enum):

    MOVING = "moving"
    CASTING = "casting"


class PlayerController(pygame.sprite.Sprite):

    def __init__(self, start_pos: Tuple[int, int], boat_sprite, screen_width):
        super().__init__()
        self.MOVEMENT_SPEED = 200
        self._state = PlayerState.MOVING
        self.screen_width = screen_width
        self.velocity = pygame.math.Vector2(self.MOVEMENT_SPEED, 0)

        self.image = boat_sprite
        self.pos = pygame.math.Vector2(*start_pos)
        self.rect: pygame.Rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))

        self.LEFT_STOP_MOVEMENT_OFFSET = self.image.get_width()

        self._spacebar_pressed = False

    def cast(self):
        self._state = PlayerState.CASTING
        self.velocity = pygame.math.Vector2(0, 0)

    def move(self):
        self._state = PlayerState.MOVING
        self.velocity = pygame.math.Vector2(self.MOVEMENT_SPEED, 0)

    def update(self, dt, keys, hook_pos: pygame.math.Vector2) -> None:

        # check if the hook is back at the pole
        if hook_pos.y == self.pos.y and self._state == PlayerState.CASTING:
            self.move()

        # Detect spacebar press to 'debounce'
        if keys[pygame.K_SPACE]:
            if not self._spacebar_pressed:
                self._spacebar_pressed = True
                if self._state == PlayerState.MOVING:
                    self.cast()
        else:
            self._spacebar_pressed = False

        if self._state == PlayerState.MOVING:
            if keys[pygame.K_LEFT]:
                self.pos.x -= self.velocity.x * dt
                if self.pos.x < 0 + self.LEFT_STOP_MOVEMENT_OFFSET:
                    self.pos.x = 0 + self.LEFT_STOP_MOVEMENT_OFFSET
            if keys[pygame.K_RIGHT]:
                self.pos.x += self.velocity.x * dt
                if self.pos.x + self.rect.width > self.screen_width:
                    self.pos.x = self.screen_width - self.rect.width

        self.rect.topleft = self.pos
