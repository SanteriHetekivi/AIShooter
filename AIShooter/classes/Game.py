from __future__ import annotations

import pygame
import time
from .Movement import Movement
from .Cords import Cords
from .Player import Player


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
        pygame.init()
        self.resolution = Cords(width, height)
        self.scale = Cords(
            self.resolution.x/800,
            self.resolution.y/600
        )
        self.surface = pygame.display.set_mode(
            (self.resolution.x, self.resolution.y)
        )
        self.player = Player(self.scale)

    def run(self: Game) -> Game:
        """Run the game.

        Args:
            self (Game): Itself.

        Returns:
            Game: Itself.
        """
        self.running = True
        self.time = time.time()
        while self.running:
            self.frame()
        pygame.quit()
        return self

    def update_time(self: Game) -> float:
        """Update timer

        Args:
            self (Game): Itself.

        Returns:
            float: Time diff from last update.
        """
        curr_time = time.time()
        time_diff = curr_time - self.time
        self.time = curr_time
        return time_diff

    def frame(self: Game) -> Game:
        """Run logic inside frame.

        Args:
            self (Game): Itself.

        Returns:
            Game: Itself.
        """
        time_diff = self.update_time()
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
            else:
                events.append(event)
        self.surface.fill((0, 0, 0))
        self.player.frame(time_diff, events, self.surface)
        pygame.display.update()
        return self
