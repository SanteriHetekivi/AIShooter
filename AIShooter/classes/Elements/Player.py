from __future__ import annotations

import pygame

from .Shooter import Shooter
from ..Helpers.Cords import Cords


class Player(Shooter):
    """Player charather.
    """

    def frame(self: Player, time_diff: float, events: list, surface: pygame.Surface, scale: Cords) -> Player:
        """Proccess frame.

        Args:
            self (Player): Itself.
            time_diff (float): Time difference.
            events (list): Event list.
            surface (pygame.Surface): Game surface.
            scale (Cords): Scale of the drawing.

        Returns:
            Player: Itself.
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    self._movement.left = True
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self._movement.right = True
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self._movement.up = True
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    self._movement.down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    self._movement.left = False
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self._movement.right = False
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self._movement.up = False
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    self._movement.down = False
        return Shooter._frame(self, time_diff, surface, scale)
