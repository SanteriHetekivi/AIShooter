from __future__ import annotations

# Packages
import pygame

# Helpers
from ..Helpers.Cords import Cords

# Elements
from .Element import Element


class Position(Element):
    def __init__(self: Position, x: float = 0.00, y: float = 0.00, color: pygame.Color = pygame.Color(255, 255, 255)) -> Position:
        """Initialize game element.

        Args:
            self (Position): Itself.
            x (float, optional): Start X-cordinate. Defaults to 0.00.
            y (float, optional): Start Y-cordinate. Defaults to 0.00.
            speed (float, optional): Starting speed. Defaults to 1000.00.
            color (pygame.Color, optional): Color of the element. Defaults to pygame.Color(255, 255, 255).

        Returns:
            Position: Itself.
        """
        Element.__init__(
            self,
            color
        )
        self._cords = Cords(x, y)
        self._has_hitbox = True

    def width(self: Position) -> float:
        """Width of the element.

        Args:
            self (Position): Itself.

        Returns:
            float: Width of the element.
        """
        return 1.00

    def height(self: Position) -> float:
        """Height of the element.

        Args:
            self (Position): Itself.

        Returns:
            float: Height of the element.
        """
        return 1.00

    def hitbox(self: Position, scale: Cords) -> pygame.Rect:
        """Hitbox for element.

        Args:
            self (Position): Itself.
            scale (Cords): Scale.

        Returns:
            pygame.Rect: Hitbox for element.
        """
        rect = pygame.Rect(
            0, 0,
            self.width()*scale.x,
            self.height()+scale.y
        )
        rect.center = (
            self._cords.x,
            self._cords.y
        )
        return rect
