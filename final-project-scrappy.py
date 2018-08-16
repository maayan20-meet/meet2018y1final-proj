
import turtle
import time
import random
riddle2_asked = False
riddle3_asked = False
riddle4_asked = False
count_riddle = 0

room_count = 0
u_door = None
n = 100

riddle1_asked = False
print("You are stuck in an infinite loop! You need to find your way out! Wait! \
I smell a break around here! Go find it before your laptop runs out of battery!\
Start by answering this riddle I guess?")
screen = turtle.Screen()
clock = turtle.Turtle()        
#hello team tbd
def timer():
    global n
    n = n - 1
    clock.penup()
    clock.hideturtle()
    clock.goto(0,300)
    clock.clear()
    clock.write(str(n), move = True, align = 'center', font=("Times New Roman",30,"normal"))
    if n == 0:
        print("Your battery ran out! Good luck next time!")
        quit()
    turtle.ontimer(timer, 1000)


#door1 = turtle.clone()
#door2 = turtle.clone()
#door3 = turtle.clone()
riddle1_answer = ["Wrong answer!, no hint for you!  now, can you move forward by chosing one of this doors?", "Wrong answer!, no hint for you!  now, can you move forward by chosing one of this doors?", "Oh! You made it! Here's a hint!: In room number 0 the best door is 1+1-1+1-1=x  now, can you move forward by chosing one of this doors?", "Wrong answer!, no hint for you!  now, can you move forward by chosing one of this doors?"]
riddle2_answer = ["Wrong answer!", "Wrong answer!", "Wrong answer!", "Oh! You made it! Here's a hint!: In room number 1 the best door is 4 * x = 8"]
riddle3_answer = ["Wrong answer!", "Oh! you made it! Here's a hint : in room number 2 the best door is the first prime number","Wrong answer!","Wrong answer!"]
riddle4_answer = ['Worng answer!', 'Nice! here is a hint: In room number 3 the number of door sounds like a train horn!', 'Worng answer', 'Worng answer'] 
answer_list = [riddle1_answer, riddle2_answer,riddle3_answer, riddle4_answer]



screen.addshape('door1.gif')
screen.addshape('door2.gif')
screen.addshape('door3.gif')
screen.addshape('door4.gif')
screen.addshape('door5.gif')
screen.addshape('door6.gif')
screen.addshape('door7.gif')
screen.addshape('door2a(1).gif')
#screen.addshape('noam.gif')
#screen.addshape('mona.gif')
#screen.addshape('judeh.gif')
#screen.addshape('maayan.gif')
door_shapes = ['door1.gif', 'door2.gif', 'door3.gif', 'door4.gif', 'door5.gif', 'door6.gif', 'door7.gif', 'door2a(1).gif']


door1 = turtle.clone()
door2 = turtle.clone()
door3 = turtle.clone()

riddleT1 = turtle.clone()
riddleT2 = turtle.clone()
riddleT3 = turtle.clone()
riddleT4 = turtle.clone()
riddleHL = turtle.clone()

riddleT1.speed(0)
riddleT2.speed(0)
riddleT3.speed(0)
riddleT4.speed(0)
riddleHL.speed(0)

riddleT1.penup()
riddleT2.penup()
riddleT3.penup()
riddleT4.penup()
riddleHL.penup()

riddleHL.hideturtle()



#!/usr/bin/python
# -*- coding: utf-8 -*-


