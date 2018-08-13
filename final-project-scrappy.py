u_door = None
print("You are stuck in an infinite loop! You need to find your way out! Wait! \
I smell a break around here! Go find it before you go insane in this horrible\
 place!You can start by choosing one of these three doors i guess?")
import turtle
           
#hello team tbd

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

def chose_door(current_room):
    global u_door
    #draw_doors()
    u_door = int(input("What number of door would you like to open?"))
    (current_room)(u_door)
    
    
def room_0(u_door):
    riddle2()
    if u_door == 1:
        print('You made it!')
        chose_door(room_1)
    elif u_door == 2:
        print('oh no its a trap')
        chose_door(room_0)
    elif u_door == 3:
        print('oh no its a trap')
        chose_door(room_0)

def room_1(u_door):
    riddle3()
    if u_door == 1:
        print('oh no its a trap')
        chose_door(room_0)
    elif u_door == 2:
        print('You made it!')
        chose_door(room_2)
    elif u_door == 3: 
        print('oh no its a trap')
        chose_door(room_0)

def room_2(u_door):
    riddle4()
    if u_door == 1:
        print('oh no its a trap')
        chose_door(room_0)
    elif u_door == 2:
        print('You made it!')
    elif u_door == 3:
        print('oh no its a trap')
        chose_door(room_0)
def room_3(u_door):
    if u_door == 1:
        print ('oh no its a trap')
        chose_door(room_0)
    elif u_door == 2:
        print('you made it')
    elif u_door== 3:
        print(' oh no its a trap')
        chose_door(room_0)

'''
def draw_doors():
    global u_door

    door1 = turtle.clone()
    door2 = turtle.clone()
    door3 = turtle.clone()

    door1.penup()
    door2.penup()
    door3.penup()

    door2.shape('square')
    door3.shape('circle')

    door1.goto(-200,0)
    door2.goto(0, 0)
    door3.goto(200, 0)

    
    door1.onclick(fun_door1)
    door2.onclick(fun_door2)
    door3.onclick(fun_door3)


def fun_door1(x, y):
    u_door = 1
def fun_door2(x, y):
    u_door = 2
def fun_door3(x, y):
    u_door = 3
'''              
                     
                                          
                     
riddle1()                    
chose_door(room_0)
