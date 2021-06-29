#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """returns sum of 2 vectors"""
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """returns sub of 2 vectors"""
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        """returns multiplication of 1 vector and num"""
        return Vec2d(self.x * k, self.y * k)

    def __len__(self):
        """returns length of vector"""
        return math.sqrt(self.x * self.x + self.y * self.y)

    def int_pair(self):
        """returns pair of coordinates (x, y)"""
        return self.x, self.y

    def make_x_opposite(self):
        """is used for multiplication x by -1"""
        self.x = -self.x

    def make_y_opposite(self):
        """is used for multiplication y by -1"""
        self.y = -self.y


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []

    def add_point(self, point: Vec2d, speed: Vec2d):
        """add point to polyline"""
        self.points.append(point)
        self.speeds.append(speed)

    def set_points(self):
        """recount coordinates"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p].make_x_opposite()
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p].make_y_opposite()

    def draw_points(self, style="points", width=3, color=(255, 255, 255), pnts=None):
        """draws points on the screen"""

        if pnts == None:
            pnts = self.points

        if style == "line":
            for p_n in range(-1, len(pnts) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(pnts[p_n].x), int(pnts[p_n].y)),
                                 (int(pnts[p_n + 1].x), int(pnts[p_n + 1].y)), width)

        elif style == "points":
            for p in pnts:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p.x), int(p.y)), width)


class Knot(Polyline):
    def set_points(self):
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p].make_x_opposite()
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p].make_y_opposite()

        self.get_knot()

    def get_point(self, base_points, alpha, deg=None):
        if deg is None:
            deg = len(base_points) - 1
        if deg == 0:
            return base_points[0]
        return (base_points[deg] * alpha) + (self.get_point(base_points, alpha, deg - 1) * (1 - alpha))

    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_knot(self, count=35):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)

            res.extend(self.get_points(ptn, count))
        return res

    def draw_points(self, style="points", width=3, color=(255, 255, 255), pnts=None):


        if style == "line":
            pnts = self.get_knot()
            for p_n in range(-1, len(pnts) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(pnts[p_n].x), int(pnts[p_n].y)),
                                 (int(pnts[p_n + 1].x), int(pnts[p_n + 1].y)), width)
        elif style == "points":
            for p in pnts:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p.x), int(p.y)), width)

# =======================================================================================
# Функции отрисовки
# =======================================================================================
def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    polyline = Polyline()
    knot = Knot()
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                polyline.add_point(Vec2d(event.pos[0], event.pos[1]), Vec2d(random.random() * 2, random.random() * 2))
                knot.add_point(Vec2d(event.pos[0], event.pos[1]), Vec2d(random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        polyline.draw_points()

        knot.draw_points("line", 3, color)

        # draw_points(get_knot(points, steps), "line", 3, color)
        if not pause:
            polyline.set_points()

            knot.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
