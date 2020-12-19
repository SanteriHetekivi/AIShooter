from __future__ import annotations

# Packages
import pygame

# Exceptions
from ..Exceptions.End import End

# Helpers
from ..Helpers.Cords import Cords

# Elements
from .Shooter import Shooter


class Player(Shooter):
    """Player charather.
    """

    def die(self: Player) -> None:
        """Mark player as dead.

        Args:
            self (Player): Itself.

        Returns:
            Player: Itself.
        """
        Shooter.die(self)
        raise End("You died!")

    def _frame(self: Player, time_diff: float, events: list, surface: pygame.Surface, scale: Cords) -> Player:
        """Handle frame.

        Args:
            self (Player): Itself.
            time_diff (float): Time difference.
            events (list): Event list.
            surface (pygame.Surface): Game surface.
            scale (Cords): Scale of the drawing.

        Returns:
            Player: Itself.
        """

        shoot = False
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
                if event.key == pygame.K_SPACE:
                    shoot = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    self._movement.left = False
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self._movement.right = False
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self._movement.up = False
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    self._movement.down = False
        Shooter._frame(self, time_diff, events, surface, scale)
        if shoot:
            self._shoot()
        return self
