import random       # mengimport random

import turtle       # meng-import turtle


#mengatur judul screen dan warna background

scn = turtle.Screen()
scn.bgcolor('white')
scn.title('Colorful Chessboard and Flower')

t = turtle.Turtle()

t.speed(0)              #membuat jadi kecepatan tercepat (0 - 10)
t.shape("turtle")       #agar bentuknya menjadi kura - kura

#membuat screen untuk memasukkan input

ts = t.getscreen()
r = int(ts.numinput('Colorful Chessboard and Flower', 'Enter the number of Rows:', 5, 2, 10))
s = int(ts.numinput('Colorful Chessboard and Flower', 'Enter the square size(pixels):', 20, 2, 30))
p = int(ts.numinput('Colorful Chessboard and Flower', 'Enter the number of petals of the flower:', 8, 3, 25))


########### membuat kotak ###########

t.up()
t.goto(-0.5*r*s, 70)
t.down()

#loop untuk membuat beberapa baris ke bawah

for i in range(r):

    #loop untuk membuat baris kotak ke samping
    
    for i in range(r):

        #untuk membuat warna menjadi random
        
        R = random.random()
        G = random.random()
        B = random.random()
        t.color(R, G, B)
        t.begin_fill()

        #loop untuk membuat kotak persegi 4
        
        for i in range(4):
            t.down()
            t.forward(s)
            t.right(90)
        t.end_fill()
        t.forward(s)
    t.up()
    t.backward(r*s)
    t.right(90)
    t.forward(s)
    t.left(90)


######## membuat bunga #####

sudut = 360/p
t.up()
t.goto(0, 175)
t.down()
arah = 0

#loop untuk membuat petal di bunga

for i in range(p):

    #agar warnanya random
    
    R = random.random()
    G = random.random()
    B = random.random()
    t.color(R, G, B)

    t.circle(70, 60)
    t.left(120)
    t.circle(70, 60)
    t.seth(arah)
    arah += sudut
    t.left(sudut)


#membuat tulisan di akhir program

t.up()
t.goto(0, -(r*s))
t.down()

#mengubah warna tulisan

t.color('black')

#menulis tulisan di bawah chessboard

t.write('Colorful Chessboard of {} Squares and Flower of {} Petals'.format(r**2, p),align='center', font=('Muli', 16,))

#menyembunyikan turtle setelah selesai

t.hideturtle()

input()