from __future__ import annotations

# Helpers
from .Cords import Cords
from .Facing import Facing


class Movement(Facing):
    """Class for handeling movement.
    """

    def __init__(self: Movement, up: bool = False, down: bool = False, left: bool = False, right: bool = False) -> Movement:
        """Initialize movement.

        Args:
            self (Movement): Itself.
            up (bool, optional): Is default facing up. Defaults to False.
            down (bool, optional): Is default facing down. Defaults to False.
            left (bool, optional): Is default facing left. Defaults to False.
            right (bool, optional): Is default facing right. Defaults to False.

        Returns:
            Movement: Itself.
        """
        Facing.__init__(
            self,
            up,
            down,
            left,
            right
        )
        self.facing = Facing(
            up,
            down,
            left,
            right
        )

    @staticmethod
    def FromFacing(facing: Facing) -> Movement:
        """Create Movement from Facing.

        Args:
            facing (Facing): Create from this.

        Returns:
            Movement: Created Movement.
        """
        return Movement(
            facing.up,
            facing.down,
            facing.left,
            facing.right
        )

    def facing_as_movement(self: Movement) -> Movement:
        """Current facing as a Movement.

        Args:
            self (Movement): Itself.

        Returns:
            Movement: Current facing as a Movement.
        """
        return Movement.FromFacing(
            self.facing
        )

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

    def update_cords(self: Movement, cords: Cords, factor: float = 1.00) -> Cords:
        """Update given cordinates with movement cordinates.

        Args:
            self (Movement): Itself.
            cords (Cords): Cordinates to update.
            factor (float, optional): Multiply movement cordinates with this. Defaults to 1.00.

        Returns:
            Cords: Updated cordinates.
        """
        movement_cords = self.cords()
        if(movement_cords.empty()):
            return cords
        self.facing.set(
            self.up,
            self.down,
            self.left,
            self.right
        )
        movement_cords.factor(factor)
        cords.x += movement_cords.x
        cords.y += movement_cords.y
        return cords
