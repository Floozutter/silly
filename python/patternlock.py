from tkinter import Tk
from turtle import ScrolledCanvas, TurtleScreen, RawTurtle

DIGIT2POS = dict(zip(
    "123456789",
    ((100 * (j - 1), 100 * (-i + 1)) for i in range(3) for j in range(3))
))

def draw_dots(turt: RawTurtle) -> None:
    penstate = turt.pen()
    turt.penup()
    for x, y in DIGIT2POS.values():
        turt.setheading(turt.towards(x, y))
        turt.goto(x, y)
        turt.dot()
    turt.pen(pen = penstate)

def draw_pattern(turt: RawTurtle, pattern: str) -> None:
    penstate = turt.pen()
    turt.penup()
    for x, y in map(lambda digit: DIGIT2POS[digit], pattern):
        turt.setheading(turt.towards(x, y))
        turt.goto(x, y)
        turt.pendown()
        turt.dot()
    turt.pen(pen = penstate)

def main(pattern: str) -> None:
    master = Tk()
    canvas = ScrolledCanvas(master)
    canvas.pack()
    screen = TurtleScreen(canvas)
    screen.colormode(255)
    turt = RawTurtle(screen)
    draw_dots(turt)
    turt.pencolor((178, 34, 34))
    draw_pattern(turt, pattern)
    screen.mainloop()

if __name__ == "__main__":
    main("61834927")
