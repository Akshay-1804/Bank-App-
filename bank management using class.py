print('Welcome to the Bank')
print('--*----------------------*--')
account=123456789
password=1234
balance=1000
class bank:
    def accountopen(self):
        n=(input('Enter your name: '))
        m=int(input('Enter your mobile number: '))
        a=int(input('Enter your aadhar card number: '))
        print('Confirm your details:')
        print('Name',n); print('mobile number:',m);print('Aadhar number',a)
        print('Select account type:\n 1)Current \n 2)Saving')
        at=int(input('Enter your choice: '))
        if at==account:
            print('Your Current account Created successfully')
            print('your account number is:',account)
            print('Your password is:',password)
        elif at==account:
            print('Your Saving account Created successfully')
            print('your account number is:', account)
            print('Your password is:', password)
        else:
            print('Invalid Choice') 
    def withdraw(self):
        acc=int(input('Enter Account number: '))
        if acc==account:
            np=int(input('Enter your password: '))
            if np==password:
                global balance
                w=int(input('Enter amount to withwraw: '))
                if w<=balance:
                    balance=balance-w
                    print('your account balance is :',balance)
                if w<=balance:
                    balance=balance-w
                    print('your account balance is :',balance)
                else:
                    print('insufficient balance')
            else:
                print('Password is incorrect')
        else:
            print('Account number is incorrect')
    def deposit(self):
        acd=int(input('Enter your account number: '))
        if acd==account:
            nps=int(input('Enter your password: '))
            if nps==password:
                da=int(input('Enter amount to deposit: '))
                global balance
                balance= balance+da
                print('Your account balance is balance: ',balance)
            else:
                print('incorrect password')
        else:
            print('Account number is incorrect')
    def check_balance(self):
        cac=int(input('Enter your account number: '))
        print('Your account balance is ',balance) if cac==account else print('incorrect account number')
print('Select operations')
b=bank()
while True:
    print('select operation to perform')
    print('press 1 to Open Account')
    print('press 2 to check balance')
    print('press 3 to withraw cash')
    print('press 4 to Deposit cash')
    print('Press 5 to exit')
    choice= int(input('Enter your choice: '))
    if choice==1:
        b.accountopen()
    elif choice==2:
        b.check_balance()
    elif choice==3:
        b.withdraw()
    elif choice==4:
        b.deposit()
    elif choice==5:
        break
    else:
        print('Invalid option pressed please check')



