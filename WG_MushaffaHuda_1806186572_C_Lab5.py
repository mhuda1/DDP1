
#mengimport sys

import sys


#untuk menginput lokasi file

print('Lokasi file:')
lokasi = input('>>>')


#line code untuk menyimpan error

try:
    infile = open(lokasi, 'r')
except FileNotFoundError:
    print('File tidak ditemukan')
    sys.exit(0)

############################

a = infile.read()   # untuk membaca semua kata yang ada di .txt file
b = a.split()       # untuk membuat list dari semua kata yang ada di .txt file


############################


# print sebagai list perintah untuk input kedua

print('Perintah apa yang ingin dilakukan? ')
print('1. Mencari kata - kata yang dimulai dengan huruf - huruf tertentu')
print('2. Mencari kata - kata yang diakhiri dengan huruf - huruf tertentu')
print('3. Banyakya suatu kata tertentu')

program = int(input('>>> '))




# jika user memilih untuk menjalankan perintah 1

if program == 1:
    print('awalan huruf yang dicari: ')     # mengprint untuk perintah input
    huruf_awal = str(input('>>> '))         # untuk input huruf

    # list untuk menyimpan kata - kata

    kata = []

    # loop untuk menemukan kata

    for i in b:
        if huruf_awal == i[0:len(huruf_awal)]:
            if i not in kata:
                kata.append(i)
            else:
                continue

    # mengprint output

    for i in kata:
        print(i)


# jika user memilih untuk menjalankan perintah 2

if program == 2:
    print('akhiran huruf yang dicari: ')    #mengprint untuk perintah input
    huruf_akhir = str(input('>>> '))        #untuk input huruf

    #list untuk menyimpan kata - kata

    kata_akhir = []

    #loop  untuk menemukan kata

    for i in b:
        if huruf_akhir == i[-1*len(huruf_akhir):]:
            if i not in kata_akhir:
                kata_akhir.append(i)
            else:
                continue

    #mengprint output

    print('berikut adalah kata - kata yang berakhiran dengan "{}":'.format(huruf_akhir))
    for i in kata_akhir:
        print(i)


# jika user memilih untuk menjalankan perintah ketiga

if program == 3:
    print('kata yang ingin dicari: ')       # mengprint untuk perintah input
    kata_dicari = str(input('>>> '))        # untuk input kata
    jml_kata = b.count(kata_dicari)

    # mengprint output
    print(jml_kata)



# jika user memilih untuk menjalankan perintah diluar list perintah yang ada

if program > 3:
    print('perintah {} tidak ditemukan'.format(program))


############################