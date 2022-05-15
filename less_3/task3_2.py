name = input('Enter your name: ')
s_name = input('Enter your second name: ')
date = input('Enter your date of birth: ')
place = input('Where do you live? ')
email = input('Enter your e-mail: ')
tel = input('Enter your number of phone: ')


def passport(arg_2, arg_1, arg_3, arg_4, arg_5, arg_6):
    print(
        f"S_name - {arg_2}; Name - {arg_1}; Date - {arg_3}; Place - {arg_4}; Email - {arg_5}; Tel - {arg_6}"
    )


passport(arg_1=name,
         arg_2=s_name,
         arg_3=date,
         arg_4=place,
         arg_5=email,
         arg_6=tel)