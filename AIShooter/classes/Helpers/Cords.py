from __future__ import annotations

# Packages
from typing import Optional


class Cords():
    """Class for storing x and y cordinates.
    """

    def __init__(self: Cords, x: float = 0, y: float = 0) -> Cords:
        """Initialize cordinates.

        Args:
            self (Cords): Itself.
            x (float, optional): X cordinate. Defaults to 0.
            y (float, optional): Y cordinate. Defaults to 0.

        Returns:
            Cords: Itself.
        """
        self.x = x
        self.y = y

    def X(self: Cords) -> float:
        return self.x

    def factor(self: Cords, factor: float) -> Cords:
        """Multiply cordinates with given factor.

        Args:
            self (Cords): Itself.
            factor (float): Factor to multiply with.

        Returns:
            Cords: Itself.
        """
        self.x *= factor
        self.y *= factor
        return self

    def clamp(self: Cords, cords_min: Optional[Cords] = None, cords_max: Optional[Cords] = None) -> Cords:
        """Clamp cordinates.

        Args:
            self (Cords): Itself.
            cords_min (Optional[Cords], optional): If given this is minimum. Defaults to None.
            cords_max (Optional[Cords], optional): If given this is maximum. Defaults to None.

        Returns:
            Cords: Itself.
        """
        if cords_max is not None:
            self.x = min(self.x, cords_max.x)
            self.y = min(self.y, cords_max.y)
        if cords_min is not None:
            self.x = max(self.x, cords_min.x)
            self.y = max(self.y, cords_min.y)
        return self

    def empty(self: Cords) -> bool:
        """Are cordinates empty.

        Args:
            self (Cords): Itself.

        Returns:
            bool: Are cordinates empty.
        """
        return (self.x == 0 and self.y == 0)

    def __copy__(self: Cords) -> Cords:
        """Copy cordinates.

        Args:
            self (Cords): Itself.

        Returns:
            Cords: Copy.
        """
        return Cords(self.x, self.y)

    def same(self: Cords, cords: Cords) -> bool:
        """Self and given cordinates are same?

        Args:
            self (Cords): Itself.
            cords (Cords): Comparison.

        Returns:
            bool: Self and given cordinates are same?
        """
        return (
            self.x == cords.x
            and
            self.y == cords.y
        )
