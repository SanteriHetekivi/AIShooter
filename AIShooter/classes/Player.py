from __future__ import annotations

import pygame

from .Shooter import Shooter


class Player(Shooter):
    """Player charather.
    """

    def frame(self: Player, time_diff: float, events: list, surface: pygame.Surface) -> Player:
        """Proccess frame.

        Args:
            self (Player): Itself.
            time_diff (float): Time difference.
            events (list): Event list.
            surface (pygame.Surface): Game surface.

        Returns:
            Player: Itself.
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    self.movement.left = True
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self.movement.right = True
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self.movement.up = True
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    self.movement.down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    self.movement.left = False
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self.movement.right = False
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self.movement.up = False
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    self.movement.down = False
        return Shooter.frame(self, time_diff, surface)
