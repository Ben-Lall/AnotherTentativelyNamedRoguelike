from creature import Creature
from camera import Camera
from renderer import Renderer
from symbol import Symbol
from bearlibterminal import terminal as blt


class Player(Creature):
    """A controllable player character."""

    def __init__(self, pos, world_width, world_height):
        symbol = Symbol('@', blt.color_from_name("dark white"))
        super().__init__(pos[0], pos[1], symbol)
        self.camera = Camera(self.x, self.y, world_width, world_height)
        self.world_renderer = Renderer()

    def render_screen(self, world):
        """Render everything visible to this player to the screen."""
        self.world_renderer.transform(self.camera)
        world.render(self.camera, self.world_renderer)

    def move(self, dx, dy, world):
        """Move the player and pan the camera to compensate."""
        super().move(dx, dy, world)
        self.camera.move_to(self.x, self.y)
