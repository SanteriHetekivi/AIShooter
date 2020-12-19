from __future__ import annotations
import time


class Timer():
    """Timer class.
    """

    def __init__(self: Timer) -> Timer:
        """Initialize and start timer.

        Args:
            self (Timer): Itself.

        Returns:
            Timer: Itself.
        """
        self.start()

    def start(self: Timer) -> Timer:
        """Start timer.

        Args:
            self (Timer): Itself.

        Returns:
            Timer: Itself.
        """
        self.start_time = time.time()
        return self

    def curr(self: Timer, start: bool = False) -> float:
        """Current time diff from start.

        Args:
            self (Timer): Itself.
            start (bool, optional): Start timer after getting current? Defaults to False.

        Returns:
            float: Current time diff from start.
        """
        diff = time.time()-self.start_time
        if start:
            self.start()
        return diff
