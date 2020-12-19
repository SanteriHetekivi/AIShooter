from __future__ import annotations

# Packages
import pygame

# Exceptions
from ..Exceptions.End import End

# Helpers
from ..Helpers.Cords import Cords

# Elements
from .Element import Element


class Screen(Element):

    def _draw(self: Screen, surface: pygame.Surface, scale: Cords) -> Screen:
        """Draw element to given surface.

        Args:
            self (Screen): Itself.
            surface (pygame.Surface): Surface to draw on.
            scale (Cords): Scale of the drawing.

        Returns:
            Screen: Itself.
        """

        # Fill background.
        surface.fill((0, 0, 0))

        return self

    def _frame(self: Screen, time_diff: float, events: list, surface: pygame.Surface, scale: Cords) -> Screen:
        """Handle frame.

        Args:
            self (Screen): Itself.
            time_diff (float): Time difference.
            events (list): Event list.
            surface (pygame.Surface): Game surface.
            scale (Cords): Scale of the drawing.

        Returns:
            Screen: Itself.
        """

        # Handle events.
        for event in events:
            # Game was quited.
            if event.type == pygame.QUIT:
                raise End("pygame.QUIT event")

        # Kill children if they are inside any other hitbox.
        self.check_hitboxes(
            self.hitboxes(scale),
            scale
        )

        # Retun self.
        return Element._frame(
            self,
            time_diff,
            events,
            surface,
            scale
        )