def ask_riddle():
    global riddle1_asked, riddle2_asked, riddle3_asked, riddle4_asked, \
        count_riddle

    door1.hideturtle()
    door2.hideturtle()
    door3.hideturtle()

    if count_riddle >= 4:
        draw_doors()

    if count_riddle == 0 and not riddle1_asked:
        door1.hideturtle()
        door2.hideturtle()
        door3.hideturtle()

        riddle_list = \
            ['How many trees are cut down per year for toilet paper?',
             'how many sea creaturs die due to plastic polution each year?'
             , "how old are the world's oldest trees?",
             'how many plastic water buttles used in year??']

        riddleHL.goto(0, 250)
        riddleT1.goto(-100, 100)
        riddleT2.goto(100, 100)
        riddleT3.goto(100, -100)
        riddleT4.goto(-100, -100)

        riddleHL.write(riddle_list[count_riddle], move=True,
                       align='center', font=('David', 20, 'normal'))
        riddleT1.write('2,000', move=True, align='center', font=('David'
                       , 30, 'normal'))
        riddleT2.write('12,000', move=True, align='center',
                       font=('David', 30, 'normal'))
        riddleT3.write('27,000', move=True, align='center',
                       font=('David', 30, 'normal'))
        riddleT4.write('120,000', move=True, align='center',
                       font=('David', 30, 'normal'))

        riddleT1.showturtle()
        riddleT2.showturtle()
        riddleT3.showturtle()
        riddleT4.showturtle()

        riddleT1.shape('square')
        riddleT2.shape('square')
        riddleT3.shape('square')
        riddleT4.shape('square')

        riddleT1.goto(-100, 100)
        riddleT2.goto(110, 100)
        riddleT3.goto(110, -100)
        riddleT4.goto(-70, -100)

        riddleT1.onclick(riddle_answer1)
        riddleT2.onclick(riddle_answer2)
        riddleT3.onclick(riddle_answer3)
        riddleT4.onclick(riddle_answer4)

        riddle1_asked = True

    if count_riddle == 1 and not riddle2_asked:
        door1.hideturtle()
        door2.hideturtle()
        door3.hideturtle()

        riddleT1.showturtle()
        riddleT2.showturtle()
        riddleT3.showturtle()
        riddleT4.showturtle()

        riddleHL.goto(0, 250)
        riddleT1.goto(-100, 100)
        riddleT2.goto(100, 100)
        riddleT3.goto(100, -100)
        riddleT4.goto(-100, -100)

        riddleHL.write('how many sea creaturs die due to plastic polution each year?'
                       , move=True, align='center', font=('David', 20,
                       'normal'))
        riddleT1.write('100,000', move=True, align='center',
                       font=('David', 30, 'normal'))
        riddleT2.write('500,000', move=True, align='center',
                       font=('David', 30, 'normal'))
        riddleT3.write('750,000', move=True, align='center',
                       font=('David', 30, 'normal'))
        riddleT4.write('1,000,000', move=True, align='center',
                       font=('David', 30, 'normal'))

        riddleT1.onclick(riddle_answer1)
        riddleT2.onclick(riddle_answer2)
        riddleT3.onclick(riddle_answer3)
        riddleT4.onclick(riddle_answer4)
        riddle2_asked = True

    if count_riddle == 2 and not riddle3_asked:
        door1.hideturtle()
        door2.hideturtle()
        door3.hideturtle()

        riddle_list = \
            ['How many trees are cut down per year for toilet paper?',
             'how many sea creaturs die due to plastic polution each year?'
             , "how old are the world's oldest trees?",
             'how many plastic water buttles used in year??']

        riddleHL.goto(0, 250)
        riddleT1.goto(-100, 100)
        riddleT2.goto(100, 100)
        riddleT3.goto(100, -100)
        riddleT4.goto(-100, -100)

        riddleHL.write(riddle_list[count_riddle], move=True,
                       align='center', font=('David', 20, 'normal'))
        riddleT1.write('3,000', move=True, align='center', font=('David'
                       , 30, 'normal'))
        riddleT2.write('4,600', move=True, align='center', font=('David'
                       , 30, 'normal'))
        riddleT3.write('7,200', move=True, align='center', font=('David'
                       , 30, 'normal'))
        riddleT4.write('20,010', move=True, align='center',
                       font=('David', 30, 'normal'))

        riddleT1.showturtle()
        riddleT2.showturtle()
        riddleT3.showturtle()
        riddleT4.showturtle()

        riddleT1.shape('square')
        riddleT2.shape('square')
        riddleT3.shape('square')
        riddleT4.shape('square')

        riddleT1.goto(-30, 120)
        riddleT2.goto(190, 120)
        riddleT3.goto(190, -80)
        riddleT4.goto(0, -80)

        riddleT1.onclick(riddle_answer1)
        riddleT2.onclick(riddle_answer2)
        riddleT3.onclick(riddle_answer3)
        riddleT4.onclick(riddle_answer4)

        riddle3_asked = True

    if count_riddle == 3 and not riddle4_asked:
        door1.hideturtle()
        door2.hideturtle()
        door3.hideturtle()

        riddle_list = \
            ['How many trees are cut down per year for toilet paper?',
             'how many sea creaturs die due to plastic polution each year?'
             , "how old are the world's oldest trees?",
             'how many plastic water buttles used in year??']

        riddleHL.goto(0, 250)
        riddleT1.goto(-100, 100)
        riddleT2.goto(100, 100)
        riddleT3.goto(100, -100)
        riddleT4.goto(-100, -100)

        riddleHL.write(riddle_list[count_riddle], move=True,
                       align='center', font=('David', 20, 'normal'))
        riddleT1.write('50 billion', move=True, align='center',
                       font=('David', 30, 'normal'))
        riddleT2.write('20 billion', move=True, align='center',
                       font=('David', 30, 'normal'))
        riddleT3.write('1.6 billion', move=True, align='center',
                       font=('David', 30, 'normal'))
        riddleT4.write('57 million', move=True, align='center',
                       font=('David', 30, 'normal'))

        riddleT1.showturtle()
        riddleT2.showturtle()
        riddleT3.showturtle()
        riddleT4.showturtle()

        riddleT1.shape('square')
        riddleT2.shape('square')
        riddleT3.shape('square')
        riddleT4.shape('square')

        riddleT1.goto(-30, 120)
        riddleT2.goto(190, 120)
        riddleT3.goto(190, -80)
        riddleT4.goto(0, -80)

        riddleT1.onclick(riddle_answer1)
        riddleT2.onclick(riddle_answer2)
        riddleT3.onclick(riddle_answer3)
        riddleT4.onclick(riddle_answer4)

        riddle4_asked = True

    




