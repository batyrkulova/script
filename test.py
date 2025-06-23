# list1 = [1, 3]
# list2 = list1
# list1[0] = 4
# print(list2)


# movies = {
#     "cinema": "Grand Cinema",
#     "location": {
#         "city": "New York",
#         "state": "NY"
#     },
#     "films": [
#         {
#             "title": "Inception",
#             "director": "Christopher Nolan",
#             "rating": 8.8,
#             "genres": ["Sci-Fi", "Thriller"],
#             "box_office_millions": 829.9,
#             "showtimes": ["18:00", "21:00", "00:30"]
#         },
#         {
#             "title": "The Godfather",
#             "director": "Francis Ford Coppola",
#             "rating": 9.2,
#             "genres": ["Crime", "Drama"],
#             "box_office_millions": 246.1,
#             "showtimes": ["17:00", "20:30"]
#         },
#         {
#             "title": "Jumanji",
#             "director": "Joe Johnston",
#             "rating": 6.9,
#             "genres": ["Adventure", "Comedy"],
#             "box_office_millions": 262.8,
#             "showtimes": ["15:30", "19:00", "22:30"]
#         }
#     ]
# }

# # Your tasks:
# # High Ratings & Earnings
# # Print the title and director of all movies with a rating above 7.5 and box office earnings above 250 million.

# # for values in movies["films"]:
# #     if values["rating"] >= 7.5 and values["box_office_millions"] >= 250:
# #         print(values["director"])

# light = []

# for values in movies["films"]:
#     if values[["rating"][0]] > values[["rating"][2]]:
#         print(values["name"])

# def function(parameter):
#     if parameter == False:
#         return True


# print(function(False), function(True))

# def function(parameter = False):
#     return parameter


# print(function(True), function())


# def function(parameter):
#     parameter[0] = 2


# the_list = [1]
# function(the_list)
# print(the_list)

# angle = -1
# for i in range(-1, 1):
#     if 2 * i < 4:
#         angle += 1
#     else:
#         angle += 2
# print(angle)

# answers = (False, True, True )
# sel = answers[:]
# points = 0
# for answers in sel[1:]:
#     if answers:
#         points +=1
# print(points)

# train = {"Hello": 1, "HI": 2, "OLa": 2}

# for i in train.items():
#     print(i[0], end="s")

# the_data = [True, 3.1415, -2 ]
# the data.index(the_data[-1]) == 0
# print(the data.index)

# one = [1,2]
# two = one[:]
# two.append(3)
# print(one[-1] + two [-1])

# def process(data):
#     data = 2 
#     return data
# mes = [ 0 in range (3)]
# result = process(mes)
# print(result[-2])

def walk(top):
    if top == 0:
        return 0
    else: 
        return top * walk(top - 1)

print(walk(2))