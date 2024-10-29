import turtle
import time

# Setup layar
wn = turtle.Screen()
wn.title("I Love You Animation")
wn.bgcolor("white")

# Fungsi untuk menggambar hati
def draw_heart(turtle, size):
    turtle.color("red")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(size)
    turtle.circle(size * 0.3, 200)
    turtle.right(140)
    turtle.circle(size * 0.3, 200)
    turtle.forward(size)
    turtle.end_fill()
    turtle.setheading(0)

# Fungsi untuk menampilkan teks
def display_text(turtle, message, font_size):
    turtle.color("black")
    turtle.penup()
    turtle.goto(0, -50)
    turtle.write(message, align="center", font=("Arial", font_size, "bold"))
    turtle.hideturtle()

# Buat turtle untuk hati
heart_turtle = turtle.Turtle()
heart_turtle.speed(3)
heart_turtle.hideturtle()

# Buat turtle untuk teks
text_turtle = turtle.Turtle()
text_turtle.hideturtle()

# Animasi hati dan teks
def love_animation():
    for i in range(5):  # Ulang 5 kali untuk efek animasi
        heart_turtle.clear()
        heart_turtle.penup()
        heart_turtle.goto(0, 0)
        heart_turtle.pendown()
        
        # Gambar hati dengan ukuran berbeda untuk animasi
        draw_heart(heart_turtle, 150 - i*20)
        time.sleep(0.3)

    # Tampilkan teks "I Love You"
    display_text(text_turtle, "I Love You", 24)

# Jalankan animasi
love_animation()

# Tutup layar ketika selesai
wn.mainloop()
