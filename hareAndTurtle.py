# Sobika Thapa
#Only a couple of scenic elements (the fractal tree and the sun) were inspired by information found online,
#and made sure to change them and adapt them to the project.

##All the icons/gifs used in this project were obtained from: flaticon.com


import turtle
sky = turtle.Turtle()
sky.hideturtle()
bob=turtle.Turtle()
bob.hideturtle()
wn=turtle.Screen()
sun = turtle.Turtle()
sun.hideturtle()
road=turtle.Turtle()
road.hideturtle()
line=turtle.Turtle()
line.hideturtle()
field = turtle.Turtle()
field.hideturtle()
field2 = turtle.Turtle()
field2.hideturtle()
school = turtle.Turtle()
school.hideturtle()
girl = turtle.Turtle()
girl.hideturtle()



turtle.bgcolor("olive drab")
wn.setworldcoordinates(-1000,-1000,1000,1000)


def rectangle_left(x, width, height, myturtle, angle):
    for i in range(x):
        myturtle.forward(width)
        myturtle.left(angle)
        myturtle.forward(height)
        myturtle.left(angle)
        
def rectangle_right(x, width, height, myturtle, angle):
    for i in range(x):
        myturtle.forward(width)
        myturtle.right(angle)
        myturtle.forward(height)
        myturtle.right(angle)

def draw_sky():
    sky.speed(10)
    sky.hideturtle()
    sky.up()
    sky.goto(-1100,800)
    sky.color('light blue', 'light blue')
    sky.down()
    sky.begin_fill()
    rectangle_left(2, 2100, 250, sky, 90)
    sky.end_fill()
draw_sky()

wn.addshape("smallclouds.gif")
def draw_cloud(cloud, cl, x,y):
    cloud.hideturtle()
    cloud.shape(cl)
    cloud.speed(10)
    cloud.up()
    cloud.goto(x,y)
    cloud.showturtle()

cloud1=turtle.Turtle()
cloud2=turtle.Turtle()
cloud3=turtle.Turtle()
cloud4=turtle.Turtle()
cloud5=turtle.Turtle()
draw_cloud(cloud1,"smallclouds.gif",-900,950)
draw_cloud(cloud2,"smallclouds.gif",-300,850)
draw_cloud(cloud3,"smallclouds.gif",100,920)
draw_cloud(cloud4,"smallclouds.gif",600,870)
draw_cloud(cloud5,"smallclouds.gif",-700,930)
##draws a sun
def draw_sun():
    sun.speed(10)
    sun.hideturtle()
    sun.up()
    sun.goto(750,900)
    sun.down()
    sun.color('yellow', 'yellow')
    sun.begin_fill()
    for i in range(37):
        sun.forward(200)
        sun.left(170)
    sun.end_fill()
    sun.hideturtle()
draw_sun()

##To draw the road
def draw_road():
    road.speed(10)
    road.color('sienna','sienna')
    road.up()
    road.hideturtle()
    road.goto(-1100,-250)
    road.down()
    road.begin_fill()
    rectangle_left(2, 2100, 500, road, 90)
    road.end_fill()
draw_road()
    
##To draw the starting line
def start_line():
    bob.speed(10)
    bob.hideturtle()
    bob.up()
    bob.color('white')
    bob.goto(-950,275)
    bob.right(90)
    bob.up()
    start = "START"
    for i in range(5):
        bob.forward(100)
        bob.write(start[i])
    bob.forward(100)
    bob.goto(-900,250)
    bob.down()
    bob.forward(500)
start_line()

##To draw the finish line:
##To draw the finish line:
def finish_line():
    bob.up()
    bob.color('white')
    bob.goto(900, 275)
    bob.up()
    finish = "FINISH"
    for i in range(6):
        bob.forward(83)
        bob.write(finish[i])
    bob.forward(83)
    bob.goto(850,250)
    bob.down()
    bob.forward(500)
    bob.hideturtle()
finish_line()

def lines():
    line.color('white')
    line.up()
    line.goto(-900,150)
    line.down()
    line.forward(1750)
    line.up()
    line.right(90)
    line.forward(100)
    line.right(90)
    line.down()
    line.forward(1750)
    line.up()
    line.left(90)
    line.forward(100)
    line.left(90)
    line.down()
    line.forward(1750)
    line.up()
    line.right(90)
    line.forward(100)
    line.right(90)
    line.down()
    line.forward(1750)
    line.hideturtle()
    
lines()

