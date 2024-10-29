import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball Animation")

# Warna
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Parameter bola
ball_radius = 30
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 5
ball_speed_y = 5

# Loop utama
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update posisi bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Periksa tabrakan dengan dinding
    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
        ball_speed_x = -ball_speed_x  # Balik arah horizontal
    if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
        ball_speed_y = -ball_speed_y  # Balik arah vertikal

    # Mengisi latar belakang
    screen.fill(WHITE)

    # Menggambar bola
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Perbarui layar
    pygame.display.flip()

    # Atur kecepatan frame
    pygame.time.delay(30)
