from Rail_Service_impl import RailServiceimpl
from Rail_info import Railway

railob = RailServiceimpl()

while True:
    print('''
            1.Add Ticket
            2.Delete Ticket
            3.List Ticket
            4.Search Ticket
            5.Max Price
            6.Min Price
            7.Exit
    ''')

    choice=int(input('Enter your choice'))
    if choice in [2,3,4,5,6,7]:
            Rail=railob.list_Railticket()
            if not Railway:
                print('First add Ticket')
                continue

    if choice==1:
            rtic=int(input('enter your ticket'))
            passname=input('enter passsenger name')
            journeyto=input('enter from to journey')
            tprice=float(input('enter ticket price'))
            cat=input('enter ticket category')

            R1=Railway(tno=rtic,pname=passname,jfto=journeyto,price=tprice,cate=cat)
            railob.add_Railticket(R1)

    elif choice==2:
            rtic=int(input('enter the ticket for delete'))
            railob.delete_Railticket(rtic)

    elif choice==3:
            Rail_list=railob.list_Railticket()
            print(Rail_list)

    elif choice==4:
            rtic=int(input('enter the Ticket no'))
            railt=railob.search_Railticket(rtic)
            print('ticket',railt)

    elif choice==5:
            railt=railob.max_price_ticket()

    elif choice==6:
            railt=railob.min_price_ticket()

    else:
        print('invalid choice')

    print('Execution Completed')