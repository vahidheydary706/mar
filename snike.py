import turtle
import time
import random

delay = 0.1
score = 0

class snike:
    win = turtle.Screen()
    win.title('Game snike')
    win.bgcolor('blue')
    win.setup(width=600, height=600)
    win.tracer(0)

    head = turtle.Turtle()
    head.speed(0)
    head.shape('square')
    head.color('green')
    head.penup()
    head.goto(0,0)
    head.direction = 'up'

    food = turtle.Turtle()
    food.speed(0)
    food.shape('circle')
    food.color('red')
    food.penup()
    food.goto(0,100)

    segments = []

    def goup():
        head.direction = 'up'

    def godown():
        head.direction = 'down'

    def goright():
        head.direction = 'right'

    def goleft():
        head.direction = 'left'

    def move():
        if head.direction == 'up':
            y = head.ycor()
            head.sety(y+20)

        if head.direction == 'down':
            y = head.ycor()
            head.sety(y-20)

        if head.direction == 'right':
            x = head.xcor()
            head.setx(x+20)

        if head.direction == 'left':
            x = head.xcor()
            head.setx(x-20)

    win.listen()
    win.onkeypress(goup, 'w')
    win.onkeypress(godown, 's')
    win.onkeypress(goright, 'd')
    win.onkeypress(goleft, 'a')

while True:
    win.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        print('GameOver')
        head.goto(0,0)
        head.direction = 'stop'

        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()
        score = 0
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        newsegment = turtle.Turtle()
        newsegment.speed(0)
        newsegment.shape('square')
        newsegment.color('black','green',)
        newsegment.penup()
        segments.append(newsegment)
        score = score +1
        print(score)

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
    time.sleep(delay)
