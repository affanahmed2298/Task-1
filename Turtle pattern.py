
import turtle as tu

bob= tu.Turtle()  # Turtle object
sc = tu.Screen()  # Screen Object
sc.bgcolor("black")  # Screen Bg color
sc.title("Pattern")
bob.left(90)  # moving the turtle 90 degrees towards left
bob.speed(200)  # setting the speed of the turtle
sw = 0
hue1 = 1.0
hue2 = 0.0
hue3 = 0.0
for i in range (300): 
    if sw == 0:
        if hue3 >= 0.8:
            sw = 1
            
        hue3 += 0.1
    if sw==1:
        if hue2>=0.8:
            sw = 2
            
        hue2 += 0.1
    if sw==2:
        if hue1<=0.2:
            sw = 3
            
        hue1 -= 0.1
    if sw==3:
        if hue3<=0.2:
            sw=4
            
        hue3 -= 0.1
    if sw==4:
        if hue2 <= 0.2:
            sw = 5 
            
        hue2 -= 0.1
    if sw == 5:
        if hue1 >= 0.8:
            sw = 0
            
        hue1 += 0.1
    
    color = (hue1,hue2,hue3)
    bob.pencolor(color) 
    bob.right(i)
    bob.circle(60,i)
    bob.forward(i)
    bob.left(89)
sc.exitonclick()