#To insert audience:
wn.addshape("bear.gif")
wn.addshape("bird.gif")
wn.addshape("cow.gif")
wn.addshape("deer.gif")
wn.addshape("monkey.gif")
wn.addshape("sheep.gif")
wn.addshape("squirrel.gif")
wn.addshape("wolf.gif")
bear = turtle.Turtle()
bird = turtle.Turtle()
cow = turtle.Turtle()
deer = turtle.Turtle()
monkey = turtle.Turtle()
sheep = turtle.Turtle()
squirrel = turtle.Turtle()
wolf = turtle.Turtle()
def audience(myturtle, type,x,y):
    myturtle.hideturtle()
    myturtle.shape(type)
    myturtle.up()
    myturtle.goto(x,y)
    myturtle.showturtle()

def animals(a,b,c,d,e,f,g,h):
    
    audience(bear, "bear.gif", a,300)
    audience(bird, "bird.gif", b,300)
    audience(cow, "cow.gif", c,300)
    audience(deer, "deer.gif", d,300)
    audience(monkey, "monkey.gif", e,300)
    audience(sheep, "sheep.gif", f,300)
    audience(squirrel, "squirrel.gif", g,300)
    audience(wolf, "wolf.gif", h,300)
    
animals(-400,-350,-290,-230,-170,-110,-50,10)

##To insert the flowers:
wn.addshape("rose.gif")
wn.addshape("sunflower.gif")
wn.addshape("flower-2.gif")
wn.addshape("flower.gif")
flower = turtle.Turtle()
flower2 = turtle.Turtle()
flower3 = turtle.Turtle()
flower4 = turtle.Turtle()
flower5 = turtle.Turtle()
flower6 = turtle.Turtle()
flower7 = turtle.Turtle()
flower8=turtle.Turtle()
flower9 = turtle.Turtle()

def flower_fct(myturtle, type,x,y):
    myturtle.hideturtle()
    myturtle.shape(type)
    myturtle.up()
    myturtle.goto(x,y)
    myturtle.showturtle()
    
flower_fct(flower, "flower-2.gif", 0,500)
flower_fct(flower2, "flower.gif", -950,600)
flower_fct(flower3, "rose.gif", 100,400)
flower_fct(flower4, "rose.gif", 700,700)
flower_fct(flower5, "flower.gif", 700,400)
flower_fct(flower6, "sunflower.gif", -850,400)
flower_fct(flower7, "sunflower.gif", 200,650)
flower_fct(flower8, "sunflower.gif", 950,700)
flower_fct(flower9, "flower.gif",200,450)

####to draw the baseball field:
t = turtle.Pen()
t.speed(10)
t.hideturtle()
t.up()
t.goto(250,-500)
t.left(180)
t.down()
#
t.color('brown','brown')
def Polygon(myTurtle, sideLength, numSides):
    angle= 270/numSides
    for i in range(1, numSides,1):
        myTurtle.forward(sideLength)
        myTurtle.right(angle)

def drawCircle(myTurtle, rad):
    P=2*rad*3.14
    sideLength= P/270 #360 is the number of sides
    Polygon(myTurtle, sideLength, 270)
    
drawCircle(t, 30)

t.color('brown','brown')
t.hideturtle()
t.begin_fill()
t.left(90)
t.forward(300)
pos = t.position()
field2.up()
field2.hideturtle()
field2.pencolor("white")
field2.speed(10)
field2.goto(pos)
field2.down()
field2.forward(100)
#
t.right(90)
for x in range(100):
    t.forward(6)
    t.right(1)
t.right(91)
t.forward(312)
t.end_fill()
t.hideturtle()
#
#
field.color('brown','brown')
field.hideturtle()
field.speed(10)
field.up()
field.goto(250,-500)
field.left(180)
field.down()
field.begin_fill()
def Polygon2(myTurtle, sideLength, numSides):
    angle= 360/numSides
    for i in range(1, numSides,1):
        myTurtle.forward(sideLength)
        myTurtle.right(angle)

def drawCircle2(myTurtle, rad):
    P=2*rad*3.14
    sideLength= P/360 #360 is the number of sides
    Polygon2(myTurtle, sideLength, 360)
    
drawCircle2(field, 40)
field.end_fill()
field.hideturtle()

field2.right(90)
for x in range(100):
    field2.forward(7.62)
    field2.right(1)
field2.right(88.5)
field2.forward(93)
field2.hideturtle()


