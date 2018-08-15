
import turtle
import time

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




def riddle1():
    
    

    print("How many trees are cut down per year for toilet paper?")
    print(" 1 = 2000, 2 = 12000, 3 = 27000, 4 = 120000")
    user_answer = int(input("What number would you like to choose?"))
    if user_answer == 3:
        print('HINT: in room 1 the best door is 1+1-1+1-1')
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

def chose_door():
    global u_door
    global current_room
    global room_count

    
    
    roomT.clear()
    roomT.penup()
    roomT.hideturtle()
    roomT.goto(0,350)
    roomT.write('Room: ' + str(room_count), move = True, align = 'center', font=("Times New Roman",30,"normal"))
    


    
    draw_doors()
    

    #(current_room)(u_door)
        
def room_0(u_door):
    #riddle2()
    if u_door == 1:
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
    if u_door == 1:
        print('oh no its a trap')
        current_room = room_0
        room_count = 0
        chose_door()
    elif u_door == 2:
        print('You made it!')
        current_room = room_3
        room_count += 1
        chose_door
    elif u_door == 3:
        print('oh no its a trap')
        current_room = room_0
        chose_door()
def room_3(u_door):
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
    #global current_room
    
    
    door1 = turtle.clone()
    door2 = turtle.clone()
    door3 = turtle.clone()
    
    door1.penup()
    door2.penup()
    door3.penup()

    door1.speed(0)
    door2.speed(0)
    door3.speed(0)
    
    screen.addshape('door1.gif')
    door1.shape('door1.gif')
    screen.addshape('door2.gif')
    door2.shape('door2.gif')
    screen.addshape('door3.gif')
    door3.shape('door3.gif')

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
    


    
     
    #print()


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
             
current_room = room_0
timer()
#riddle1()                    
chose_door()
#door1.onclick(fun_door1)
#door2.onclick(fun_door2)
#door3.onclick(fun_door3)
turtle.mainloop()


