
import turtle
import time
import random


count_riddle = 1
roomT = turtle.clone()
room_count = 0
u_door = None
n = 100
print("You are stuck in an infinite loop! You need to find your way out! Wait! \
I smell a break around here! Go find it before you go insane in this horrible\
 place!You can start by choosing one of these three doors i guess?")
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


screen.addshape('door1.gif')
screen.addshape('door2.gif')
screen.addshape('door3.gif')
screen.addshape('door4.gif')
screen.addshape('door5.gif')
screen.addshape('door6.gif')
screen.addshape('door7.gif')

door_shapes = ['door1.gif', 'door2.gif', 'door3.gif', 'door4.gif', 'door5.gif', 'door6.gif', 'door7.gif']


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



def ask_riddle():

    door1.hideturtle()
    door2.hideturtle()
    door3.hideturtle()

    riddle_list=["How many trees are cut down per year for toilet paper?","how many sea creaturs die due to plastic polution each year?","how old are the world's oldest trees?","how many plastic water buttles used in year??"]
    global count_riddle

    riddleHL.goto(0,250)
    riddleT1.goto(-100, 100)
    riddleT2.goto(100, 100)
    riddleT3.goto(100, -100)
    riddleT4.goto(-100, -100)

    riddleHL.write(riddle_list[count_riddle], move = True, align = 'center', font=("David",20,"normal"))
    riddleT1.write('2,000', move = True, align = 'center', font=("David",30,"normal"))
    riddleT2.write('12,000', move = True, align = 'center', font=("David",30,"normal"))
    riddleT3.write('27,000', move = True, align = 'center', font=("David",30,"normal"))
    riddleT4.write('120,000', move = True, align = 'center', font=("David",30,"normal"))

    riddleT1.goto(-120, 100)
    riddleT2.goto(80, 100)
    riddleT3.goto(80, -100)
    riddleT4.goto(-120, -100)

    riddleT1.onclick(riddle_answer1)
    riddleT2.onclick(riddle_answer2)
    riddleT3.onclick(riddle_answer3)
    riddleT4.onclick(riddle_answer4)

    s

    if count_riddle == 2:
        riddleHL.goto(0,250)
        riddleT1.goto(-100, 100)
        riddleT2.goto(100, 100)
        riddleT3.goto(100, -100)
        riddleT4.goto(-100, -100)

        riddleHL.write('how many sea creaturs die due to plastic polution each year?', move = True, align = 'center', font=("David",20,"normal"))
        riddleT1.write('100,000', move = True, align = 'center', font=("David",30,"normal"))
        riddleT2.write('500,000', move = True, align = 'center', font=("David",30,"normal"))
        riddleT3.write('750,000', move = True, align = 'center', font=("David",30,"normal"))
        riddleT4.write('1,000,000', move = True, align = 'center', font=("David",30,"normal"))

        riddleT1.goto(-120, 100)
        riddleT2.goto(80, 100)
        riddleT3.goto(80, -100)
        riddleT4.goto(-120, -100)

        riddleT1.onclick(riddle_answer1)
        riddleT2.onclick(riddle_answer2)
        riddleT3.onclick(riddle_answer3)
        riddleT4.onclick(riddle_answer4)
    

        
         
    '''
    

    if count_riddle = 3:

    if count_riddle = 4:
    '''


'''

def riddle1():
    
    

    print("How many trees are cut down per year for toilet paper?")
    print(" 1 = 2000, 2 = 12000, 3 = 27000, 4 = 120000")
    user_answer = int(input("What number would you like to choose?"))
    if user_answer == 3:
        print('HINT: in room 1 the bes
        t door is 1+1-1+1-1')
    else:
        print('wrong! better luck next time')

def riddle2():
    print("how many sea creaturs die due to plastic polution each year?")
    print("1 =100,000, 2 =500,000 , 3=750,000 , 4 =1,000,000")
    user_answer= int(input("what number would you like to choose?"))
    if user_answer == 4:
       print("HINT:in room number 2 the third door is the worst")
    else:
print('wrong! better luck next time')

def riddle3():
    print("how old are the world's oldest trees?")
    print("1 =3,000, 2 =4,600 , 3=7,200 , 4 =12,050")
    user_answer= int(input("what number would you like to choose?"))
    if user_answer == 2:
       print("HINT:In room number 3 the third door isnt the best choice")
    else:
        print('wrong! better luck next time')

def riddle4():
    print("how many plastic water buttles used in year??")
    print("1 =50 billion,  2 =20 billion , 3=billion , 4 =1,000,000")
    user_answer= int(input("what number would you like to choose?"))
    if user_answer == 1:
       print("HINT:In room number 4 doors 2997/999 and 1000-999")
    else:
        print('wrong! better luck next time')
        ###############################################################
'''
def chose_door():
    global u_door
    global current_room
    

    
    
    roomT.clear()
    roomT.penup()
    roomT.hideturtle()
    roomT.goto(0,350)
    roomT.write('Room: ' + str(room_count), move = True, align = 'center', font=("Times New Roman",30,"normal"))
    


    
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
        print('You made it!')
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
        print('you made it. You have broken the loop!')
        room_count += 1
        quit()
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
    


    
     

    print()


def fun_door1(x, y):
    print('clicked door 1!')
    global u_door, door_clicked
    u_door = 1
    door_clicked = True
    enter_door()
def fun_door2(x, y):
    global u_door, door_clicked
    u_door = 2
    door_clicked = True
    enter_door()
def fun_door3(x, y):
    global u_door, door_clicked
    u_door = 3
    door_clicked = True
    enter_door()


def riddle_answer1(x,y):
    print('oh no wrong answer')
    draw_doors()

def riddle_answer2(x,y):
    print('oh no wrong answer')
    draw_doors()

def riddle_answer3(x,y):
    print('HINT: in room number 1 the right door is x/2 = 4')
    draw_doors()

def riddle_answer4(x,y):
    print('oh no wrong answer')
    draw_doors()
             
current_room = room_0
timer()
#riddle1()                    
chose_door()
#door1.onclick(fun_door1)
#door2.onclick(fun_door2)
#door3.onclick(fun_door3)
turtle.mainloop()


