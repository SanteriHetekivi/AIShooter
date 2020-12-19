from __future__ import annotations

# Packages
import pygame

# Helpers
from ..Helpers.Cords import Cords
from ..Helpers.Movement import Movement

# Elements
from .Position import Position


class Moving(Position):
    def __init__(self: Moving, x: float = 0.00, y: float = 0.00, speed: float = 1000.00, color: pygame.Color = pygame.Color(255, 255, 255)) -> Moving:
        """Initialize game element.

        Args:
            self (Moving): Itself.
            x (float, optional): Start X-cordinate. Defaults to 0.00.
            y (float, optional): Start Y-cordinate. Defaults to 0.00.
            speed (float, optional): Starting speed. Defaults to 1000.00.
            color (pygame.Color, optional): Color of the element. Defaults to pygame.Color(255, 255, 255).

        Returns:
            Moving: Itself.
        """
        self._movement = Movement()
        self._speed = speed
        Position.__init__(
            self,
            x,
            y,
            color
        )

    def _update_location(self: Moving, time_diff: float, screen_rect: pygame.Rect) -> Moving:
        """Update location.

        Args:
            self (Moving): Itself.
            time_diff (float): Time difference.
            screen_rect (pygame.Rect): Screen rectancle.

        Returns:
            Moving: Itself.
        """

        # Get cordinates from movement.
        raw_cords = self._movement.update_cords(
            self._cords,
            time_diff*self._speed,
        )

        # Clamp cordinates to screen rect.
        self._cords = raw_cords.__copy__().clamp(
            Cords(0, 0),
            Cords(
                screen_rect.width,
                screen_rect.height
            )
        )

        # If went outside screen set not alive.
        if not self._cords.same(raw_cords):
            self.die()

        return self

    def _frame(self: Moving, time_diff: float, events: list, surface: pygame.Surface, scale: Cords) -> Moving:
        """Handle frame.

        Args:
            self (Moving): Itself.
            time_diff (float): Time difference.
            events (list): Event list.
            surface (pygame.Surface): Game surface.
            scale (Cords): Scale of the drawing.

        Returns:
            Moving: Itself.
        """

        self._update_location(time_diff, surface.get_rect())
        return Position._frame(
            self,
            time_diff,
            events,
            surface,
            scale
        )
