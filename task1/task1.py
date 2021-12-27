import sys

if __name__ == '__main__':
#если программа запускается через аргументы командной строки
    if sys.argv and len(sys.argv)>2:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
#если программа запускается не из консоли	  
    else:
        n,m = map(int, input().split(' '))
    #print(n + m)
	
    i = 1
    while True:
        print(i, end='')
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    print()
  

#if __name__ == '__main__':
#  main()