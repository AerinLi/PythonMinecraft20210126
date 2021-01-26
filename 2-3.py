from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
import random,time
while True:
    x,y,z = Aerin.player.getTilePos()
    color = random.randrange(0,16)
    Aerin.setBlocks(x+10,y,z+10,x-10,y,z-10,95,color)
    time.sleep(3)
                            
