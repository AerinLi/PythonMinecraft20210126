from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
x,y,z = Aerin.player.getTilePos()
try:
    blockType = int(input('請問你右邊要放甚麼方塊:'))
    Aerin.setBlock(x+1,y,z,answer)
except:
    print('只能輸入數字!!!!!!')