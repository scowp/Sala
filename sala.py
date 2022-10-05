#
# for i in range(1,5):
#     for j in range(1,11):
#         dic = {}
#         dic[i,j]=[[i+2,j+2],[i+3,j+3]]
#         print(dic)


# for i in range(1,5):
#     for j in range(1,11):
#         dic = {}
#         if i < 3 and j < 8:
#             dic[i,j]=[[i+3,j+3],[i+4,j+4]]
#             print(dic)
#         else:
#             dic[i,j]=[["NaN","NaN"],["NaN","NaN"]]
#             print(dic)


for i in range(1,5):
    for j in range(1,11):
        dic = {}
        if i < 2 and j < 7:
            dic[i,j]=[[i+3,j+3],[i+4,j+4]]
            print(dic)
        elif i < 3 and j < 8:
            dic[i,j]=[[i+3,j+3],["NaN","NaN"]]
            print(dic)
        else:
            dic[i, j] = [["NaN", "NaN"], ["NaN", "NaN"]]
            print(dic)