import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Definisikan verteks kubus
vertices = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
]

# Definisikan sisi kubus
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 7),
    (7, 6),
    (6, 4),
    (0, 4),
    (1, 5),
    (2, 7),
    (3, 6)
]

# Definisikan balok
def draw_rectangle():
    glBegin(GL_QUADS)
    glColor3fv((0.0, 1.0, 0.0))  # Warna hijau
    glVertex3fv((1, 1, -1))
    glVertex3fv((1, -1, -1))
    glVertex3fv((1, -1, 1))
    glVertex3fv((1, 1, 1))
    glEnd()

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    # Rotasi awal
    x_rotation, y_rotation = 0, 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Mengatur rotasi
        x_rotation += 1
        y_rotation += 1

        # Membersihkan layar
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Memindahkan dan merotasi objek
        glTranslatef(0.0, 0.0, -5)
        glRotatef(x_rotation, 1, 0, 0)
        glRotatef(y_rotation, 0, 1, 0)

        # Menggambar kubus
        draw_cube()

        # Menggambar balok
        draw_rectangle()

        # Memperbarui layar
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
