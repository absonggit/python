import time
import telepot
import string
from telepot.loop import MessageLoop


menu = [
    {'id': '0', 'name': '特色皮蛋卷', 'price': '240'},
    {'id': '1', 'name': '西红柿炒蛋', 'price': '180'},
    {'id': '2', 'name': '青椒炒蛋', 'price': '180'},
    {'id': '3', 'name': '丝瓜炒蛋', 'price': '180'},
    {'id': '4', 'name': '咸蛋黄茄子', 'price': '180'},
    {'id': '5', 'name': '外婆菜炒蛋', 'price': '200'},
    {'id': '6', 'name': '千叶豆腐', 'price': '180'},
    {'id': '7', 'name': '香干炒肉', 'price': '180'},
    {'id': '8', 'name': '麻婆豆腐', 'price': '180'},
    {'id': '9', 'name': '腐竹炒肉', 'price': '180'},
    {'id': '10', 'name': '油豆腐炒肉', 'price': '180'},
    {'id': '11', 'name': '豆皮炒肉', 'price': '180'},
]

order = []

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if "menu" in msg['text']:
        m = ":: 菜单 ::\n"
        for i in menu:
            m += i['id'] + " " + i['name'] + " " + i['price'] + "P" + "\n"
        m += "点餐：\n\t/order@jjkkss_bot + 编号"
        bot.sendMessage(chat_id, m)
    
    if "order" in msg['text']:
        print(msg)
        order.append({'name' : msg['from']['first_name'], 'order': menu[int(msg['text'].split(" ")[1])]['name'], 'price': menu[int(msg['text'].split(" ")[1])]['price']})
        total = 0
        m = ":: 订单 ::\n"
        for i in order:
            m += i['name'] + " " + i['order'] + " " + i['price'] + "P" + "\n"
            total += int(i['price'])
        m += "总计: " + str(total) + "P"
        bot.sendMessage(chat_id, m)
    if "cancel" in msg['text']:
        for i in order:
           if i['name'] == msg['from']['first_name']:
                order.pop(order.index(i))
        m = ":: 订单 ::\n"
        total = 0
        for i in order:
            m += i['name'] + " " + i['order'] + " " + i['price'] + "P" + "\n"
            total += int(i['price'])
        m += "总计: " + str(total) + "P"
        bot.sendMessage(chat_id, m)
        
                

TOKEN = 'your tg token'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)