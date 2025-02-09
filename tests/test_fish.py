import unittest
from unittest.mock import Mock
import pygame
from app.fishing_hook import FishingHook
from app.fish import Fish


# Tests check the following:
#   movement left or right depending on facing
#   no movement past boundaries of screen
#   if collision with a hook, now being caught (no velocity and psotion at the  hook position)
class TestFish(unittest.TestCase):
    def setUp(self):
        self.screen = Mock()
        self.screen.get_width.return_value = 800
        self.fish_sprite = pygame.Surface((50, 50))  # Dummy sprite
        self.hook = Mock(spec=FishingHook)
        self.hook.pos = pygame.math.Vector2(260, 200)
        # Assign the hook a valid rect with dimensions 13x22 (from sprite_sheet.json)
        self.hook.rect = pygame.Rect(0, 0, 13, 22)
        self.hook.rect.center = (self.hook.pos.x, self.hook.pos.y)

    def test_left_movement(self):
        # establish a fish moving left
        fish = Fish((100, 100), self.fish_sprite, "left", 50, self.screen)
        # save original position for comparisons
        initial_x = fish.pos.x
        # utilize the fish update method as would be done from the gamestate
        fish.update(1.0, self.hook, self.screen)
        # the position should be moved left after one tick or update iteration
        self.assertLess(fish.pos.x, initial_x)

    # @patch("pygame.sprite.collide_rect", return_value=False)
    def test_right_movement(self):
        # establish a fish moving left
        fish = Fish((100, 100), self.fish_sprite, "right", 50, self.screen)
        # save original position for comparisons
        initial_x = fish.pos.x
        # utilize the fish update method as would be done from the gamestate
        fish.update(1.0, self.hook, self.screen)
        # the position should be moved right after one tick or update iteration
        self.assertGreater(fish.pos.x, initial_x)

    def test_boundary_right(self):
        fish = Fish((799, 100), self.fish_sprite, "right", 50, self.screen)
        fish_group = pygame.sprite.Group()
        fish_group.add(fish)
        self.assertTrue(fish.alive())
        # two ticks of movement
        fish.update(1.0, self.hook, self.screen)
        fish.update(1.0, self.hook, self.screen)
        self.assertFalse(fish.alive())

    def test_boundary_left(self):
        # Create a fish moving left; start close enough to left edge so it goes off
        fish = Fish((1, 100), self.fish_sprite, "left", 50, self.screen)
        fish_group = pygame.sprite.Group()
        fish_group.add(fish)
        self.assertTrue(fish.alive())
        # two ticks of movement
        fish.update(1.0, self.hook, self.screen)
        fish.update(1.0, self.hook, self.screen)
        self.assertFalse(fish.alive())

    def test_hook_collision_from_left(self):
        # Create a fish instance with an initial position away from the hook
        fish = Fish((200, 200), self.fish_sprite, "right", 50, self.screen)

        # first update: no collision because the fish's rect does not overlap the hook's
        self.assertNotEqual(fish.pos, self.hook.pos)

        # Update the fish so that collide_rect now checks real overlap
        fish.update(1.0, self.hook, self.screen)

        # After a collision, the fish should have zero velocity and be on the hook.
        self.assertEqual(fish.velocity.x, 0)
        self.assertEqual(fish.pos, self.hook.rect.center)

        # make sure it doesnt move after a tick
        fish.update(1.0, self.hook, self.screen)
        self.assertEqual(fish.velocity.x, 0)
        self.assertEqual(fish.pos, self.hook.rect.center)

        # if the hook moves, the fish should go with it
        self.hook.pos = pygame.math.Vector2(260, 100)
        self.hook.rect.center = (self.hook.pos.x, self.hook.pos.y)

        fish.update(1.0, self.hook, self.screen)
        self.assertEqual(fish.velocity.x, 0)
        self.assertEqual(fish.pos, self.hook.rect.center)


if __name__ == "__main__":
    unittest.main()
