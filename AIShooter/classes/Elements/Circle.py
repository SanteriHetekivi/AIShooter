from __future__ import annotations

# Packages
import pygame

# Helpers
from ..Helpers.Cords import Cords

# Elements
from .Moving import Moving


class Circle(Moving):
    def __init__(self: Circle, radius: float, width: float = 0, x: float = 0.00, y: float = 0.00, speed: float = 1000.00, color: pygame.Color = pygame.Color(255, 255, 255)) -> Circle:
        """Cirle element.

        Args:
            self (Circle): Itself.
            radius (float): Radius of the cirle.
            width (float, optional): Width of the line (0 == fill). Defaults to 0.
            x (float, optional): Start X-cordinate. Defaults to 0.00.
            y (float, optional): Start Y-cordinate. Defaults to 0.00.
            speed (float, optional): Starting speed. Defaults to 1000.00.
            color (pygame.Color, optional): Color of the element. Defaults to pygame.Color(255, 255, 255).

        Returns:
            Circle: Itself.
        """
        Moving.__init__(self, x, y, speed, color)
        self._radius = radius
        self._width = width

    def diameter(self: Circle) -> float:
        """Diameter of the circle.

        Args:
            self (Circle): Itself.

        Returns:
            float: Diameter of the circle.
        """
        return self._radius*2

    def width(self: Circle) -> float:
        """Width of the element.

        Args:
            self (Circle): Itself.

        Returns:
            float: Width of the element.
        """
        return self.diameter()

    def height(self: Circle) -> float:
        """Height of the element.

        Args:
            self (Circle): Itself.

        Returns:
            float: Height of the element.
        """
        return self.diameter()

    def _draw(self: Circle, surface: pygame.Surface, scale: Cords) -> Circle:
        """Draw element to given surface.

        Args:
            self (Circle): Itself.
            surface (pygame.Surface): Surface to draw on.
            scale (Cords): Scale of the drawing.

        Returns:
            Circle: Itself.
        """
        Moving._draw(self, surface, scale)
        scale_float = min(
            scale.x,
            scale.y
        )
        pygame.draw.circle(
            surface,
            self._color,
            (
                self._cords.x,
                self._cords.y
            ),
            int(round(self._radius*scale_float)),
            int(round(self._width*scale_float))
        )
        return self
