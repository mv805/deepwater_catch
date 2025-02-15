from abc import ABC, abstractmethod


class State(ABC):
    def enter(self, *args, **kwargs):
        """Called when entering the state"""
        pass

    def exit(self, *args, **kwargs):
        """Called when exiting the state"""
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        """Called to update the state"""
        pass


class StateMachine:
    def __init__(self, sprite):
        self.sprite = sprite
        self.current_state = None

    def transition_to(self, state, *args, **kwargs):
        """Transition to a new state"""
        if self.current_state:
            self.current_state.exit(self.sprite, *args, **kwargs)
        self.current_state = state
        self.current_state.enter(self.sprite, *args, **kwargs)

    def update(self, *args, **kwargs):
        """Update the current state"""
        if self.current_state:
            self.current_state.update(self.sprite, *args, **kwargs)
