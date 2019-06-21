import os.path
import xml.etree.ElementTree as ET


class ChangeData(object):
    def __init__(self, path, value, xml_tag):
        self.path = path
        self.value = value
        self.xml_tag = xml_tag


def find_file(s, *end_string):
    array = map(s.endswith, end_string)
    if True in array:
        return True
    else:
        return False


if __name__ == '__main__':
    data = ChangeData
    data.xml_tag = "numToKeep"
    data.path = "./"
    data.value = "30"
    s = os.listdir(data.path)
    f_file = []
    for i in s:
        if find_file(i, '.xml'):
            f_file.append(os.path.join(data.path, i))
    for file in f_file:
        tree = ET.parse(file)
        root = tree.getroot()

        for i in root.iter(data.xml_tag):
            old_text = i.text
            i.text = data.value
            print(
                f"将文件\033[31m{file}\033[0m\n\t\033[32m{i.tag}\033[0m标签的值\033[33m{old_text}\033[0m修改为\033[34m{i.text}\033[0m")
        tree.write(file, encoding='UTF-8')

