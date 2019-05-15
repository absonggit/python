password = "123"
name = input("username:")
count = 0
file = 'deny_user_list.txt'

with open(file, "r+", encoding="utf-8") as of:
    def fib():              # 生成器
        for line in of:
            yield line.strip()
        return 'done'
    # for word in (line.strip() for line in of):  # 生成器
    for word in fib():
        if name == word:
            print(name, "User locked!")
            break
    else:
        while count <= 2:
            if password == input("password:"):
                print(name, "Welcome!")
                break
            else:
                if count < 2:
                    print(name, "The password is wrong! retry")
                    count += 1
                else:
                    print(name, "Wrong is too many,user is locked!")
                    of.write(name + '\n')
                    break
