
# function main untuk program #

def main():

    # membuat list of set dari semua set

    n = int(input())
    lst = [eval(input()) for i in range(n)]
    
    # membuat union dari semua set

    set_kosong =set()
    for i in range(len(lst)-1):
        set_kosong = set_kosong.union(lst[i])
    
    # memprint output

    print('>>>')

    # loop untuk mengiterasi setiap set di lst

    for i in range(len(lst)):
        a = set_kosong
        for j in (lst[:i] + lst[1+i:]):
            a = a - j
        if a:
            print(i, '=', a)
        else:
            continue
    

if __name__ == '__main__':
    main()