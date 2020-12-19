from __future__ import annotations

import pygame
import math

from .Movement import Movement
from .Cords import Cords
from .Player import Player
from .Timer import Timer


class Game():
    """Game class that houses main game logic.
    """

    def __init__(self: Game, width: int = 800, height: int = 600) -> Game:
        """Initialise new game.

        Args:
            self (Game): Itself.
            width (int, optional): Window resolution width. Defaults to 800.
            height (int, optional): Window resolution height. Defaults to 600.

        Returns:
            Game: Itself.
        """
        self._fps_cap = 360
        self._resolution = Cords(width, height)
        self._scale = Cords(
            self._resolution.x/800,
            self._resolution.y/600
        )
        self._surface = pygame.display.set_mode(
            (self._resolution.x, self._resolution.y)
        )
        self._player = Player(self._scale)
        self._running = False
        self._timer = Timer()
        self._init_fps()
        self._init_frame_limiter()
        pygame.init()

    def run(self: Game) -> Game:
        """Run the game.

        Args:
            self (Game): Itself.

        Returns:
            Game: Itself.
        """

        # Set running.
        self._running = True

        # Initialize counters and timers.
        self._init_fps()
        self._init_frame_limiter()
        self._timer = Timer()

        # While running.
        while self._running:
            # Run actions on frame.
            self._frame()
            # Limit framerate to given cap.
            self._frame_limiter()
            # Count and print FPS every second.
            self._fps()
        pygame.quit()
        return self

    def _init_fps(self: Game) -> Game:
        """Initialize FPS counter and timer.

        Args:
            self (Game): Itself.

        Returns:
            Game: Itself.
        """
        self._frame_counter = 0
        self._fps_timer = Timer()
        return self

    def _fps(self: Game) -> bool:
        """Count FPS and print average every second.

        Args:
            self (Game): Itself.

        Returns:
            bool: Was FPS printed.
        """
        self._frame_counter += 1
        curr = self._fps_timer.curr()
        print_fps = (curr > 1)
        if print_fps:
            print("FPS: ", self._frame_counter/curr)
            self._frame_counter = 0
            self._fps_timer.start()
        return print_fps

    def _init_frame_limiter(self: Game) -> Game:
        """Initialize frame limiter variables.

        Args:
            self (Game): Itself.

        Returns:
            Game: Itself.
        """
        self._frame_timer = Timer()
        self._fps_cap_seconds = 1/self._fps_cap
        return self

    def _frame_limiter(self: Game) -> bool:
        """Handle frame limiter.

        Args:
            self (Game): Itself.

        Returns:
            bool: Was frames limited.
        """
        limit = (self._frame_timer.curr() < self._fps_cap_seconds)
        if limit:
            pygame.time.wait(
                math.floor(
                    (
                        self._fps_cap_seconds
                        -
                        self._frame_timer.curr()
                    )
                    *
                    1000
                )
            )
        self._frame_timer.start()
        return limit

    def _update_time(self: Game) -> float:
        """Update timer

        Args:
            self (Game): Itself.

        Returns:
            float: Time diff from last update.
        """
        return self._timer.curr(True)

    def _frame(self: Game) -> Game:
        """Run logic inside frame.

        Args:
            self (Game): Itself.

        Returns:
            Game: Itself.
        """
        time_diff = self._update_time()
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                return
            else:
                events.append(event)
        self._surface.fill((0, 0, 0))
        self._player.frame(time_diff, events, self._surface)
        pygame.display.update()
        return self
