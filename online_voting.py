# import mysql.connector
# mydb = mysql.connector.connect(
#     host='localhost', user='root', passwd='Yamaha@Rx100', database='online_voting_poll')
# mycursor = mydb.cursor()


# class checking_details:
#     def __init__(self, name, voter_id):
#         self.name = name
#         self.voter_id = voter_id

#     def isexists_user(self):
#         mycursor.execute(
#             'select user_id,name,voter_id from user_details where voter_id like %s', (self.voter_id,))
#         details = mycursor.fetchall()
#         for i in details:
#             if i[2] == self.voter_id:
#                 return i[0]


# if __name__ == '__main__':
#     name = input('enter your name: ')
#     voter_id = int(input('enter your voter id: '))
#     address = input('enter your address: ')
#     aadhaar_no = int(input('enter your aadhaar_no: '))
#     mycursor.execute('insert into user_details(name,voter_id,address,aadhaar_no) values(%s,%s,%s,%s)',
#                      (name, voter_id, address, aadhaar_no))
#     mydb.commit()
#     check = checking_details(name, voter_id)
#     checking = check.isexists_user()
#     if checking:
#         print('\n')
#         print("your exists user, you can't vote again....")

#     else:
#         print('hi')

import mysql.connector
mydb = mysql.connector.connect(
    host='localhost', user='root', passwd='Yamaha@Rx100', database='online_voting_poll')
mycursor = mydb.cursor()


class checking_details:
    def __init__(self, name, voter_id):
        self.name = name
        self.voter_id = voter_id

    def isexists_user(self):
        mycursor.execute(
            'select user_id,name,voter_id from user_details where voter_id like %s', (self.voter_id,))
        details = mycursor.fetchall()
        for i in details:
            if i[2] == self.voter_id:
                return True
            else:
                return False


class party_details:
    def __init__(self):
        self.total_count = 0
        self.admk = 0
        self.dmk = 0
        self.pmk = 0

    def count_votes(self):
        mycursor.execute('select * from party_details ')
        ind = mycursor.fetchall()
        for i in ind:
            print('*', i[1], ' ', i[3])
        vote_here = input('enter your vote [party_name or symbol]: ')
        self.total_count = self.total_count+1
        if vote_here == 'ADMK' or vote_here == 'leaf':
            self.admk = self.admk+1
        elif vote_here == 'DMK' or vote_here == 'sun':
            self.dmk = self.dmk+1
        else:
            self.pmk = self.pmk+1

    def count(self):
        print('total_count:', self.total_count)
        print('admk: ', self.admk)
        print('dmk: ', self.dmk)
        print('pmk: ', self.pmk)


class modify_req:
    def location_req(self):
        lst = ['approved', 'decline']
        decision = input('electoral officer decision: ')
        if decision == lst[0]:
            print('your location has been modified, now you can vote...')
        else:
            print("sorry you can't vote, your details are not correct....")


if __name__ == '__main__':
    election = party_details()

    for i in range(2):
        Workflow = int(input("For voting press '1': "))
        if(Workflow == 1):
            name = input('enter your name: ')
            voter_id = int(input('enter your voter_id: '))
            address = input('enter your street name: ')
            aadhaar_no = int(input('enter your aadhaar no: '))
            check = checking_details(name, voter_id)
            checking = check.isexists_user()

            if checking:
                print('you are already voted....')

            else:
                mycursor.execute(
                    'INSERT into USER_DETAILS(name,voter_id,address,aadhaar_no) VALUES(%s,%s,%s,%s)', (name, voter_id, address, aadhaar_no,))
                mydb.commit()
                request = input(
                    'if u have any location modification, type[yes or no]: ')

                if(request == 'no'):

                    election.count_votes()

                else:
                    new_address = input('enter your new location name: ')
                    req = modify_req()
                    reqt = req.location_req()

    election.count()
