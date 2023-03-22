balance = 0

acc_nums = {"cha233" : 0, "bha215" : 0, "bha216" : 0}

printf("HELLO")
def printing_stuff():
    print("To create a new account --> 1")
    print("To deposit money --> 2")
    print("To withdraw money --> 3")
    print("To check balance --> 4")
    print("To exit --> 5")


def printing_less_stuff():
    print("To deposit money --> 2")
    print("To withdraw money --> 3")
    print("To check balance --> 4")
    print("To exit --> 5")


def new_acc_details():
    global key
    name = input("Enter account holder name : ")
    age = int(input("Enter your age : "))
    roll_no = input("Enter your roll number : ")
    acc_num = name[:3] + roll_no[-3:]
    print("Account No. :", acc_num)
    print(type(acc_nums["cha233"]))
    acc_nums[acc_num] = 0  #puts the value of the key (acc_num) as 0
    print(acc_nums)
    print(acc_nums["cha233"])


def deposit(amount):
    global key
    #acc_nums.update((key + amount) for key in acc_nums.items())
    print(type(amount))
    acc_nums[key] = acc_nums[key] + amount
    print("balance :", acc_nums[key])
    print(acc_nums)


def withdraw(amount):
    global balance
    if amount > acc_nums[key]:
        print(acc_nums)
        print("Insufficient funds! Current Balance :", acc_nums[key])
    else:
        acc_nums[key] = acc_nums[key] - amount
        print("balance :", acc_nums[key])


def check_bal():
    print("Balance :", balance)

#            ..............main................


running = True

while running:
    printing_stuff()

    n = int(input("Select any option : "))

#      .........creating a new acc............

    if n == 1:
        new_acc_details()

    #    ..................depositing money................

    elif n == 2:
        ch = input("Enter account number : ")

        for key in acc_nums.keys():
            if key == ch:
                amount = int(input("enter the amount to deposit : "))
                print("................THIS IS THE KEY..............", key)
                deposit(amount)

            elif key != ch:
                pass

    #      ..................withdrawing money................

    elif n == 3:
        ch = input("Enter account number : ")

        for key in acc_nums.keys():
            if key == ch:
                amount = int(input("enter the amount to withdraw : "))
                print("................THIS IS THE KEY..............", key)
                withdraw(amount)

            elif key != ch:
                pass


#         .................. checking balance..............

    elif n == 4:
        ch = input("Enter account number : ")
        for key in acc_nums.keys():
            if key == ch:
                check_bal()

    elif n == 5:
        break
