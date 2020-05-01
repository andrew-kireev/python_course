#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)



class Vec2d:
    x = []
    def __init__(self, x, y=None):
        if y == None:
            self.x = list(x)
        else:
            self.x = [x, y]

    def int_pair(self):
        return self.x, self.y

    def __add__(self, other):
        if isinstance(other, tuple):
            return self.x[0] + other[0], self.x[1] + other[1]
        return self.x[0] + other.x[0], self.x[1] + other.x[1]

    def __sub__(self, other):
        self.x -= other.x
        return self.x

    def __mul__(self, num):
        return self.x[0] * num, self.x[1] * num

    def __len__(self):
        return math.sqrt(self.x[1] * self.x[1] + self.x[0] * self.x[0])

    def __getitem__(self, item):
        return self.x[item]



class Polyline:
    def __init__(self):
        self.base_points = []
        self.speeds = []
        self.steps = 35

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return Vec2d(Vec2d(points[deg]) * alpha) + Vec2d(Vec2d(self.get_point(points, alpha, deg - 1)) *  (1 - alpha))

    def get_points(self, base_points):
        alpha = 1 / self.steps
        res = []
        for i in range(self.steps):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.base_points)):
            self.base_points[p] = Vec2d(self.base_points[p]) + self.speeds[p]
            if self.base_points[p][0] > SCREEN_DIM[0] or self.base_points[p][0] < 0:
                self.speeds[p] = (- self.speeds[p][0], self.speeds[p][1])
            if self.base_points[p][1] > SCREEN_DIM[1] or self.base_points[p][1] < 0:
                self.speeds[p] = (self.speeds[p][0], -self.speeds[p][1])

    def draw_points(self, points, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(points[p_n][0]), int(points[p_n][1])),
                                 (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)

        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p[0]), int(p[1])), width)



class Knot(Polyline):
    def __init__(self):
        super().__init__()
        self.per_poinst = []

    def get_knot(self):
        if len(self.base_points) < 3:
            return []
        res = []
        for i in range(-2, len(self.base_points) - 2):
            ptn = []
            ptn.append(Vec2d(Vec2d(self.base_points[i]) + Vec2d(self.base_points[i + 1])) * 0.5)
            ptn.append(self.base_points[i + 1])
            ptn.append(Vec2d(Vec2d(self.base_points[i + 1]) +  Vec2d(self.base_points[i + 2])) *  0.5)

            res.extend(self.get_points(ptn))
        return res





# =======================================================================================
# Функции отрисовки
# =======================================================================================

def draw_help(steps):
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


# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    # steps = 35
    working = True
    points = []
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    line = Knot()

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    line.base_points = []
                    line.speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    line.steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    line.steps -= 1 if line.steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                line.base_points.append(Vec2d(event.pos))
                line.speeds.append(Vec2d(random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        line.draw_points(line.base_points)
        line.draw_points(line.get_knot(), "line", 3, color)
        if not pause:
            line.set_points()
        if show_help:
            draw_help(line.steps)

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)