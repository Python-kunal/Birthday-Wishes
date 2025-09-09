import turtle

my_turtle = turtle.Turtle()

my_turtle.speed(10)

my_turtle.pencolor("red")

my_turtle.penup()
my_turtle.goto(-250,0)
my_turtle.pendown()

my_turtle.write("Happy", font=("Arial", 45 , "bold"))

my_turtle.pencolor("violet")

my_turtle.penup()
my_turtle.forward(200)

my_turtle.write("Birthday", font=("Arial", 45 , "bold"))

my_turtle.pencolor("red")

my_turtle.penup()
my_turtle.goto(205,0)
my_turtle.pendown()

my_turtle.write("Kunal", font=("Arial", 45 , "bold"))

my_turtle.hideturtle()
turtle.done()