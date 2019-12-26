# Write the code which will write excepted data to files below
# For example given offices of Google:
# 1) google_kazakstan.txt
# 2) google_paris.txt
# 3)google_uar.txt
# 4)google_kyrgyzstan.txt
# 5)google_san_francisco.txt
# 6)google_germany.txt
# 7)google_moscow.txt
# 8)google_sweden.txt
# When the user will say “Hello”
# Your code must communicate and give a choice from listed offices. After it
# has to receive a complain from user, and write it to file chosen by user.
# Hint: Use construction “with open”

offices = [
    "kazakstan", "paris", "uar", "kyrgyzstan",
    "san_francisco", "germany", "moscow", "sweden"
    ]
o = offices                                 # to make it short
# print("Available Google offices: \n", o)

if str(
    input('\nHello user! \nInput "Hello" to continue: \n')).lower(
    ) == "hello":
    a = input(
        f"Choose Google office: \n{o[0]}, {o[1]}, {o[2]}, {o[3]}, {o[4]}, {o[5]}, {o[6]}, {o[7]}\n")
    
    if a == o[0]:
        with open(f'google_{o[0]}.txt', 'w') as filename:
            filename.write(input(f"Message for Google {o[0]} office:\n"))
        print(f"Google {o[0]} will receive your message")
    
    elif a == o[1]:
        with open(f'google_{o[1]}.txt', 'w') as filename:
            filename.write(input(f"Message for Google {o[1]} office:\n"))
        print(f"Google {o[1]} will receive your message")

    elif a == o[2]:
        with open(f'google_{o[2]}.txt', 'w') as filename:
            filename.write(input(f"Message for Google {o[2]} office:\n"))
        print(f"Google {o[2]} will receive your message")

    elif a == o[3]:
        with open(f'google_{o[3]}.txt', 'w') as filename:
            filename.write(input(f"Message for Google {o[3]} office:\n"))
        print(f"Google {o[3]} will receive your message")

    elif a == o[4]:
        with open(f'google_{o[4]}.txt', 'w') as filename:
            filename.write(input(f"Message for Google {o[4]} office:\n"))
        print(f"Google {o[4]} will receive your message")

    elif a == o[5]:
        with open(f'google_{o[5]}.txt', 'w') as filename:
            filename.write(input(f"Message for Google {o[5]} office:\n"))
        print(f"Google {o[5]} will receive your message")

    elif a == o[6]:
        with open(f'google_{o[6]}.txt', 'w') as filename:
            filename.write(input(f"Message for Google {o[6]} office:\n"))
        print(f"Google {o[6]} will receive your message")

    elif a == o[7]:
        with open(f'google_{o[7]}.txt', 'w') as filename:
            filename.write(input(f"Message for Google {o[7]} office:\n"))
        print(f"Google {o[7]} will receive your message")

    else:
        print("Try again")
else:
    print("Error")
