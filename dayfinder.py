def Find_day(m,n):
    first=lint[m-2]
    
    if n%7==0:
       print(first)
    elif (m==3 and n==6) :
       print(lint[0])
    else:
        print(lint[m+(n%7)-2])

lint= [ 'Mon','Tue','Wed','Thu','Fri','Sat','Sun']
firstday =''
while 1:
    print('WELCOME TO DAY FINDER ')
    print('To Quit Press Q/QUIT')
    print('To Continue press Y/YES')   
    s=input(' ')
    if s=='y' or s== 'yes':
        
        print("Enter Your First Desired Day from the list (For e.g. 1 for Monday/2 for Tueday etc. ")
        print( "1.Mon \n2.Tue \n3.Wed\n4.Thu\n5.Fri\n6.Sat\n7.Sun")
        while firstday not in range(0,8):
            try:
                firstday=int(input(" ENTER HERE   "))
            except:
                print("Please  Enter Only from 1-7")
                
        Num=int(input("Enter the day's Number for which you wanna know the day oF "))
        Find_day(firstday,Num)
            
    elif s=='q' or s=='quit':
        print('THANK YOU , COME AGAIN SOMETIME ')
        break
    else:
        print('please Enter Valid option  ')
        print('||||||||||||||||||||||||||')
        print('||||||||||||||||||||||||||')

