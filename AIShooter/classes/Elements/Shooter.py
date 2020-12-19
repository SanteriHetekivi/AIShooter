from __future__ import annotations

import pygame

from .Rectangle import Rectangle


class Shooter(Rectangle):
    """Shooter character for the game.
    """

    def __init__(self: Rectangle, x: float = 0.00, y: float = 0.00, speed: float = 1000.00, color: pygame.Color = pygame.Color(255, 255, 255)) -> Rectangle:
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
