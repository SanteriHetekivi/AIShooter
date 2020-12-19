from __future__ import annotations

# Packages
import pygame

# Helpers
from ..Helpers.Cords import Cords

# Elements
from .Rectangle import Rectangle
from .Bullet import Bullet


class Shooter(Rectangle):
    """Shooter character for the game.
    """

    def __init__(self: Rectangle, x: float = 0.00, y: float = 0.00, speed: float = 400.00, color: pygame.Color = pygame.Color(255, 255, 255)) -> Rectangle:
        """Initialize shooter character.

        Args:
            self (Shooter): Itself.
            x (float, optional): Start X-cordinate. Defaults to 0.00.
            y (float, optional): Start Y-cordinate. Defaults to 0.00.
            speed (float, optional): Starting speed. Defaults to 1000.00.
            color (pygame.Color, optional): Color of the element. Defaults to pygame.Color(255, 255, 255).

        Returns:
            Shooter: Itself.
        """
        Rectangle.__init__(self, 10, 10, x, y, speed, color)
        self._bullets = []

    def _shoot(self: Shooter, scale: Cords) -> Shooter:
        """Shoot bullet.

        Args:
            self (Shooter): Itself.
            scale (Cords): Scale.

        Returns:
            Shooter: Itself.
        """
        movement = self._movement.facing_as_movement()
        self.add_child(
            Bullet(
                movement.update_cords(
                    self._cords.__copy__(),
                    self.max_radius(scale)*5
                ),
                movement
            )
        )
        return self
