

def play_snake_game(score_y,score_size,food_size,food_X,food_Y1,food_Y2,pc_height,pc_width,pc_shapesize,pc_forward,pc_border_pensize,pc_borderX,pc_borderY,pc_game_width,pc_game_height,pc_collisonX,pc_collisonY1,pc_collisonY2,using_phone):
    class Snake(Turtle):
        def __init__(self):
            super().__init__()
            self.body = []
            self.startingBody()

        def startingBody(self):
            for i in range(3):
                self.createSnake(0, 0)
            self.body[0].color("blue")

        def createSnake(self, posiX, posiY):
            segment = Turtle("square")
            segment.color('white')
            segment.speed("fastest")
            segment.penup()
            segment.shapesize(pc_shapesize, pc_shapesize)
            segment.ht()
            segment.goto(posiX, posiY)
            self.body.append(segment)
            segment.showturtle()

        def deleteSnake(self):
            for segment in self.body:
                segment.clear()
                segment.reset()
                segment.ht()
                del segment

        def addSegment(self):
            self.createSnake(self.body[-1].xcor(), self.body[-1].ycor())

        def move(self):
            for i in range(len((self.body)) - 1, 0, -1):
                self.body[i].goto(self.body[i - 1].xcor(), self.body[i - 1].ycor())
            self.body[0].forward(pc_forward)

        def moveUp(self, x=None, y=None):
            if self.body[0].heading() != 270:
                self.body[0].setheading(90)

        def moveDown(self, x=None, y=None):

            if self.body[0].heading() != 90:
                self.body[0].setheading(270)

        def moveLeft(self, x=None, y=None):
            if self.body[0].heading() != 0:
                self.body[0].setheading(180)

        def moveRight(self, x=None, y=None):
            if self.body[0].heading() != 180:
                self.body[0].setheading(0)

        def collide(self):
            if self.body[0].xcor() > pc_collisonX or self.body[0].xcor() < -pc_collisonX or self.body[0].ycor() > pc_collisonY1 or self.body[0].ycor() < pc_collisonY2:
                return True
            else:
                for segment in self.body:
                    if segment == self.body[0]:
                        pass
                    elif self.body[0].distance(segment) < 10:
                        return True

    class Score(Turtle):
        def __init__(self):
            super().__init__()
            self.score_count = 0
            self.color('yellow')
            self.speed("fastest")
            self.penup()
            self.ht()
            self.goto(0, score_y)
            self.loadScreen()
            self.updateBoard()

        def loadScreen(self):
            border = Turtle()
            border.ht()
            border.pensize(pc_border_pensize)
            border.penup()
            border.goto(pc_borderX, pc_borderY)
            border.color("red")
            border.speed("fast")
            border.pendown()
            load = Turtle()
            load.ht()
            load.penup()
            load.write("L O A D I N G", True, align="center", font=("Arial", 20, "bold"))
            for i in range(4):
                border.setheading(90 * i)
                if i % 2 == 0:
                    border.forward(pc_game_width)
                else:
                    border.forward(pc_game_height)
            load.clear()

        def updateBoard(self):
            self.write(f"SCORE : {self.score_count}", False, align="center", font=("Arial", score_size, "bold"))

        def increaseScore(self):
            self.clear()
            self.score_count += 1
            self.updateBoard()

        def gameOver(self):
            self.goto(0, 0)
            self.write(f"GAME OVER", False, align="center", font=("Arial", 20, "bold"))

        def clearBoard(self):
            self.ht()
            self.reset()
            self.clear()
            del self

    class Food(Turtle):
        def __init__(self):
            super().__init__()
            self.shape("circle")
            self.penup()
            self.color("blue")
            self.shapesize(food_size, food_size)
            self.speed("fastest")
            self.createFood()

        def createFood(self):
            if food_Y2 == None:
                self.goto(random.randint(-food_X, food_X), random.randint(-food_Y1, food_Y1))
            else:
                self.goto(random.randint(-food_X, food_X), random.randint(-food_Y1, food_Y2))
        def clearFood(self):
            self.ht()
            self.reset()
            self.clear()
            del self

    score = Score()
    food = Food()
    snake = Snake()
    condition = True

    screen = Screen()
    screen.title("SNAKE GAME (RS)")
    screen.tracer()
    screen.bgcolor("black")
    screen.title("SNAKE GAME")
    screen.setup(pc_width, pc_height)
    screen.listen()
    screen.onkey(key="w", fun=snake.moveUp)
    screen.onkey(key="a", fun=snake.moveLeft)
    screen.onkey(key="s", fun=snake.moveDown)
    screen.onkey(key="d", fun=snake.moveRight)
    if "YES".lower() in using_phone:
        up_button = Turtle()
        up_button.speed("fastest")
        up_button.shape("triangle")
        up_button.color("yellow")
        up_button.shapesize(8)
        up_button.penup()
        up_button.goto(0, -740)
        up_button.setheading(90)
        up_button.onclick(snake.moveUp)

        down_button = Turtle()
        down_button.speed("fastest")
        down_button.shape("triangle")
        down_button.color("yellow")
        down_button.shapesize(8)
        down_button.penup()
        down_button.setheading(270)
        down_button.goto(0, -990)
        down_button.onclick(snake.moveDown)

        left_button = Turtle()
        left_button.speed("fastest")
        left_button.shape("triangle")
        left_button.color("yellow")
        left_button.shapesize(8)
        left_button.penup()
        left_button.setheading(180)
        left_button.goto(-130, -860)
        left_button.onclick(snake.moveLeft)

        right_button = Turtle()
        right_button.speed("fastest")
        right_button.shape("triangle")
        right_button.color("yellow")
        right_button.shapesize(8)
        right_button.penup()
        right_button.goto(130, -860)
        right_button.onclick(snake.moveRight)
    # screen.tracer()
    while condition:
        # screen.update()
        time.sleep(0.09)
        snake.move()
        if snake.collide():
            score.gameOver()
            food.clearFood()
            snake.deleteSnake()
            score.clearBoard()
            play_snake_game(score_y, score_size, food_size, food_X, food_Y1, food_Y2, pc_height, pc_width, pc_shapesize,
                            pc_forward, pc_border_pensize, pc_borderX, pc_borderY, pc_game_width, pc_game_height,
                            pc_collisonX, pc_collisonY1, pc_collisonY2, using_phone)
            break
        if snake.body[0].distance(food) < 25:
            score.increaseScore()
            food.createFood()
            snake.addSegment()
    screen.mainloop()
