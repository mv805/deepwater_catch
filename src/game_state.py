import pygame
from typing import Tuple
from sprites import load_sprites
from game_colors import Colors
from player_controller import PlayerController
from fishing_hook import FishingHook
from fish_generator import FishGenerator


class GameState:

    def __init__(self, game_screen: pygame.Surface, player_pos: Tuple[int, int]):
        self.screen = game_screen

        self.fish_spawner_parameters = {
            "MAX_FISH": 10,
            "MIN_FISH_SPAWN_INTERVAL": 1 * 1000,
            "MAX_FISH_SPAWN_INTERVAL": 3 * 1000,
            "MIN_Y_POS": 100,
            "MAX_Y_POS": 350,
            "MIN_FISH_SPEED": 20,
            "MAX_FISH_SPEED": 300,
        }
        # load sprites
        self.game_sprites = load_sprites()
        self.player_sprite = self.game_sprites["Boat"]
        self.hook_sprite = self.game_sprites["Hook"]
        self.fish_sprite = self.game_sprites["Fish"]
        self.background = self.game_sprites["Background"]
        # create objects
        self.player = PlayerController(player_pos, self.player_sprite, self.screen.get_width())
        self.hook = FishingHook(player_pos, self.hook_sprite, game_screen.get_height())

        # Add player and hook to all_sprites
        self.all_sprites_group = pygame.sprite.Group()
        self.fish_sprites_group = pygame.sprite.Group()
        self.all_sprites_group.add(self.player)
        self.all_sprites_group.add(self.hook)

        self.fish_caught_count = 0
        self.FISH_COUNTER_POS = (5, 5)

        self.fish_generator = FishGenerator(
            screen=self.screen,
            min_y_spawn_limit=self.fish_spawner_parameters["MIN_Y_POS"],
            max_y_spawn_limit=self.fish_spawner_parameters["MAX_Y_POS"],
            spawn_interval_min=self.fish_spawner_parameters["MIN_FISH_SPAWN_INTERVAL"],
            spawn_interval_max=self.fish_spawner_parameters["MAX_FISH_SPAWN_INTERVAL"],
            max_fish_to_be_generated=self.fish_spawner_parameters["MAX_FISH"],
            fish_on_screen=self.fish_sprites_group,
            min_fish_speed=self.fish_spawner_parameters["MIN_FISH_SPEED"],
            max_fish_speed=self.fish_spawner_parameters["MAX_FISH_SPEED"],
            fish_sprite=self.game_sprites["Fish"],
        )

        pygame.font.init()
        self.font = pygame.font.Font(None, 20)  # None for default font, 36 for font size

    def update(self, keys, dt):
        self.player.update(dt, keys, self.hook.pos)
        self.hook.update(dt, keys, self.player.pos, self.fish_sprites_group, self)

        fish_to_spawn = self.fish_generator.spawn_fish()
        if fish_to_spawn:
            self.fish_sprites_group.add(fish_to_spawn)
            self.all_sprites_group.add(fish_to_spawn)

        self.fish_sprites_group.update(dt, self.hook, self.screen)

    def fish_caught(self):
        self.fish_caught_count += 1

    def draw_text(self, text, position):
        text_surface = self.font.render(text, True, Colors.HIGHLIGHT_TAN.value)
        self.screen.blit(text_surface, position)

    def draw(self):

        self.screen.blit(self.background, self.background.get_rect().topleft)

        # render all the sprites
        self.all_sprites_group.draw(self.screen)

        self.hook.draw(self.screen, self.player.pos)
        # draw score
        self.draw_text(f"Fish Caught: {self.fish_caught_count}", self.FISH_COUNTER_POS)
