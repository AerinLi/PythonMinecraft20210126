from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
x,y,z = Aerin.player.getTilePos()
Aerin.setSign(x,y,z+1,63,0,"我愛Minecraft","也愛Python")