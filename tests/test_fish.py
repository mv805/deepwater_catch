import unittest
from unittest.mock import Mock
import pygame
from app.fishing_hook import FishingHook
from app.fish import Fish
from tests.params_testing import TestParams


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DEFAULT_FISH_SPEED = 50
HOOK_START_POS = (260, 200)


class TestFishMovementAndCollision(unittest.TestCase):

    def setUp(self):
        self.fish_sprite = pygame.Surface((TestParams.FISH_SPRITE.width, TestParams.FISH_SPRITE.height))  # Dummy sprite
        self.hook = Mock(spec=FishingHook)
        self.hook.pos = pygame.math.Vector2(*HOOK_START_POS)
        # Assign the hook a valid rect with dimensions 13x22 (from sprite_sheet.json)
        self.hook.rect = pygame.Rect(0, 0, TestParams.HOOK_SPRITE.width, TestParams.HOOK_SPRITE.height)
        self.hook.rect.center = (self.hook.pos.x, self.hook.pos.y)

    def test_left_movement(self):
        # establish a fish moving left
        fish = Fish((100, 100), self.fish_sprite, "left", DEFAULT_FISH_SPEED)
        # save original position for comparisons
        initial_x = fish.pos.x
        # utilize the fish update method as would be done from the gamestate
        fish.update(1.0, self.hook)
        # the position should be moved left after one tick or update iteration
        self.assertLess(fish.pos.x, initial_x)

    def test_right_movement(self):
        # establish a fish moving left
        fish = Fish((100, 100), self.fish_sprite, "right", DEFAULT_FISH_SPEED)
        # save original position for comparisons
        initial_x = fish.pos.x
        # utilize the fish update method as would be done from the gamestate
        fish.update(1.0, self.hook)
        # the position should be moved right after one tick or update iteration
        self.assertGreater(fish.pos.x, initial_x)

    def test_hook_collision_from_left(self):
        # Create a fish instance with an initial position away from the hook
        fish = Fish((200, 200), self.fish_sprite, "right", DEFAULT_FISH_SPEED)

        # no collision because the fish's rect does not overlap the hook's
        self.assertNotEqual(fish.pos, self.hook.pos)

        # Update the fish so that collide_rect now checks real overlap
        fish.update(1.0, self.hook)

        # After a collision, the fish should have zero velocity and be on the hook.
        self.assertEqual(fish.velocity.x, 0)
        self.assertEqual(fish.pos, self.hook.rect.center)

        # make sure it doesnt move after a tick
        fish.update(1.0, self.hook)
        self.assertEqual(fish.velocity.x, 0)
        self.assertEqual(fish.pos, self.hook.rect.center)

        # if the hook moves, the fish should go with it
        self.hook.pos = pygame.math.Vector2(*HOOK_START_POS)
        self.hook.rect.center = (self.hook.pos.x, self.hook.pos.y)

        fish.update(1.0, self.hook)
        self.assertEqual(fish.velocity.x, 0)
        self.assertEqual(fish.pos, self.hook.rect.center)


class TestFishInitialization(unittest.TestCase):

    def test_invalid_movement_speed(self):
        self.screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        # Using a dummy sprite for the test.
        dummy_sprite = pygame.Surface((TestParams.FISH_SPRITE.width, TestParams.FISH_SPRITE.height))
        with self.assertRaises(ValueError) as context:
            Fish((100, 100), dummy_sprite, "right", 0)
        self.assertEqual(str(context.exception), "movement_speed must be > 0")


if __name__ == "__main__":
    unittest.main()
