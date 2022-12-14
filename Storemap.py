class Storemap:
	def __init__(self):
		self.blockmap=[
                        [[4,4,4,4,4,4,4,4,4,4,4,4,4],
                        [4,0,0,0,1,1,1,2,1,0,0,0,4],
                        [4,0,4,1,4,1,4,0,4,1,4,0,4],
                        [4,0,1,2,0,0,2,0,1,1,1,0,4],
                        [4,1,4,0,4,2,4,2,4,1,4,1,4],
                        [4,0,2,0,2,3,3,3,2,0,1,0,4],
                        [4,1,4,2,4,3,4,3,4,2,4,1,4],
                        [4,1,1,0,2,3,3,3,2,0,2,0,4],
                        [4,1,4,0,4,2,4,2,4,1,4,1,4],
                        [4,0,1,2,0,0,2,0,1,1,1,0,4],
                        [4,0,4,1,4,2,4,1,4,1,4,0,4],
                        [4,0,0,0,1,0,1,0,1,0,0,0,4],
                        [4,4,4,4,4,4,4,4,4,4,4,4,4]],

                        [[4,4,4,4,4,4,4,4,4,4,4,4,4],
                        [4,0,0,0,1,0,4,0,1,0,0,0,4],
                        [4,0,0,4,0,1,0,1,0,4,0,0,4],
                        [4,0,4,0,1,4,1,4,0,1,4,0,4],
                        [4,1,0,1,1,3,2,3,1,0,1,1,4],
                        [4,0,1,1,4,2,4,2,4,1,1,0,4],
                        [4,0,4,3,2,3,3,3,2,3,4,0,4],
                        [4,1,0,1,4,2,4,2,4,1,0,1,4],
                        [4,1,1,0,1,3,2,3,1,1,1,1,4],
                        [4,0,4,1,0,4,1,4,1,0,4,0,4],
                        [4,0,0,4,1,1,0,1,0,4,0,0,4],
                        [4,0,0,0,1,0,4,0,1,0,0,0,4],
                        [4,4,4,4,4,4,4,4,4,4,4,4,4]]
                    ]
	def choosemap(self,number):
		return self.blockmap[number]

	def readmap(self,height,width):
		f = open('yourmap.txt',mode='r')
		lines = f.readlines()
		print(lines)
		if (len(lines)!=height-2 or len(lines[0].split())!=width-2):
			print("Invalid map Input")
			map=[[0 for j in range(width)] for i in range(height)]
			for i in range(height):
				map[i][0]=4
				map[i][width-1]=4
			for i in range(width):
				map[0][i]=4
				map[height-1][i]=4
			return map
		map=[[0 for j in range(width)] for i in range(height)]
		for i in range(height):
			map[i][0]=4
			map[i][width-1]=4
		for i in range(width):
			map[0][i]=4
			map[height-1][i]=4
		for i in range(height-2):
			for j in range(width-2):
				map[i+1][j+1]=int(lines[i].split()[j])
		f.close()
		return map