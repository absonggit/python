with open("old.txt", "r", encoding="utf-8") as f1, open("new.txt", "w", encoding="utf-8") as f2:
    for line in f1:
        if "最终成功上市" in line:
            line = line.replace("最终成功上市", "最终破产倒闭")
        f2.write(line)
