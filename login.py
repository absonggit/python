password = "123"
user_list = []
name = input("username:")
count = 0
file = 'deny_user_list.txt'

with open(file, "r+", encoding="utf-8") as of:
    for line in of:
        user_list.append(line.strip())

    for word in user_list:
        if name == word:
            print(name, "User locked!")
            break
    else:
        while count <= 2:
            if password == input("password:"):
                print(name, "welcome!")
                break
            else:
                if count < 2:
                    print(name, "The password is wrong! retry")
                    count += 1
                else:
                    print(name, "Wrong is too many,user is locked!")
                    of.write(name + '\n')
                    break
