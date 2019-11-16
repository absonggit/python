# import win32com.client
# import time
# #装饰器
# def alerter(func):
#     def inner(*args,**kwargs):
#         print("\033[34mINFO:  开始执行%s函数\033[0m" % (func.__name__))
#         time.perf_counter()
#         try:
#             func(*args, **kwargs)
#         except BaseException as e:
#             print("\033[31mERROR: 执行%s函数 %s\033[0m" % (func.__name__, e))
#             print()
#         else:
#             print("\033[34mINFO:  执行%s函数 耗时 %s\033[0m" % (func.__name__, time.perf_counter()))
#             print()
#     return inner

# @alerter
# def exactDiv(*args):
#     print(args[0] // args[1])

# @alerter
# def readFile(path):
#     with open(path, "r", encoding="utf-8") as f:
#          print(f.read())

# @alerter
# def voice(content):
#     speaker = win32com.client.Dispatch("SAPI.SpVoice")
#     speaker.Speak(content)

# exactDiv(12,0)
# readFile("file.txt")
# voice("黑化肥挥发会发黑")

# class Person(object):
#     def __init__(self, gun):
#         self.gun = gun

#     def fire(self):
#         self.gun.shoot()
        
#     def fillBullet(self, count):
#         self.gun.bulletBox.addBullet(count)

# class Gun(object):
#     def __init__(self, bulletBox):
#         self.bulletBox = bulletBox
    
#     def shoot(self):
#         if self.bulletBox.getBullet() == 0:
#             print("没有子弹了")
#         else:
#             self.bulletBox.delBullet(1)
#             print("射击！ 剩余%d颗子弹。" % (self.bulletBox.getBullet()))

# class bulletBox(object):
#     def __init__(self, count):
#         self.count = count

#     def addBullet(self, count):
#         self.count += count

#     def delBullet(self, count):
#         self.count -= count

#     def getBullet(self):
#         return self.count

# b = bulletBox(3)
# g = Gun(b)
# p = Person(g)
# p.fire()
# p.fillBullet(3)
# p.fire()

# import smtplib
# from email.mime.text import MIMEText

# SMTPServer = "smtp.163.com"
# sender = "xxx@163.com"
# password = "m1234567890"
# message = "hellow world"
# msg = MIMEText(message)
# msg["Subject"] = "这是一封测试邮件"
# msg["From"]= sender

# mailServer = smtplib.SMTP(SMTPServer, 25)
# mailServer.login(sender, password)
# mailServer.sendmail(sender, ["xxx@qq.com"], msg.as_string())
# mailServer.quit()

# import tkinter
# #创建主窗口
# win = tkinter.Tk()

# #设置标题
# win.title("test")

# #设置窗口大小和位置
# win.geometry("600x500+600+200")

# lable = tkinter.Label(win, text="Lable 文本内容", bg="green", fg="black", font=("黑体"), width=100)
# lable.pack()

# def test():
#     #显示文本
#     lable = tkinter.Label(win, text=(username_entry.get(), password_entry.get()), bg="green", fg="black", font=("黑体"), width=100)
#     lable.pack()

# #输入
# username_entry = tkinter.Entry(win)
# username_entry.pack()
# password_entry = tkinter.Entry(win, show="*")
# password_entry.pack()

# #按钮
# button = tkinter.Button(win, text="按钮", command=test)
# button.pack()
# quit_button = tkinter.Button(win, text="退出", command=win.quit)
# quit_button.pack()

# win.mainloop()
