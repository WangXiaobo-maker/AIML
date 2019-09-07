# -*- coding: utf-8 -*-
import aiml
import os

os.chdir('./resource')
mybot = aiml.Kernel()
mybot.learn("startup.xml")
mybot.respond('load nao')

#处理响应
while True:
    message = raw_input("Enter your message >> ")
    if("exit" == message):
        exit()
    response = mybot.respond(message) # 机器人应答
    if(response):
        print response
    else:
        print "我没听清，可以再说一次吗？或者尝试换一种提问方式"