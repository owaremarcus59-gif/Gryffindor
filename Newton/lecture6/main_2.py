# sad = open("./mock.csv")

# for line in sad.readlines():
#     print(line)

# sad.close()    


#Example 2
# sad = open("./mock.csv")

# print(sad.readlines()[:10])
# for line in sad.readlines():
#     pass

# Another example
# sad = open("./mock.csv")

# content = sad.readline()
# for line in content:
#     print(line)

#print(content[:1])

from PIL import Image, ImageChops
img1 = Image.open('./kk.png')
img2 = Image.open('./NF.png')

diff = ImageChops.difference(img1,img2)
diff.show()
