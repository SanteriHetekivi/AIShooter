from __future__ import annotations

import pygame

from .Cords import Cords
from .Movement import Movement


class Shooter():
    """Shooter character for the game.
    """

    def __init__(self: Shooter, scale: Cords, x: float = 0.00, y: float = 0.00, speed: float = 1000.00) -> Shooter:
        """Initialize shooter character.

        Args:
            self (Shooter): Itself.
            scale (Cords): Scale.
            x (float, optional): Staring X coordinate. Defaults to 0.00.
            y (float, optional): Staring Y coordinate. Defaults to 0.00.
            speed (float, optional): Speed of the charather. Defaults to 1000.00.

        Returns:
            Shooter: Itself.
        """
        self.cords = Cords(x, y)
        self.rect = pygame.Rect(
            self.cords.x, self.cords.y,
            scale.x*10, scale.y*10
        )
        self.movement = Movement()
        self.speed = speed

    def update_location(self: Shooter, time_diff: float, screen_rect: pygame.Rect) -> Shooter:
        """Update location.

        Args:
            self (Shooter): Itself.
            time_diff (float): Time difference.
            screen_rect (pygame.Rect): Screen rectancle.

        Returns:
            Shooter: Itself.
        """
        self.cords = self.movement.update_cords(
            self.cords,
            time_diff*self.speed,
            Cords(0, 0),
            Cords(
                screen_rect.width,
                screen_rect.height
            )
        )
        self.rect.x = self.cords.x
        self.rect.y = self.cords.y
        self.rect.clamp_ip(screen_rect)
        return self

    def frame(self: Shooter, time_diff: float, surface: pygame.Surface) -> Shooter:
        """Proccess frame.

        Args:
            self (Shooter): Itself.
            time_diff (float): Time difference.
            surface (pygame.Surface): Game surface.

        Returns:
            Shooter: Itself.
        """
        self.update_location(time_diff, surface.get_rect())
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
        return self