##to draw the girls' school:
def draw_school():
    school.speed(10)
    school.hideturtle()
    school.up()
    school.color('beige','beige')
    school.begin_fill()
    school.goto(-500,-500)
    rectangle_right(2, 500, 250, school, 90)

    school.end_fill()
    school.up()
    school.begin_fill()
    school.forward(50)
    school.down()
    school.left(90)
    rectangle_right(2,100,400,school,90)
    school.end_fill()
    school.up()
    school.goto(-200,-750)
    school.down()
    school.color('brown','brown')
    school.begin_fill()
    rectangle_left(2, 175, 75, school, 90)
    door= school.pos()
    school.end_fill()

    ##To write girl's school
    girl.up()
    girl.hideturtle()
    girl.goto(-435,-470)
    girls_school = "HARES' SCHOOL"
    for i in range(13):
        girl.write(girls_school[i])
        girl.forward(30)
draw_school()

def insert_school():
    wn.addshape("bigschool.gif")
    school_turtle = turtle.Turtle()
    school_turtle.hideturtle()
    school_turtle.shape("bigschool.gif")
    school_turtle.up()
    school_turtle.goto(-400,-600)
    school_turtle.showturtle()
#insert_school()

#To draw the tree
def treeDraw(branchLength,tree):
    if branchLength > 2:
        tree.forward(branchLength)
        tree.right(20)
        treeDraw(branchLength-15,tree)
        tree.left(40)
        treeDraw(branchLength-15,tree)
        tree.right(20)
        tree.backward(branchLength)

def main_tree():
    tree = turtle.Turtle()
    tree.hideturtle()
    tree.speed(10)
    tree.up()
    tree.goto(500,400)
    tree.down()
    tree.left(90)
    tree.up()
    tree.backward(100)
    tree.down()
    tree.color("saddle brown")
    treeDraw(100,tree)
    pos_tree= tree.pos()
    

main_tree()

##To bring in contestants:
input("Instructions: Press enter to move on with the dialogues and answer as appropriate when promted.")
input("Narrator: Hello ladies and gentlemen and welcome to the Tortoise vs Hare legendary race!")
input("Take a seat, get comfortable, and get ready to enjoy the show!")
input("But wait...how about we make this more fun?")
input("You can participate too! Just follow the instructions as they pop on the screen.")
print("First, let's welcome under a thunder of applause our first contestant: the speedy, charming Hare! Clap for him to come out! ")
input("Type 'Clap' ")
#
hare = turtle.Turtle()
wn.addshape("rabbit.gif")
hare.shape("rabbit.gif")
hare.speed(3)
hare.up()
hare.goto(-995,-100)

print("Hare: WOOOOO!! Hello everyone! Ready to see me win this?")
R1= input("Do you think the Hare will win the race? Insert Yes or No: ")
if R1 == "Yes":
    input("Hare: Haha! You sure are right!")
elif R1 == "No":
    input("Hare: Hmph...sit back and watch me prove you wrong then.")

print("Narrator: Okay! Now, onto the second contestant: the slow but sure Hare! Clap for him to come out! ")
input("Type 'Clap' ")
tortoise = turtle.Turtle()
wn.addshape("tortoise.gif")
tortoise.shape("tortoise.gif")
tortoise.speed(1)
tortoise.up()
tortoise.goto(-995,100)
input("Narrator: ...haha...well, the Tortoise is a little slow, but better late than never, right?")
input("Narrator: Anyway, let's get this race started! Contestants, at your marks, get, set, go!! *blows horn* ")
input("Hare: Come on Tortoise, I'm giving you a headstart, you go first.")
input("Tortoise: God no. That horn sound was terrifying, I need a moment to collect myself. *hides in his shell*")
input("Hare: Huh, okay. BYE LOSER!!")

hare.speed(3)
hare.forward(400)
print("Hare: Oh! A school for heirs? Should I check it out?")
R2 = input("Type Yes or No: ")
if R2 == "Yes":
    print("Hare: Yay! Let's go in! ")
    hare.goto(-275,-750)
    input("*knock knock*")
    student = turtle.Turtle()
    student.hideturtle()
    wn.addshape("rabbit2.gif")
    student.shape("rabbit2.gif")
    student.up()
    student.left(180)
    student.goto(-200,-750)
    student.showturtle()
    input("Student: Hey, what's up?")
    input("Hare: Just passing by! I saw you guys have a baseball field. Up for a game?")
    input("Student: Sure, let's go!")
    input("Hare: Lead the way!")
    student.right(260)
    student.goto(280,-450)
    hare.goto(240,-500)
    
    input("Narrator: Meanwhile...the tortoise has finally recovered.")
    input("Tortoise: Phew...okay...let's do this...")
    tortoise.forward(300)
    input("Tortoise: *wheeze wheeze*")
    input("Tortoise: I am clearly too old for this...")
    print("Narrator: It seems like the Tortoise needs some encouragement! Tell the tortoise it can do it!")
    R3 = input("Type 'You can do it!'")
    if R3 == "You can do it!":
        input("Tortoise: You're right. Let's keep moving!")
        tortoise.forward(200)
        print(tortoise.pos())
        input("Hare: Oh! It looks like the Tortoise is finally catching up...It was nice playing with you my friend, but I gotta run!")
        input("Student: Okay! Have fun and come back again soon!")
        student.hideturtle()
        hare.left(180)
        student.left(180)
        hare.goto(-275,-750)
        student.goto(-275,-750)
        hare.right(90)
        hare.goto(-495,-100)
        input("Hare: See you not so soon, Tortoise!")
        hare.right(90)
