from __future__ import annotations


class Facing():
    """Class for handeling facing.
    """

    def __init__(self: Facing, up: bool = False, down: bool = False, left: bool = False, right: bool = False) -> Facing:
        """Initialize Facing.

        Args:
            self (Facing): Itself.
            up (bool, optional): Is default facing up. Defaults to False.
            down (bool, optional): Is default facing down. Defaults to False.
            left (bool, optional): Is default facing left. Defaults to False.
            right (bool, optional): Is default facing right. Defaults to False.

        Returns:
            Facing: Itself.
        """
        self.set(
            up,
            down,
            left,
            right
        )

    def clear(self: Facing) -> Facing:
        """Clear facement.

        Args:
            self (Facing): Itself.

        Returns:
            Facing: Itself.
        """
        return self.set()

    def set(self: Facing, up: bool = False, down: bool = False, left: bool = False, right: bool = False) -> Facing:
        """Set facing.

        Args:
            self (Facing): Itself.
            up (bool, optional): Is default facing up. Defaults to False.
            down (bool, optional): Is default facing down. Defaults to False.
            left (bool, optional): Is default facing left. Defaults to False.
            right (bool, optional): Is default facing right. Defaults to False.

        Returns:
            Facing: Itself.
        """
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        return self
