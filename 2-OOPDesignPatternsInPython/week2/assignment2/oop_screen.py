#! / usr / bin / env python3
# - * - coding: utf-8 - * -

import pygame
import random
import math

SCREEN_DIM = (800, 600)

def draw_help ():
    "" "function of drawing the help screen of the program" ""
    gameDisplay.fill ((50, 50, 50))
    font1 = pygame.font.SysFont ("courier", 24)
    font2 = pygame.font.SysFont ("serif", 24)
    data = []
    data.append (["F1", "Show Help"])
    data.append (["R", "Restart"])
    data.append (["P", "Pause / Play"])
    data.append (["Num +", "More points"])
    data.append (["Num-", "Less points"])
    data.append (["", ""])
    data.append ([str (steps), "Current points"])

    pygame.draw.lines (gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate (data):
        gameDisplay.blit (font1.render (
            text [0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit (font2.render (
            text [1], True, (128, 128, 255)), (200, 100 + 30 * i))

class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Vec2d(self.x * k, self.y * k)

    def __len__(self):
        return math.sqrt(self.x * self.x, self.y * self.y)

    def __getitem__(self, idx):
        if idx == 0:
            return self.x
        else:
            return self.y


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []

    def add_point(self, ptn):
        self.points.append(ptn)

    def add_speed(self, speed):
        self.speeds.append(speed)
    
    def reset(self):
        self.points = []
        self.speeds = []

    def set_points(self):
        """function of recalculation of GCP coordinates"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p][0] > SCREEN_DIM[0] or self.points[p][0] < 0:
                self.speeds[p] = (-self.speeds[p][0], self.speeds[p][1])
            if self.points[p][1] > SCREEN_DIM[1] or self.points[p][1] < 0:
                self.speeds[p] = (self.speeds[p][0], -self.speeds[p][1])

    def draw_points(self, points,  style="points", width=3, color=(255, 255, 255)):
        """function of drawing points on the screen"""
        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(
                    gameDisplay,
                    color,
                    (int(points[p_n][0]), int(points[p_n][1])),
                    (int(points[p_n + 1][0]), int(points[p_n + 1][1])),
                    width,
                )

        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color, (int(p[0]), int(p[1])), width)


class Knot(Polyline):
    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return (points[deg] * alpha) + (
            self.get_point(points, alpha, deg - 1) * (1 - alpha)
        )

    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_knot(self, count):
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
# ================================================= =======================================
# Main program
# ================================================= =======================================
if __name__ == "__main__":
    pygame.init ()
    gameDisplay = pygame.display.set_mode (SCREEN_DIM)
    pygame.display.set_caption ("MyScreenSaver")

    steps = 35
    working = True
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color (0)

    knot = Knot()

    while working:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    knot.reset()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                knot.add_point(Vec2d(*event.pos))
                knot.add_speed(Vec2d(random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        knot.draw_points(knot.points)
        knot.draw_points(knot.get_knot(steps), "line", 3, color)
        if not pause:
            knot.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)