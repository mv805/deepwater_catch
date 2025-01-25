from typing import Dict
import pygame
import json
import re

# generate a surface
# load an image onto the surface
# get coordicates and for collision use Rect
# a sprite used in sprite groups is surface with image and rect


def load_sprites() -> Dict[str, pygame.Surface]:
    """
    Load sprites from a sprite sheet and metadata JSON file.
    This function loads a sprite sheet image and its corresponding metadata
    from a JSON file. It extracts individual sprites from the sprite sheet
    based on the metadata and stores them in a dictionary with their names
    as keys.
    Returns:
        Dict[str, pygame.Surface]: A dictionary where the keys are sprite names
        and the values are pygame.Surface objects representing the sprites.
    """

    sprite_sheet = pygame.image.load("./art/sprite_sheet.png").convert_alpha()
    # returns a pygame surface with transperancy

    # Dictionary to hold sprites by name
    sprites = {}

    # Load the JSON metadata
    with open("./art/sprite_sheet.json", "r") as f:
        metadata = json.load(f)

    def get_sprite_from_metadata(sprite_sheet: pygame.Surface, frame_data: Dict[str, int]) -> pygame.Surface:
        """Extract a single sprite from the sprite sheet using frame
        metadata from the json file that comes with the
        exported sprite sheet."""
        x, y, w, h = frame_data["x"], frame_data["y"], frame_data["w"], frame_data["h"]
        sprite = pygame.Surface((w, h), pygame.SRCALPHA)  # Create a new transparent surface
        sprite.blit(sprite_sheet, (0, 0), (x, y, w, h))  # Copy the sprite area from the sheet
        return sprite

    for sprite_name, data in metadata["frames"].items():
        # need to pull data from the sprite json

        # 'frame' is-
        #  "x":  The x-coordinate of the top-left corner of the sprite within the     sprite sheet.
        # "y": The y-coordinate of the top-left corner of the sprite within the sprite sheet.
        # "w": The width of the sprite.
        # "h":  The height of the sprite.

        frame_data = data["frame"]
        # pulls dict from the data like "frame": { "x": 0, "y": 0, "w": 700, "h": 130 },

        frame_data = data["frame"]
        # Extract the object name and convert to lowercase for easier reference
        sprite_object_name = re.sub(r".* \((.*)\)\.aseprite", r"\1", sprite_name).lower()
        sprites[sprite_object_name] = get_sprite_from_metadata(sprite_sheet, frame_data)

    return sprites


if __name__ == "__main__":

    class TestSprite(pygame.sprite.Sprite):
        def __init__(self, image: pygame.Surface, *groups):
            super().__init__()
            self.image = image
            self.rect: pygame.Rect = self.image.get_rect()
            self.MOVE_SPEED = 300

        def update(self, dt):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                test_sprite_boat.rect.x -= self.MOVE_SPEED * dt
            if keys[pygame.K_RIGHT]:
                test_sprite_boat.rect.x += self.MOVE_SPEED * dt
            if keys[pygame.K_UP]:
                test_sprite_boat.rect.y -= self.MOVE_SPEED * dt
            if keys[pygame.K_DOWN]:
                test_sprite_boat.rect.y += self.MOVE_SPEED * dt

    pygame.init()
    screen = pygame.display.set_mode((700, 400))  # need to set minimal display for test
    sprites = load_sprites()
    clock = pygame.time.Clock()

    print(sprites)

    test_sprite_boat = TestSprite(sprites["boat"])
    test_sprite_boat.rect.center = (350, 200)  # Center the sprite on the screen
    all_sprites = pygame.sprite.Group(test_sprite_boat)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60) / 1000  # Amount of seconds between each loop

        all_sprites.update(dt)

        # Clear the screen and redraw everything
        screen.fill((0, 0, 0))  # Clear the screen with black
        all_sprites.draw(screen)  # Draw the sprites
        pygame.display.flip()  # Update the display

    pygame.quit()
