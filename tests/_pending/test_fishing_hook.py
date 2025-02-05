# import unittest
# from unittest.mock import Mock
# import pygame
# from src.fishing_hook import FishingHook, HookState


# class TestFishingHook(unittest.TestCase):
#     def setUp(self):
#         self.hook_sprite = pygame.Surface((20, 20))
#         self.screen_height = 600
#         self.hook = FishingHook(start_pos=(400, 10), hook_sprite=self.hook_sprite, screen_height=self.screen_height)

#     def test_state_transitions(self):
#         # Test drop
#         self.hook.drop()
#         self.assertEqual(self.hook._state, HookState.DROPPING)

#         # Test reel
#         self.hook.reel()
#         self.assertEqual(self.hook._state, HookState.REELING)

#         # Test idle
#         self.hook.idle()
#         self.assertEqual(self.hook._state, HookState.IDLE)

#     def test_movement_limits(self):
#         # Test bottom boundary
#         self.hook.pos.y = self.screen_height - 30
#         self.hook.update(1.0, {}, Mock(), Mock(), Mock())
#         self.assertEqual(self.hook.pos.y, self.screen_height - 35)
#         self.assertEqual(self.hook._state, HookState.REELING)

#         # Test top boundary
#         self.hook.pos.y = 5
#         self.hook.update(1.0, {}, Mock(), Mock(), Mock())
#         self.assertEqual(self.hook.pos.y, 10)
# self.assertEqual(self.hook._state, HookState.IDLE)
