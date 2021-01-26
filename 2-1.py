from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
x,y,z = Aerin.player.getTilePos()
Aerin.setBlock(x,y,z+1,7)
Aerin.setBlock(x,y,z-1,7)
Aerin.setBlock(x-1,y,z,7)
Aerin.setBlock(x+1,y,z,7)
Aerin.setBlock(x+1,y,z+1,7)
Aerin.setBlock(x-1,y,z+1,7)
Aerin.setBlock(x+1,y,z-1,7)
Aerin.setBlock(x-1,y,z-1,7)

              
