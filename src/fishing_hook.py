from enum import Enum
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_state import GameState


class HookState(Enum):
    IDLE = "idle"
    DROPPING = "dropping"
    REELING = "reeling"


class FishingHook(pygame.sprite.Sprite):

    def __init__(self, start_pos, hook_sprite, screen_height):
        super().__init__()
        self.MOVEMENT_SPEED = {"dropping": 100, "reeling": 250}
        self._state = HookState.IDLE
        self.screen_height = screen_height
        self.velocity = pygame.math.Vector2(0, 0)

        self.image = hook_sprite
        self.pos: pygame.math.Vector2 = pygame.math.Vector2(*start_pos)
        self.rect: pygame.Rect = self.image.get_rect(midtop=(self.pos.x, self.pos.y))

        self.TOP_STOP_MOVEMENT_OFFSET = self.pos.y
        self.BOTTOM_STOP_MOVEMENT_OFFSET = 35

        self._spacebar_pressed = False
        self.caught_fish = None

    def drop(self):
        self._state = HookState.DROPPING
        self.velocity = pygame.math.Vector2(0, self.MOVEMENT_SPEED["dropping"])

    def reel(self):
        self._state = HookState.REELING
        self.velocity = pygame.math.Vector2(0, self.MOVEMENT_SPEED["reeling"])

    def idle(self):
        self._state = HookState.IDLE
        self.velocity = pygame.math.Vector2(0, 0)

    def update(
        self, dt, keys, player_pos: pygame.math.Vector2, fish_group: pygame.sprite.Group, game_state: "GameState"
    ):
        # Detect spacebar press to 'debounce'
        if keys[pygame.K_SPACE]:
            if not self._spacebar_pressed:
                self._spacebar_pressed = True
                if self._state == HookState.IDLE:
                    self.drop()
                elif self._state == HookState.DROPPING:
                    self.reel()
        else:
            self._spacebar_pressed = False

        # Check for collision with fish
        if self.caught_fish is None:
            collided_fish = pygame.sprite.spritecollideany(self, fish_group)
            if collided_fish:
                self.caught_fish = collided_fish
                self.reel()

        if self._state == HookState.DROPPING:
            self.pos.y += self.velocity.y * dt

            # check to see if it hits the bottom
            if self.pos.y > self.screen_height - self.BOTTOM_STOP_MOVEMENT_OFFSET:
                self.pos.y = self.screen_height - self.BOTTOM_STOP_MOVEMENT_OFFSET
                self.reel()

        elif self._state == HookState.REELING:
            self.pos.y -= self.velocity.y * dt

            # check to see if it gets back to the fishing pole
            if self.pos.y <= self.TOP_STOP_MOVEMENT_OFFSET:
                self.pos.y = self.TOP_STOP_MOVEMENT_OFFSET
                self.idle()

        # kill any fish that they catch
        if self.caught_fish and self._state == HookState.IDLE:
            game_state.fish_caught()
            self.caught_fish.kill()
            self.caught_fish = None

        # Align the hook with the fishing pole
        self.pos.x = player_pos.x

        self.rect.midtop = self.pos  # need to update rect pos