def chose_door():
    global u_door
    global current_room
    

    
    
    turtle.clear()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0,350)
    turtle.write('Room: ' + str(room_count), move = True, align = 'center', font=("Times New Roman",30,"normal"))


    
    ask_riddle()
    

    #(current_room)(u_door)
        
def room_0(u_door):
    #riddle2()
    if u_door == 1:
        global current_room, room_count
        print('You made it!')
        current_room = room_1
        room_count += 1
        chose_door()
    elif u_door == 2:
        print('oh no its a trap')
        current_room = room_0
        room_count = 0
        chose_door()
    elif u_door == 3:
        print('oh no its a trap')
        current_room = room_0
        room_count = 0
        chose_door()

def room_1(u_door):
    #riddle3()
    global current_room, room_count
    if u_door == 1:
        print('oh no its a trap')
        current_room = room_0
        room_count = 0
        chose_door()
    elif u_door == 2:

        print('hell yeah! you made it!')
        current_room = room_2
        room_count += 1
        chose_door()
    elif u_door == 3:

        print('oh no its a trap')
        current_room = room_0
        room_count = 0
        chose_door()

def room_2(u_door):
    #riddle4()
    global current_room, room_count
    if u_door == 1:
        print('oh no its a trap')
        current_room = room_0
        room_count = 0
        chose_door()
    elif u_door == 2:
        print('You made it!')
        current_room = room_3
        room_count += 1
        chose_door()
    elif u_door == 3:
        print('oh no its a trap')
        current_room = room_0
        room_count = 0
        chose_door()

