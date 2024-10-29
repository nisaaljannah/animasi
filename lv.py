import pygame
import math
import sys

# Inisialisasi Pygame
pygame.init()

# Konfigurasi layar
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("I Love You Animation")

# Warna
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 74)
text = font.render("I Love You", True, BLACK)

def draw_heart(x, y, size):
    """Menggambar hati dengan posisi dan ukuran yang diberikan."""
    points = [
        (x, y + size * 0.25),
        (x - size * 0.25, y - size * 0.25),
        (x - size * 0.75, y + size * 0.25),
        (x, y + size),
        (x + size * 0.75, y + size * 0.25),
        (x + size * 0.25, y - size * 0.25),
    ]
    pygame.draw.polygon(screen, RED, points)

def main():
    # Loop utama
    running = True
    size = 50
    grow = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Membersihkan layar
        screen.fill(WHITE)

        # Mengatur posisi hati dan animasi
        x = width // 2
        y = height // 2

        if grow:
            size += 1
            if size > 70:
                grow = False
        else:
            size -= 1
            if size < 50:
                grow = True

        draw_heart(x, y, size)

        # Menampilkan teks di bawah hati
        text_rect = text.get_rect(center=(x, y + 100))
        screen.blit(text, text_rect)

        # Memperbarui tampilan
        pygame.display.flip()
        pygame.time.delay(30)

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
