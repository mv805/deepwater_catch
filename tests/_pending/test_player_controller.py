# import unittest
# from unittest.mock import Mock
# import pygame
# from src.player_controller import PlayerController, PlayerState


# class TestPlayerController(unittest.TestCase):
#     def setUp(self):
#         self.boat_sprite = pygame.Surface((50, 50))
#         self.player = PlayerController(start_pos=(100, 10), boat_sprite=self.boat_sprite, screen_width=800)

#     def test_movement_bounds(self):
#         # Test left boundary
#         self.player.pos.x = 10
#         self.player.update(1.0, {pygame.K_LEFT: True}, Mock())
#         self.assertGreaterEqual(self.player.pos.x, 50)  # Boat width offset

#         # Test right boundary
#         self.player.pos.x = 780  # 800 - 20 (buffer)
#         self.player.update(1.0, {pygame.K_RIGHT: True}, Mock())
#         self.assertLessEqual(self.player.pos.x, 800 - 50)

#     def test_state_transitions(self):
#         # Test casting
#         self.player.update(1.0, {pygame.K_SPACE: True}, Mock())
#         self.assertEqual(self.player._state, PlayerState.CASTING)

#         # Test return to moving
#         self.player._state = PlayerState.CASTING
#         self.player.update(1.0, {}, pygame.math.Vector2(100, 10))
#         self.assertEqual(self.player._state, PlayerState.MOVING)
