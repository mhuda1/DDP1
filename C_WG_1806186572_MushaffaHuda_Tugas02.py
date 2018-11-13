import random as r      # mengimport random

import turtle as t      # mengimport turtle

import math             # mengimport math


# function untuk memilih file lewat GUI Window

def choose_file():
 """Prompts user to choose file to load via GUI-based modal window."""

 import tkinter

 from tkinter import filedialog

 root_window = tkinter.Tk()
 root_window.withdraw()

 return filedialog.askopenfilename()


# fungsi untuk menentukan arah posisi awal

def arah(posisi_x, posisi_y):
    t.up()
    t.goto(posisi_x, posisi_y)
    t.down()
    t.seth(0)

# fungsi untuk membuat persegi

def kotak(posisi_x, posisi_y, sisi):
    arah(posisi_x, posisi_y)
    for i in range(4):
        t.fd(sisi)
        t.right(90)

# fungsi untuk membuat lingkaran

def lingkaran(posisi_x, posisi_y, rad):
    arah(posisi_x, posisi_y)
    t.circle(rad, 360)

# fungsi untuk membuat persegi - panjang

def persegi_panjang(posisi_x, posisi_y, lebar, tinggi):
    arah(posisi_x, posisi_y)
    for i in range(2):
        t.fd(lebar)
        t.left(90)
        t.fd(tinggi)
        t.left(90)

# fungsi untuk membuat pentagon

def pentagon(posisi_x, posisi_y, sisi):
    arah(posisi_x, posisi_y)
    for i in range(5):
        t.fd(sisi)
        t.left(72)

# fungsi untuk membuat checkerboard

def checkerboard(posisi_x, posisi_y, row, size):
    arah(posisi_x, posisi_y)
    for i in range(row):
        for i in range(row):
            for i in range(4):
                t.down()
                t.forward(size)
                t.right(90)
            t.forward(size)
        t.up()
        t.backward(row*size)
        t.right(90)
        t.forward(size)
        t.left(90)

# fungsi untuk membuat flower

def flower(posisi_x, posisi_y, petal):
    sudut = 360/petal
    a = 0
    arah(posisi_x, posisi_y)
    for i in range(petal):
        t.circle(70, 60)
        t.left(120)
        t.circle(70,60)
        t.seth(a)
        a += sudut
        t.left(sudut)


# fungsi main program untuk menjalankan semuanya

def main():
    try:    # untuk error handling

        """main program untuk membaca sebuah text file input dan
        menggambarnya di program turtle """

        selected_file = choose_file()
        
        print('Selected file: {}'.format(selected_file))

        # untuk membuka file yang telah dipilih

        infile = open(selected_file, 'r')
        lst = infile.readlines()
        infile.close()

        # untuk membuat list dari per - line dan memecahnya jadi per kata
        
        new_lst = []
        for i in lst:
            new_lst.append(i.split())
        
        # loop untuk mengiterasi setiap line
        
        for i in range(len(new_lst)):

            # untuk membuat judul dari window turtle

            if i == 0:
                t.title(' '.join(new_lst[0][:len(new_lst[0])-1]) + ' | ' + ''.join(new_lst[0][-1:]))
            
            # untuk membuat semua bentuk dengan warna yang dipilih

            elif i > 0:
                
                # untuk mengubah turtle menjadi warna yang diinginkan

                if new_lst[i][0] == 'color':
                    t.colormode(255)
                    t.color(int(new_lst[i][1]), int(new_lst[i][2]), int(new_lst[i][3]))
                    t.up()
                
                # membuat bentuk kotak(persegi)

                elif new_lst[i][0] =='square':
                    try:
                        posisi_x = int(new_lst[i][1])
                        posisi_y = int(new_lst[i][2])
                        sisi = int(new_lst[i][3])
                        kotak(posisi_x, posisi_y, sisi)
                    except:
                        print('error input at line {}'.format(i+1))
                
                # membuat bentuk lingkaran

                elif new_lst[i][0] =='circle':
                    try:
                        posisi_x = int(new_lst[i][1])
                        posisi_y = int(new_lst[i][2])
                        rad = int(new_lst[i][3])
                        lingkaran(posisi_x, posisi_y, rad)
                    except:
                        print('error input at line {}'.format(i+1))
                
                # membuat bentuk persegi panjang

                elif new_lst[i][0] =='rectangle':
                    try:
                        posisi_x = int(new_lst[i][1])
                        posisi_y = int(new_lst[i][2])
                        lebar = int(new_lst[i][3])
                        tinggi = int(new_lst[i][4])
                        persegi_panjang(posisi_x, posisi_y, lebar, tinggi)
                    except:
                        print('error input at line {}'.format(i+1))                        
                
                # membuat bentuk pentagon

                elif new_lst[i][0] =='pentagon':
                    try:
                        posisi_x = int(new_lst[i][1])
                        posisi_y = int(new_lst[i][2])
                        sisi = int(new_lst[i][3])
                        pentagon(posisi_x, posisi_y, sisi)
                    except:
                        print('error input at line {}'.format(i+1))
                
                # membuat bentuk bunga

                elif new_lst[i][0] =='flower':
                    try:
                        posisi_x = int(new_lst[i][1])
                        posisi_y = int(new_lst[i][2])
                        petal = int(new_lst[i][3])
                        flower(posisi_x, posisi_y, petal)   
                    except:
                        print('error input at line {}'.format(i+1))
                
                # membuat bentuk checkerboard

                elif new_lst[i][0] =='checkerboard':
                    try:
                        posisi_x = int(new_lst[i][1])
                        posisi_y = int(new_lst[i][2])
                        row = int(new_lst[i][3])
                        size = int(new_lst[i][4])
                        checkerboard(posisi_x, posisi_y, row, size)
                    except:
                        print('error input at line {}'.format(i+1))

        t.exitonclick()

    except:     # untuk error handling
        print('program tidak bisa dijalankan aka tidak VALID')

if __name__ =='__main__':
    main()