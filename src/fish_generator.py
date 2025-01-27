import pygame
from fish import Fish
import random
from typing import Literal


class FishGenerator:

    def __init__(
        self,
        screen: pygame.Surface,
        min_y_spawn_limit: int,
        max_y_spawn_limit: int,
        spawn_interval_min: int,
        spawn_interval_max: int,
        max_fish_to_be_generated: int,
        fish_on_screen: pygame.sprite.Group,
        min_fish_speed: int,
        max_fish_speed: int,
        fish_sprite: pygame.Surface,
    ) -> None:
        pass
        self.fish_sprite = fish_sprite

        # height of screen
        self.screen = screen

        # upper and lower screen bounds of where to spawn the fish
        self.MIN_Y_SPAWN_LIMIT = min_y_spawn_limit
        self.MAX_Y_SPAWN_LIMIT = max_y_spawn_limit

        # max and min spawn interval
        self.SPAWN_INTERVAL_MIN_TIME = spawn_interval_min
        self.SPAWN_INTERVAL_MAX_TIME = spawn_interval_max

        # max fish generated at a time
        self.MAX_FISH_ON_SCREEN = max_fish_to_be_generated

        # group of current fish on screen
        # reference to what is in the main state group
        self.current_fish_on_screen: pygame.sprite.Group = fish_on_screen

        # range of speed of the fish
        self.max_fish_speed = max_fish_speed
        self.min_fish_speed = min_fish_speed

        # toggle for what side it will come from next spawn
        self.fish_facing: Literal["left", "right"] = "left"

        # time of last spawned fish
        self.last_spawned_fish_time = pygame.time.get_ticks()

        # the current interval between spawns
        self.current_spawn_time_interval = self.SPAWN_INTERVAL_MAX_TIME

        # off screen buffers left and right
        self.SPAWN_SCREEN_OFFSET = 100

    def spawn_fish(self):

        now = pygame.time.get_ticks()
        if (now - self.last_spawned_fish_time > self.current_spawn_time_interval) and (
            len(self.current_fish_on_screen) < self.MAX_FISH_ON_SCREEN
        ):

            # calculate spawn location and side
            y_spawn_pos = random.randint(self.MIN_Y_SPAWN_LIMIT, self.MAX_Y_SPAWN_LIMIT)
            if self.fish_facing == "left":
                x_spawn_pos = self.screen.get_width() + self.SPAWN_SCREEN_OFFSET
            else:  # facing right
                x_spawn_pos = -self.SPAWN_SCREEN_OFFSET

            # calculate movement speed
            speed = random.randint(self.min_fish_speed, self.max_fish_speed)

            fish = Fish((x_spawn_pos, y_spawn_pos), self.fish_sprite, self.fish_facing, speed, self.screen)

            # toggle to other side for next spawn
            self._toggle_fish_facing()

            # reset the time keeping
            self.last_spawned_fish_time = pygame.time.get_ticks()
            self.current_spawn_time_interval = random.randint(
                self.SPAWN_INTERVAL_MIN_TIME, self.SPAWN_INTERVAL_MAX_TIME
            )

            return fish

        return None

    def _toggle_fish_facing(self):
        if self.fish_facing == "left":
            self.fish_facing = "right"
        else:
            self.fish_facing = "left"
