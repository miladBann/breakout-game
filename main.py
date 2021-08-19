from turtle import *
from paddle import Paddle
from ball import Ball
import time
from objects import Object


window = Screen()
window.setup(1200, 600)
window.tracer(0)
window.listen()

screen_delay = 0.1

the_paddle = Paddle((0, -270))
the_ball = Ball((0, 0))
objects = Object()

objects.create_first_row()
objects.create_second_row()
objects.create_third_row()
objects.create_fourth_row()
objects.create_fifth_row()
objects.create_sixth_row()


window.onkeypress(key="Right", fun=the_paddle.move_right)
window.onkeypress(key="Left", fun=the_paddle.move_left)

end = False
while end == False:
    time.sleep(screen_delay)
    window.update()

    the_ball.move()

    if the_ball.ycor() >= 280:
        the_ball.reflect_up_down()

    if the_ball.xcor() >= 580 or the_ball.xcor() <= -580:
        the_ball.reflect_sides()

    if the_ball.ycor() <= -280:
        the_ball.goto(0, 0)
        the_paddle.goto(0, -270)

    if the_ball.distance(the_paddle) <= 90 and the_ball.ycor() <= -260:
        the_ball.reflect_up_down()
        screen_delay -= 0.002

    for object in objects.all_cars:
        if object.distance(the_ball) < 30:
            object.goto(1000, 1000)
            the_ball.reflect_up_down()


window.mainloop()
