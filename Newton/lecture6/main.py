def collection():
    arr = []
    num = 40
    while num != 0:
        amount = input("Put something in the collection bowl: ")
        arr.append(amount)
        print(amount)
        num = - 1
        print(arr)
collection()

#files
open('./text,txt')
open('../lecture/text.txt')
file = open('./text.txt')
print(file.read())
file.close()
        