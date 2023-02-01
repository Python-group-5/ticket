from Rail_Service import RailService
from Rail_info import Railway

class RailServiceimpl(RailService):

    Rail_list=[]
    def add_Railticket(self,railt):
        if type(railt)==Railway:
            if railt.tic_no>0:
                if railt.tic_price>0:
                    RailServiceimpl.Rail_list.append(railt)
                    print('ticket successfully added')
                else:
                    print('invalid ticket no')
            else:
                print('invalid ticket price')
        else:
            print('invalid ticket cant added ')

    def delete_Railticket(self,rtic):
        if rtic>0:
            for railt in RailServiceimpl.Rail_list:
                if railt.tic_no==rtic:
                    RailServiceimpl.Rail_list.remove(railt)
                    print('Ticket successfully deleted')
                    break
                else:
                    print('invalid ticket no')

    def search_Railticket(self,rtic):
        if rtic>0:
            for railt in RailServiceimpl.Rail_list:
                if railt.tic_no==rtic:
                    return railt
        else:
            print('invalid ticket no')

    def max_price_ticket(self):
        max_price=0.0
        for railt in RailServiceimpl.Rail_list:
            if railt.tic_price>max_price:
                max_price=railt.tic_price
                print('this is maxprice',max_price)

    def min_price_ticket(self):
        min_price=RailServiceimpl.Rail_list[0].tic_price
        for railt in RailServiceimpl.Rail_list:
            if railt.tic_price<min_price:
                min_price=railt.tic_price
                print('this is min price',min_price)
                return min_price


    def list_Railticket(self):
        return RailServiceimpl.Rail_list