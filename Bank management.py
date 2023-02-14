print('Welcome to the Bank')
print('--**--**--**--**--**--**--**--**--**--**--**--**--')
def accountopen():
    n=(input('Enter your name: '))
    m=int(input('Enter your mobile no: '))
    a=int(input('Enter your aadhar number: '))
    print('Confirm your Details:'); print('Name:',n);print('mobile number:',m);print('Aadhar number',a)
    print('select account type: \n 1)Current \n 2)Saving')
    n=input('Enter your choice: ')
    if n=='Current'or n=='current':
        print('Your Current account Created successfully')
        print('Your account number is 123456789')
        print('Your password is 1234')
    elif n=='Saving'or n=='saving':
        print('Your Saving account Created successfully')
        print('Your account number is 123456789')
        print('Your password is 1234')
    else:
        print('Invalid Choice')
password=1234
balance= 10000
account= 123456789
def withdraw():
    acc=int(input('Enter account number: '))
    if acc==account:
        np=int(input('Enter your password: '))
        if np==password:
            w=int(input('Enter amount to withraw: '))
            print(w,'amount is withdrawed from your account no',account)
            global balance
            balance= balance-w
            print('your account balance is: ',balance)
        else:
         print('Password incorrect')
    else:
        print('Account number is incorrect')
def deposit():
    acd=int(input('Enter account number: '))
    if acd==account:
        nps=int(input('Enter your password: '))
        if nps==password:
            da=int(input('Enter amount to be Deposit: '))
            global balance
            balance= balance+da
            print('Your account balance is: ',balance)
        else:
            print('Password is incorrect')
    else:
        print('Account number is incorrect:')
def check_balance():
    cac=int(input('Enter account number: '))
    print('Your account balance is :',balance) if cac==account else print('Incorrect account number')
print('Select operations')
while True:
    print('select operation to perform')
    print('press 1 to Open Account')
    print('press 2 to check balance')
    print('press 3 to withraw cash')
    print('press 4 to Deposit cash')
    print('Press 5 to exit')
    choice= int(input('Enter your choice: '))
    if choice==1:
        accountopen()
    elif choice==2:
        check_balance()
    elif choice==3:
        withdraw()
    elif choice==4:  
        deposit()
    elif choice==5:
        break
    else:
        print('Invalid option pressed please check')


        
