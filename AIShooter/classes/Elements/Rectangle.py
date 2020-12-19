from __future__ import annotations

# Packages
from typing import Optional
import pygame

# Helpers
from ..Helpers.Cords import Cords

# Elements
from .Moving import Moving


class Rectangle(Moving):
    def __init__(self: Rectangle, width: float, height: float, x: float = 0.00, y: float = 0.00, speed: float = 1000.00, color: pygame.Color = pygame.Color(255, 255, 255)) -> Rectangle:
        """Initialize Rectangle game element.

        Args:
            self (Rectangle): Itself.
            width (float): Width.
            height (float): Height.
            x (float, optional): Start X-cordinate. Defaults to 0.00.
            y (float, optional): Start Y-cordinate. Defaults to 0.00.
            speed (float, optional): Starting speed. Defaults to 1000.00.
            color (pygame.Color, optional): Color of the element. Defaults to pygame.Color(255, 255, 255).

        Returns:
            Rectangle: Itself.
        """
        Moving.__init__(self, x, y, speed, color)
        self._rect = pygame.Rect(
            0, 0,
            width, height
        )
        self._update_rect()

    def width(self: Rectangle) -> float:
        """Width of the element.

        Args:
            self (Rectangle): Itself.

        Returns:
            float: Width of the element.
        """
        return self._rect.width

    def height(self: Rectangle) -> float:
        """Height of the element.

        Args:
            self (Rectangle): Itself.

        Returns:
            float: Height of the element.
        """
        return self._rect.height

    def _update_rect(self: Rectangle, clamp_rect: Optional[pygame.Rect] = None) -> pygame.Rect:
        """Update the rect.

        Args:
            self (Rectangle): Itself.
            clamp_rect (Optional[pygame.Rect], optional): If given clamp to this. Defaults to None.

        Returns:
            pygame.Rect: Updated rect.
        """
        self._rect.center = (self._cords.x, self._cords.y)
        if clamp_rect is not None:
            self._rect.clamp_ip(clamp_rect)
        return self._rect

    def _scaled_rect(self: Rectangle, scale: Cords) -> pygame.Rect:
        """Scaled version of the rect.

        Args:
            self (Rectangle): Itself.
            scale (Cords): Scaling factors.

        Returns:
            pygame.Rect: Scaled version of the rect.
        """
        rect = self._rect.copy()
        rect.width *= scale.x
        rect.height *= scale.y
        return rect

    def _update_location(self: Rectangle, time_diff: float, screen_rect: pygame.Rect) -> Rectangle:
        """Update location.

        Args:
            self (Rectangle): Itself.
            time_diff (float): Time difference.
            screen_rect (pygame.Rect): Screen rectancle.

        Returns:
            Rectangle: Itself.
        """
        Moving._update_location(self, time_diff, screen_rect)
        self._update_rect(screen_rect)
        return self

    def max_radius(self: Rectangle, scale: Cords = Cords(1.00, 1.00)) -> float:
        """Max possible radius.

        Args:
            self (Rectangle): Itself.
            scale (Cords, optional): Scaling. Defaults to Cords(1.00, 1.00).

        Returns:
            float: Max possible radius.
        """
        rect = self._scaled_rect(scale)
        return max(rect.width, rect.height)/2

    def _draw(self: Rectangle, surface: pygame.Surface, scale: Cords) -> Rectangle:
        """Draw element to given surface.

        Args:
            self (Rectangle): Itself.
            surface (pygame.Surface): Surface to draw on.
            scale (Cords): Scale of the drawing.

        Returns:
            Rectangle: Itself.
        """
        Moving._draw(self, surface, scale)
        pygame.draw.rect(surface, self._color, self._scaled_rect(scale))
        return self