pc_height = 670
pc_width = 840

pc_shapesize = 1
pc_forward = 25

pc_border_pensize = 5
pc_borderX = -415
pc_borderY = -310
pc_game_width = 830
pc_game_height = 600

pc_collisonX = 379
pc_collisonY1 = 250
pc_collisonY2 = -280

score_y = 290
score_size = 20

food_X = 380
food_Y1 = 280
food_Y2 = None
food_size = 1
######################
ph_height = 2000
ph_width = 1010

ph_shapesize = 2
ph_forward = 45

ph_border_pensize = 15
ph_borderX = -527
ph_borderY = -615
ph_game_width = 1050
ph_game_height = 1630

ph_collisonX = 490
ph_collisonY1 = 980
ph_collisonY2 = -540

ph_score_y = 1030
ph_score_size = 10

ph_food_size = 2
ph_food_X = 480
ph_food_Y1 = 580
ph_food_Y2 = 980
from turtle import *
import time, random

using_phone = textinput(title="PLAY IN FULL SCREEN WHEN PLAYING IN P.C.", prompt="ARE YOU USING PHONE (YES OR NO) ? ")
if using_phone == None:
    pass
elif "NO".lower() in using_phone:
    play_snake_game(score_y,score_size,food_size,food_X,food_Y1,food_Y2,pc_height,pc_width,pc_shapesize,pc_forward,pc_border_pensize,pc_borderX,pc_borderY,pc_game_width,pc_game_height,pc_collisonX,pc_collisonY1,pc_collisonY2,using_phone)
elif "YES".lower() in using_phone:
    play_snake_game(ph_score_y, ph_score_size, ph_food_size, ph_food_X, ph_food_Y1, ph_food_Y2, ph_height, ph_width, ph_shapesize,
                    ph_forward, ph_border_pensize, ph_borderX, ph_borderY, ph_game_width, ph_game_height, ph_collisonX,
                    ph_collisonY1, ph_collisonY2, using_phone)
