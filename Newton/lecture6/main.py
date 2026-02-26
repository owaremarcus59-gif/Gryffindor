# def collection():
#     arr = []
#     num = 40
#     while num != 0:
#         amount = input("Put something in the collection bowl: ")
#         arr.append(amount)
#         print(amount)
#         num = - 1
#         print(arr)
# collection()

#files
# open('./text,txt')
# open('../lecture/text.txt')
# file = open('./text.txt')
# print("I Love you")
# file.close()
              
import pytube


url = "https://youtu.be/nfstvFhWQXQ?si=lf2uneXJ2xg8mc0R"
stream = pytube.YouTube(url)
stream.streams.get_highest_resolution().download()