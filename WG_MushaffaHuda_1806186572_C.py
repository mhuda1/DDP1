def factor_tree(n): # membuat function untuk mencari faktor
    faktor = [] #untuk menyimpan angka faktor
    div = 2 # sebagai pembagi awal

    a = [] #untuk menyimpan pembagi
    b = [] #untuk menyimpan jumlah pembagi

    #membuat while untuk menemukan angka - angka faktor
    while div <= n:
        if n % div == 0:
            n/=div
            faktor.append(div)

        else:
            div += 1
    #untuk membuat loop memasukkan angka ke a, b
    for i in faktor:
        if i not in a:
            a.append(i)
            b.append(faktor.count(i))

    idx = 0 #counter untuk index

    #untuk mengeprint angka2 faktor
    for i in range(len(a)):
        if i != (len(a)-1):
            print(a[idx],'^',b[idx],' x ', end = '')
            idx += 1
        else:
            print(a[idx], '^', b[idx], end='')
    









