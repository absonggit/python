import redis

# r = redis.Redis(host='2.2.2.200', port=6379 , password='123456')
# r.set('name', 'harry')
# print(r.get('name'))
# r.close()
r1 = redis.StrictRedis(host='2.2.2.200', port=6379, password='123456')

print(r1.get('name'))
pipe = r1.pipeline()
pipe.set("a","1")
pipe.set("b","2")
pipe.set("c","3")
pipe.execute()
print(r1.keys())
print(r1.get("a"))
print(r1.get("b"))
print(r1.get("c"))
r1.close()