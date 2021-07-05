#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math
from typing import Tuple, List


class Vec2d:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    @staticmethod
    def from_tuple(p: Tuple[float, float]):
        return Vec2d(p[0], p[1])

    def len(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def int_pair(self) -> Tuple[int, int]:
        return int(self.x), int(self.y)

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __mul__(self, k: float):
        return Vec2d(self.x * k, self.y * k)


class Polyline:
    def __init__(self, game_display, screen_dimension: Vec2d) -> None:
        self._base_speed = 1.0
        self._screen_dimension = screen_dimension
        self.points: List[Vec2d] = []
        self.speeds: List[Vec2d] = []
        self._game_display = game_display

    def speed_up(self, d: float):
        self._base_speed *= d

    def reset(self) -> None:
        self.points: List[Vec2d] = []
        self.speeds: List[Vec2d] = []

    def add_point(self, point: Vec2d, speed: Vec2d) -> None:
        self.points.append(point)
        self.speeds.append(speed)

    def remove_last_point(self) -> None:
        self.points = self.points[:-1]

    def set_points(self) -> None:
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p] * self._base_speed
            if self.points[p].x > self._screen_dimension.x or self.points[p].x < 0:
                self.speeds[p] = Vec2d(-self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y > self._screen_dimension.y or self.points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)

    def draw_points(self, width=3, color=(255, 255, 255)) -> None:
        for p in self.points:
            pygame.draw.circle(
                self._game_display,
                color,
                p.int_pair(),
                width,
            )


class Knot(Polyline):
    def get_point(self, base_points, alpha: float, deg: int = None) -> Vec2d:
        if deg is None:
            deg = len(base_points) - 1

        if deg == 0:
            return base_points[0]

        return (base_points[deg] * alpha) + (self.get_point(base_points, alpha, deg - 1) * (1 - alpha))

    def get_points(self, base_points, count: int) -> List[Vec2d]:
        alpha = 1 / count
        res = []

        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))

        return res

    def get_knot(self, count: int) -> List[Vec2d]:
        if len(self.points) < 3:
            return []

        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = [
                (self.points[i] + self.points[i + 1]) * 0.5,
                self.points[i + 1],
                (self.points[i + 1] + self.points[i + 2]) * 0.5,
            ]
            res.extend(self.get_points(ptn, count))

        return res

    def draw_knots(self, count: int, width=3, color=(255, 255, 255)) -> None:
        knots = self.get_knot(count)
        for p_n in range(-1, len(knots) - 1):
            pygame.draw.line(
                self._game_display,
                color,
                knots[p_n].int_pair(),
                knots[p_n + 1].int_pair(),
                width,
            )

    def redraw(self, count, color) -> None:
        self.draw_points()
        self.draw_knots(count, color=color)


def draw_help(game_display) -> None:
    game_display.fill((50, 50, 50))

    data = [
        ["F1", "Show Help"],
        ["", ""],
        ["A", "Add new line"],
        ["D", "Delete last point"],
        ["", ""],
        ["R", "Restart"],
        ["P", "Pause/Play"],
        ["", ""],
        ["F", "Faster"],
        ["S", "Slower"],
        ["", ""],
        ["Num+", "More points"],
        ["Num-", "Less points"],
        ["", ""],
        [str(steps), "Current points"],
    ]

    pygame.draw.lines(
        game_display,
        (255, 50, 50, 255),
        True,
        [(0, 0), (800, 0), (800, 600), (0, 600)],
        5,
    )

    for i, text in enumerate(data):
        game_display.blit(
            pygame.font.SysFont("courier", 24).render(text[0], True, (128, 128, 255)),
            (100, 100 + 30 * i),
        )
        game_display.blit(
            pygame.font.SysFont("serif", 24).render(text[1], True, (128, 128, 255)),
            (200, 100 + 30 * i),
        )


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("MyScreenSaver")
    screen_dimension = Vec2d(800, 600)
    game_display = pygame.display.set_mode(screen_dimension.int_pair())
    knot = [Knot(game_display, screen_dimension)]

    steps = 35
    working = True
    show_help = False
    pause = True

    hue = 0
    knot_color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    for k in knot:
                        k.reset()
                if event.key == pygame.K_a:
                    knot.append(Knot(game_display, screen_dimension))
                if event.key == pygame.K_d:
                    k = knot[-1]
                    if len(k.points) == 0:
                        knot = knot[:-1]
                    if len(knot) == 0:
                        working = False
                    k.remove_last_point()
                if event.key == pygame.K_f:
                    for k in knot:
                        k.speed_up(1.1)
                if event.key == pygame.K_s:
                    for k in knot:
                        k.speed_up(0.9)
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                knot[-1].add_point(
                    Vec2d.from_tuple(event.pos),
                    Vec2d(random.random() * 2, random.random() * 2),
                )

        hue = (hue + 1) % 360
        knot_color.hsla = (hue, 100, 50, 100)
        game_display.fill((0, 0, 0))

        for k in knot:
            k.redraw(steps, knot_color)

        if not pause:
            for k in knot:
                k.set_points()

        if show_help:
            draw_help(game_display)

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
