from __future__ import annotations

# Packages
import pygame

# Helpers
from ..Helpers.Cords import Cords
from ..Helpers.Movement import Movement


class Element():
    def __init__(self: Element, color: pygame.Color = pygame.Color(255, 255, 255)) -> Element:
        """Initialize game element.

        Args:
            self (Element): Itself.
            color (pygame.Color, optional): Color of the element. Defaults to pygame.Color(255, 255, 255).

        Returns:
            Element: Itself.
        """
        self._color = color
        self._alive = True
        self._children = []
        self._has_hitbox = False

    def _draw(self: Element, surface: pygame.Surface, scale: Cords) -> Element:
        """Draw element to given surface.

        Args:
            self (Element): Itself.
            surface (pygame.Surface): Surface to draw on.
            scale (Cords): Scale of the drawing.

        Returns:
            Element: Itself.
        """
        return self

    def _frame(self: Element, time_diff: float, events: list, surface: pygame.Surface, scale: Cords) -> Element:
        """Handle frame.

        Args:
            self (Element): Itself.
            time_diff (float): Time difference.
            events (list): Event list.
            surface (pygame.Surface): Game surface.
            scale (Cords): Scale of the drawing.

        Returns:
            Element: Itself.
        """

        # Draw itself.
        self._draw(surface, scale)

        # Handle children.
        children = []
        child: Element
        for child in self._children:
            # If is still alive.
            if child.alive():
                child._frame(
                    time_diff,
                    events,
                    surface,
                    scale
                )
                children.append(child)
            else:
                print(type(child).__name__, ": Died")
        self._children = children

        return self

    def alive(self: Element) -> bool:
        """Is game element alive.

        Args:
            self (Element): Itself.

        Returns:
            bool: Is game element alive.
        """
        return self._alive

    def add_child(self: Element, child: Element) -> Element:
        """Add child.

        Args:
            self (Element): Itself.
            child (Element): Child to add.

        Returns:
            Element: Itself.
        """
        self._children.append(child)
        return self

    def hitbox(self: Element, scale: Cords) -> pygame.Rect:
        """Hitbox for element.

        Args:
            self (Element): Itself.
            scale (Cords): Scale.

        Returns:
            pygame.Rect: Hitbox for element.
        """
        return pygame.Rect(0, 0, 0, 0)

    def hitboxes(self: Element, scale: Cords) -> dict:
        """All hitboxes.

        Args:
            self (Element): Itself.
            scale (Cords): Scale.

        Returns:
            dict: Hitboxes dictonary with key as object id and value pygame.Rect hitbox.
        """
        hitboxes = {}
        if self._has_hitbox and self.alive():
            hitboxes[id(self)] = self.hitbox(scale)
        child: Element
        for child in self._children:
            # Collect hitboxes.
            hitboxes.update(child.hitboxes(scale))
        return hitboxes

    def die(self: Element) -> Element:
        """Mark element as dead.

        Args:
            self (Element): Itself.

        Returns:
            Element: Itself.
        """
        self._alive = False
        return self

    def check_hitboxes(self: Element, hitboxes: dict, scale: Cords) -> Element:
        """Check given hitboxes.

        Args:
            self (Element): Itself.
            hitboxes (dict): Hitboxes to check.
            scale (Cords): Scale.

        Returns:
            Element: Itself.
        """

        # Check own hitbox, if have one and is alive.
        if self._has_hitbox and self.alive():
            my_id = id(self)
            own_hitbox = self.hitbox(scale)
            hitbox: pygame.Rect
            for key, hitbox in hitboxes.items():
                # Is not own hitbox and collides with own.
                if key != my_id and own_hitbox.colliderect(hitbox):
                    # Set as dead.
                    self.die()
                    break
        # Check children hitboxes.
        child: Element
        for child in self._children:
            # If is instance of Position and still alive.
            if child._has_hitbox and child.alive():
                # Collect hitboxes.
                child.check_hitboxes(hitboxes, scale)
        return self
