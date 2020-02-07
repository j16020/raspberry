from Mambo import Mambo

# 先程メモしたドローンのBLEアドレスに書き換えください
mamboAddr = "d0:3a:f2:02:e6:36"

# ドローンのオブジェクト作成
# ドローンのアームはBLE接続しないと操作できないためWi-FiはOFFにしてBLE接続する
mambo = Mambo(mamboAddr, use_wifi=False)

# ドローンと接続開始
print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)


import beep
# 離陸
print("taking off!")
mambo.safe_takeoff(8)

# 前進
#print("Flying direct: going forward")
#mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=1)
#mambo.smart_sleep(5.2)


#        print("flip front")
#        print("flying state is %s" % mambo.sensors.flying_state)
#        success = mambo.flip(direction="front")
#        print("mambo flip result %s" % success)
#        mambo.smart_sleep(5)

#        print("flip back")
#        print("flying state is %s" % mambo.sensors.flying_state)
#        success = mambo.flip(direction="back")
#        print("mambo flip result %s" % success)
#        mambo.smart_sleep(5)

# 着陸
print("landing")
mambo.safe_land(5)
mambo.smart_sleep(5)

# ドローンと接続解除
print("disconnect")
mambo.disconnect()
