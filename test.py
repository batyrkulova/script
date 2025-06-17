list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)


movies = {
    "cinema": "Grand Cinema",
    "location": {
        "city": "New York",
        "state": "NY"
    },
    "films": [
        {
            "title": "Inception",
            "director": "Christopher Nolan",
            "rating": 8.8,
            "genres": ["Sci-Fi", "Thriller"],
            "box_office_millions": 829.9,
            "showtimes": ["18:00", "21:00", "00:30"]
        },
        {
            "title": "The Godfather",
            "director": "Francis Ford Coppola",
            "rating": 9.2,
            "genres": ["Crime", "Drama"],
            "box_office_millions": 246.1,
            "showtimes": ["17:00", "20:30"]
        },
        {
            "title": "Jumanji",
            "director": "Joe Johnston",
            "rating": 6.9,
            "genres": ["Adventure", "Comedy"],
            "box_office_millions": 262.8,
            "showtimes": ["15:30", "19:00", "22:30"]
        }
    ]
}

# Your tasks:
# High Ratings & Earnings
# Print the title and director of all movies with a rating above 7.5 and box office earnings above 250 million.

# for values in movies["films"]:
#     if values["rating"] >= 7.5 and values["box_office_millions"] >= 250:
#         print(values["director"])

light = []

for values in movies["films"]:
    if values[["rating"][0]] > values[["rating"][2]]:
        print(values["name"])