def room_3(u_door):
    global current_room, room_count
    if u_door == 1:
        print('oh no its a trap')
        current_room = room_0
        room_count = 0
        
        chose_door()
    elif u_door == 2:
        print('You made it to the next room')
        room_count += 1
        current_room = room_4
        chose_door()
    elif u_door== 3:
        print(' oh no its a trap')
        current_room = room_0
        room_count = 0
        chose_door()

def room_4(u_door):
    global current_room, room_count
    if u_door == 1:
        print('You did it!')
        current_room = room_5
        room_count += 1
        chose_door()
    elif u_door == 2:
        print('oh no its a trap')
        current_room = room_0
        room_count = 0
        chose_door()
        
    elif u_door== 3:
        print(' oh no its a trap')
        current_room = room_0
        room_count = 0
        chose_door()

def room_5(u_door):
    global current_room, room_count
    if u_door == 1:
        print('oh no its a trap')
        current_room = room_0
        room_count = 0
        chose_door()
    elif u_door == 2:
        print('oh no its a trap!')
        current_room = room_0
        room_count = 0
        chose_door()
        
    elif u_door== 3:
        print('You made it to the next room!')
        current_room = room_6
        room_count += 1
        chose_door()

def room_6(u_door):
    global current_room, room_count
    if u_door == 1:
        #current_room = room_7
        room_count += 1
        print('you did it, you broke the loop!')
        quit()
    elif u_door == 2:
        print('oh no its a trap!')
        current_room = room_0
        room_count = 0
        
    elif u_door== 3:
        print(' oh no its a trap')
        current_room = room_0
        room_count = 0
        chose_door()


def draw_doors():
    global u_door, screen
    global current_room
    
    riddleT1.clear()
    riddleT2.clear()
    riddleT3.clear()
    riddleT4.clear()
    riddleHL.clear()

    riddleT1.hideturtle()
    riddleT2.hideturtle()
    riddleT3.hideturtle()
    riddleT4.hideturtle()
    riddleHL.hideturtle()

    door1.showturtle()
    door2.showturtle()
    door3.showturtle()
       
    
    door1.penup()
    door2.penup()
    door3.penup()

    

    door1.speed(0)
    door2.speed(0)
    door3.speed(0)
    
    
    door1.shape(random.choice(door_shapes))
    
    door2.shape(random.choice(door_shapes))
    
    door3.shape(random.choice(door_shapes))

    

    door1.showturtle()
    door2.showturtle()
    door3.showturtle()

    door1.goto(-200,0)
    door2.goto(0, 0)
    door3.goto(200, 0)

    door_clicked = False
    
    door1.onclick(fun_door1)
    door2.onclick(fun_door2)
    door3.onclick(fun_door3)

    
    #while not door_clicked:
        #door_clicked = door_clicked
     #   pass
    
def enter_door():
    print(u_door)
    (current_room)(u_door)
    


def fun_door1(x, y):
    global u_door
    u_door = 1
    enter_door()
def fun_door2(x, y):
    global u_door
    u_door = 2
    enter_door()
def fun_door3(x, y):
    global u_door
    u_door = 3
    enter_door()


def riddle_answer1(x,y):
    global count_riddle
    print(answer_list[count_riddle][0])
    count_riddle += 1
    draw_doors()

def riddle_answer2(x,y):
    global count_riddle
    print(answer_list[count_riddle][1])
    count_riddle += 1
    draw_doors()

def riddle_answer3(x,y):
    global count_riddle
    print(answer_list[count_riddle][2])
    count_riddle += 1
    draw_doors()
    

def riddle_answer4(x,y):
    global count_riddle
    print(answer_list[count_riddle][3])
    count_riddle += 1
    draw_doors()
             
current_room = room_0
timer()
#riddle1()                    
chose_door()
#door1.onclick(fun_door1)
#door2.onclick(fun_door2)
#door3.onclick(fun_door3)
turtle.mainloop()


