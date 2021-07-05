#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    """Class representing 2 dimensional vector"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @classmethod
    def from_pos(cls, pos):
        return cls(pos[0], pos[1])

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2d(self.x * other, self.y * other)

    def __len__(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def int_pair(self):
        return int(self.x), int(self.y)


class Polyline:
    """Class representing 2 dimensional polyline"""
    def __init__(self):
        self.points = []
        self.speeds = []

    def append(self, point, speed):
        self.points.append(point)
        self.speeds.append(speed)

    def __del__(self):
        pass

    def get_point(self, alpha, deg=None):
        if deg is None:
            deg = len(self.points) - 1
        if deg == 0:
            return self.points[0]
        return self.points[deg] * alpha + self.get_point(alpha, deg - 1) * (1 - alpha)

    def get_points(self, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(i * alpha))
        return res

    def draw_points(self, game_display, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(game_display, color, self.points[p_n].int_pair(),
                                 self.points[p_n + 1].int_pair(), width)

        elif style == "points":
            for p in self.points:
                pygame.draw.circle(game_display, color, p.int_pair(), width)

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p] = Vec2d(- self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)

    def draw(self, game_display, width, color):
        self.draw_points(game_display)
        self.draw_points(game_display, "line", width, color)


class Knot(Polyline):

    def __init__(self, steps):
        super().__init__()
        self.steps = steps

    def get_knot(self, count):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = Polyline()
            ptn.points = [(self.points[i] + self.points[i + 1]) * 0.5, self.points[i + 1],
                          (self.points[i + 1] + self.points[i + 2]) * 0.5]
            res.extend(ptn.get_points(count))
        return res

    def __add__(self, point, speed):
        super().append(point, speed)
        self.get_knot(self.steps)

    def set_points(self):
        super().set_points()
        self.get_knot(self.steps)


# Методы для работы с векторами

# "Отрисовка" точек
# Сглаживание ломаной

class ScreenSaverState:

    def __init__(self, steps):
        self.working = True
        self.points = Knot(steps)
        self.show_help = False
        self.pause = True
        self.steps = steps

    def __next__(self):
        if not self.working:
            raise StopIteration()
        for event in pygame.event.get():
            self.process_event(event)
        return self

    def process_event(self, event):
        if event.type == pygame.QUIT:
            self.working = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.working = False
            if event.key == pygame.K_r:
                self.points = Knot(self.steps)
            if event.key == pygame.K_p:
                self.pause = not self.pause
            if event.key == pygame.K_KP_PLUS:
                self.steps += 1
            if event.key == pygame.K_F1:
                self.show_help = not self.show_help
            if event.key == pygame.K_KP_MINUS:
                self.steps -= 1 if self.steps > 1 else 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.points.append(Vec2d.from_pos(event.pos), Vec2d(int(random.random() * 2), int(random.random() * 2)))


class ScreenSaver:
    def __init__(self, name, steps):
        self.name = name
        self.steps = steps
        self.game_display = None
        self.hue = 0
        self.color = pygame.Color(0)

    def __enter__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode(SCREEN_DIM)
        pygame.display.set_caption(self.name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pygame.display.quit()
        pygame.quit()

    def __iter__(self):
        return ScreenSaverState(self.steps)

    # Отрисовка справки
    def draw_help(self, steps):
        self.game_display.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = [["F1", "Show Help"], ["R", "Restart"], ["P", "Pause/Play"],
                ["Num+", "More points"], ["Num-", "Less points"], ["", ""],
                [str(steps), "Current points"]]

        pygame.draw.lines(self.game_display, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            self.game_display.blit(font1.render(text[0], True, (128, 128, 255)),
                                   (100, 100 + 30 * i))
            self.game_display.blit(font2.render(text[1], True, (128, 128, 255)),
                                   (200, 100 + 30 * i))

    def draw(self, state):
        self.game_display.fill((0, 0, 0))
        self.hue = (self.hue + 1) % 360
        self.color.hsla = (self.hue, 100, 50, 100)
        state.points.draw(self.game_display, 3, self.color)
        if not state.pause:
            state.points.set_points()
        if state.show_help:
            self.draw_help(state.steps)

        pygame.display.flip()


def main():
    with ScreenSaver("MyScreenSaver", 35) as s:
        for state in s:
            s.draw(state)
    exit(0)


# Основная программа
if __name__ == "__main__":
    main()
