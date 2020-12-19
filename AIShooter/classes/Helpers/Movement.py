from __future__ import annotations

from typing import Optional

from .Cords import Cords


class Movement():
    """Class for handeling movement.
    """

    def __init__(self: Movement) -> Movement:
        """Initialize movement.

        Args:
            self (Movement): Itself.

        Returns:
            Movement: Itself.
        """
        self.clear()

    def clear(self: Movement) -> Movement:
        """Clear movement.

        Args:
            self (Movement): Itself.

        Returns:
            Movement: Itself.
        """
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        return self

    def cords(self: Movement) -> Cords:
        """Get movement cordinates.

        Args:
            self (Movement): Itself.

        Returns:
            Cords: Movement cordinates.
        """
        cords = Cords()
        if self.left:
            cords.x -= 1
        if self.right:
            cords.x += 1
        if self.up:
            cords.y -= 1
        if self.down:
            cords.y += 1
        return cords

    def update_cords(self: Movement, cords: Cords, factor: float = 1.00, cords_min: Optional[Cords] = None, cords_max: Optional[Cords] = None) -> Cords:
        """Update given cordinates with movement cordinates.

        Args:
            self (Movement): Itself.
            cords (Cords): Cordinates to update.
            factor (float, optional): Multiply movement cordinates with this. Defaults to 1.00.
            cords_min (Optional[Cords], optional): If given clamp cordinates to this minimum. Defaults to None.
            cords_max (Optional[Cords], optional): If given clamp cordinates to this maximum. Defaults to None.

        Returns:
            Cords: Updated cordinates.
        """
        movement_cords = self.cords()
        if(movement_cords.empty()):
            return cords
        movement_cords.factor(factor)
        cords.x += movement_cords.x
        cords.y += movement_cords.y
        cords.clamp(
            cords_min,
            cords_max
        )
        return cords
