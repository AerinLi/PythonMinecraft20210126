from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
userName = input("請輸入姓名:")
message = input("請輸入發言:")
Aerin.postToChat("<"+userName + ">" +message)