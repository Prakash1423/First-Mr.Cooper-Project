import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user='root', passwd='Yamaha@Rx100', database="rental_portal")
mycursor = mydb.cursor()


class checking_details:
    def __init__(self, phone_no, user_name):
        self.phone_no = phone_no
        self.user_name = user_name

    def isexits_user(self):
        mycursor.execute(
            'select user_id,user_name,phone_no from user_details where phone_no like %s', (self.phone_no,))
        details = mycursor.fetchall()
        for i in details:
            if i[2] == self.phone_no and i[1] == self.user_name:
                return i[0]


class lands:
    def lands_for_rent(self):
        mycursor.execute('select * from land_details')
        lnd = mycursor.fetchall()
        for i in lnd:
            print('* ', 'location: ', i[1], " ", 'city: ', i[2], " ", 'square feet: ',
                  i[3], " ", 'BHK: ', i[4], " ", 'rent cost: ', i[5], " ", 'status: ', i[6])


class owner:
    def land_owner(self, sendrequest):
        if sendrequest == 'yes':
            lst = ['approved', 'decline', 'pending']
            for i in lst:
                print('status: ', i)

    def approve_request(self, add_req):
        if add_req == 'yes':
            lst = ['approved', 'decline', 'pending']
            for i in lst:
                print('status: ', i)


if __name__ == '__main__':
    user_name = input('enter your name: ')
    phone_no = int(input('enter the phone_no: '))
    check = checking_details(phone_no, user_name)
    checking = check.isexits_user()

    if checking:
        print('\n')
        print('exits user')
        type = input('enter if you want to buy or sell: ')
        # show the land details
        if type == 'buy':
            z = lands()
            zz = z.nds_for_rent()
            selectthecity = input('select what city you want:  ')
            mycursor.execute(
                'select location,city,square_feet,type_bhk,rent_cost,rental_status from land_details where city like %s', (selectthecity,))
            searchcity = mycursor.fetchall()
            for i in searchcity:
                if i[-1] == 'tolet':
                    print(i)
            print('\n')
            sendrequest = input('send the request to land owner [yes or no]: ')
            ownr = owner()
            ownrs = ownr.land_owner(sendrequest)
            ownerfinaldecision = input('enter your suggestion for request: ')
            if ownerfinaldecision == 'approved':
                print('your request has been approved')
                print('thank you for select this rent portal')
            elif ownerfinaldecision == 'decline':
                print('sorry your request has been decline from owner')
                print('choose another land for rental')
            else:
                print('still your request in pending status')
                print('wait a moment')
        else:
            add_req = input(
                'if you want to send request to approver[yes or no] :')
            ads = owner()
            finish = ads.approve_request(add_req)
            approverfinaldecision = input(
                'enter your suggestion for request: ')
            if approverfinaldecision == 'approved':
                print('your request has been approved')
                print('now you can add your post on portal')
            elif approverfinaldecision == 'decline':
                print('sorry your request has been decline from approver')

            else:
                print('still your request in pending status')
                print('wait a moment')
    else:
        email = input('enter your mail-id: ')
        aadhaar_no = int(input('enter your aadhaar no: '))
        buy_or_sell = input('enter if your buy or sell: ')
        mycursor.execute('insert into user_details(user_name,phone_no,email,aadhaar_no,buy_or_sell) values(%s,%s,%s,%s,%s)',
                         (user_name, phone_no, email, aadhaar_no, buy_or_sell))
        mydb.commit()
