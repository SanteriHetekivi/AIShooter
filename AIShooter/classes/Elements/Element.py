from __future__ import annotations

import pygame

from ..Helpers.Cords import Cords
from ..Helpers.Movement import Movement


class Element():
    def __init__(self: Element, x: float = 0.00, y: float = 0.00, speed: float = 1000.00, color: pygame.Color = pygame.Color(255, 255, 255)) -> Element:
        """Initialize game element.

        Args:
            self (Element): Itself.
            x (float, optional): Start X-cordinate. Defaults to 0.00.
            y (float, optional): Start Y-cordinate. Defaults to 0.00.
            speed (float, optional): Starting speed. Defaults to 1000.00.
            color (pygame.Color, optional): Color of the element. Defaults to pygame.Color(255, 255, 255).

        Returns:
            Element: Itself.
        """
        self._cords = Cords(x, y)
        self._movement = Movement()
        self._speed = speed
        self._color = color

    def _update_location(self: Element, time_diff: float, screen_rect: pygame.Rect) -> Element:
        """Update location.

        Args:
            self (Element): Itself.
            time_diff (float): Time difference.
            screen_rect (pygame.Rect): Screen rectancle.

        Returns:
            Element: Itself.
        """
        self._cords = self._movement.update_cords(
            self._cords,
            time_diff*self._speed,
            Cords(0, 0),
            Cords(
                screen_rect.width,
                screen_rect.height
            )
        )
        return self

    def _draw(self: Element, surface: pygame.Surface, scale: Cords) -> Element:
        """Draw element to given surface.

        Args:
            self (Element): Itself.
            surface (pygame.Surface): Surface to draw on.
            scale (Cords): Scale of the drawing.

        Returns:
            Element: Itself.
        """
        return self

    def _frame(self: Element, time_diff: float, surface: pygame.Surface, scale: Cords) -> Element:
        """Proccess frame.

        Args:
            self (Element): Itself.
            time_diff (float): Time difference.
            surface (pygame.Surface): Game surface.
            scale (Cords): Scale of the drawing.

        Returns:
            Element: Itself.
        """
        self._update_location(time_diff, surface.get_rect())
        self._draw(surface, scale)
        return self
