import sys
if len(sys.argv) != 3:
    exit("Parameters of the lack of！At a minimum, enter the string that needs to be replaced and changed")
find_str = sys.argv[1]
replace_str = sys.argv[2]
with open("old.txt", "r", encoding="utf-8") as f1, open("new.txt", "w", encoding="utf-8") as f2:
    for line in f1:
        if find_str in line:
            line = line.replace(find_str, replace_str)
        f2.write(line)