elif R2 == "No":
    input("Hare: Fine...fine, let's just keep moving then.")
    hare.forward(300)
    input("Tortoise: Oh no! The Hare is too fast! There's no hope for me to win. Might as well just take a nap...")
    input("Hare: Haha! You're about right Tortoise! BYE!")
hare.forward(800)

input("Hare: Oh that's a nice-looking tree, and I I could use a nap right now. The Tortoise can't catch up even if it tried after all.")
print("Hare: What do you think? Should I nap for a little bit?")
R4 = input("Type Yes or No: ")
if R4 == "Yes":
    input("Hare: Good choice.")
elif R4 == "No":
    input("Hare: Tsk. You don't get a say in this. I'm napping anyway.")
hare.goto(500,330)
input("Hare: *zzz...zzzz....*")
input("Tortoise: Oh...it looks like the Hare is going to be asleep for a while. Maybe I stand a chance after all?")
input("Narrator: Hey, spectator. You can help the tortoise out! The rules never stated that outside help was forbidden after all...")
print("Here, a lettuce head and an energy drink. Pick which one to give to the tortoise.")
R6 = input("Type 'A' for the lettuce head and 'B' for the energy drink")
if R6 == "A":
    lettuce = turtle.Turtle()
    lettuce.hideturtle()
    wn.addshape("lettuce.gif")
    lettuce.shape("lettuce.gif")
    lettuce.speed(10)
    lettuce.up()
    if R2 == "No":
        lettuce.goto(-925,100)
    elif R2 == "Yes":
        lettuce.goto(-425,100)
    lettuce.showturtle()
    input("Tortoise: No no no. Lettuce won't do anything for me right now. I need something stronger. Try again.")
    lettuce.hideturtle()
    input("Press B to select the energy drink")
    can = turtle.Turtle()
    can.hideturtle()
    wn.addshape("can.gif")
    can.shape("can.gif")
    can.speed(10)
    can.up()
    if R2 == "No":
        can.goto(-925,100)
    elif R2 == "Yes":
        can.goto(-425,100)
    can.showturtle()
    input("Tortoise: *slurp slurp*")
    can.hideturtle()
    input("Tortoise: YEEEEE LET'S DO THIS!")
if R6 == "B":
    can = turtle.Turtle()
    can.hideturtle()
    wn.addshape("can.gif")
    can.shape("can.gif")
    can.speed(10)
    can.up()
    if R2 == "No":
        can.goto(-925,100)
    elif R2 == "Yes":
        can.goto(-425,100)
    can.showturtle()
    input("Tortoise: *slurp slurp*")
    can.hideturtle()
    input("Tortoise: YEEEEE LET'S DO THIS!")
    #print("Tortoise: Hey, spectator, do you think I can do it?")
#R5 = input("Type Yes or No")
#if R5 == "Yes":
#    input("Tortoise: Alright! Let's do this!")
#if R5 == "No":
#    input("Tortoise: I'm sure I can now! Sit back and watch!")
tortoise.goto(400, 100)
input("Hare: *zzzz...zzzzz...*")
input("Tortoise: Shhhh...let's be quiet so that he doesn't wake up...")
tortoise.speed(1)
tortoise.forward(200)
input("Hare: *wakes up* huh? Oh no! The tortoise is already way ahead!")
input("Tortoise: You're finally awake? Well it's too late now. Victory is mine!")
input("Narrator: The Hare could not get his bearings in time.")
tortoise.speed(3)
tortoise.forward(350)
input("Tortoise: See? Your arrogance did not get you anywhere Hare!")
input("Narrator: The race is not always to the swift.")
    
        
        
    







