import turtle as t
import colorsys as c
t.bgcolor('black')
t.speed('fastest')
t.pensize(2)
t.hideturtle()
#t.bgcolor('black')
#t.pencolor('red')
for j in range(13):
	for k in range(15):
		for i in range(2):
			t.lt(90)
			t.pencolor(c.hsv_to_rgb(1/(k+1),1/(i+1),1))
			t.circle(100-(j*2),90)
			t.fd(180)
		t.circle(0,24)
t.exitonclick()