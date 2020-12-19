from __future__ import annotations

# Packages
import pygame

# Helpers
from ..Helpers.Cords import Cords
from ..Helpers.Movement import Movement
from ..Helpers.Facing import Facing

# Elements
from .Circle import Circle


class Bullet(Circle):
    """Bullet game element.
    """

    def __init__(self: Bullet, start: Cords, movement: Movement) -> Bullet:
        """Initialize bullet element.

        Args:
            self (Bullet): Itself.
            start (Cords): Starting cordinates.
            facing (Movement): Movement.

        Returns:
            Bullet: Itself.
        """
        Circle.__init__(
            self,
            5, 0,
            start.x, start.y,
            500,
            pygame.Color(255, 0, 0)
        )
        self._movement = movement
