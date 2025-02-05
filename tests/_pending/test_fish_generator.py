# import unittest
# from unittest.mock import Mock, patch
# import pygame
# from src.fish_generator import FishGenerator


# class TestFishGenerator(unittest.TestCase):
#     def setUp(self):
#         self.screen = Mock()
#         self.screen.get_width.return_value = 800
#         self.fish_group = Mock()
#         self.fish_sprite = pygame.Surface((50, 50))

#     @patch("pygame.time.get_ticks")
#     @patch("random.randint")
#     def test_spawn_logic(self, mock_randint, mock_ticks):
#         # Setup consistent random values
#         mock_randint.side_effect = [300, 150]  # y_pos, speed
#         mock_ticks.return_value = 5000

#         generator = FishGenerator(
#             screen=self.screen,
#             min_y_spawn_limit=100,
#             max_y_spawn_limit=400,
#             spawn_interval_min=1000,
#             spawn_interval_max=3000,
#             max_fish_to_be_generated=5,
#             fish_on_screen=self.fish_group,
#             min_fish_speed=100,
#             max_fish_speed=200,
#             fish_sprite=self.fish_sprite,
#         )

#         # First spawn
#         fish = generator.spawn_fish()
#         self.assertIsNotNone(fish)
#         # self.assertEqual(fish.velocity.x, -150)  # Initial facing left

#         # Verify toggle
#         self.assertEqual(generator.fish_facing, "right")

#     def test_spawn_limits(self):
#         generator = FishGenerator(
#             screen=self.screen,
#             min_y_spawn_limit=100,
#             max_y_spawn_limit=400,
#             spawn_interval_min=1000,
#             spawn_interval_max=3000,
#             max_fish_to_be_generated=2,
#             fish_on_screen=Mock(),
#             min_fish_speed=100,
#             max_fish_speed=200,
#             fish_sprite=self.fish_sprite,
#         )

#         with patch.object(generator, "current_fish_on_screen") as mock_group:
#             mock_group.__len__.return_value = 3  # Over limit
#             self.assertIsNone(generator.spawn_fish())
