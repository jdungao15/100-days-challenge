import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# initialize
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
# Event Listener
screen.onkey(player.move_up, "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate random cars and move cars
    car_manager.gen_car()
    car_manager.move()

    # check if player collide with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # check if player reached the top
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.update_scoreboard()
        car_manager.increase_speed()

screen.exitonclick()
