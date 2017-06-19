import media
import fresh_tomatoes

# Declare all movie instances first
x_men = media.Movie("X-Men: Days of Future Past",
                    "https://upload.wikimedia.org/wikipedia/en/0/0c/X-Men_Days_of_Future_Past_poster.jpg",
                    "https://www.youtube.com/watch?v=pK2zYHWDZKo")

spiderman = media.Movie("Spider-Man: Homecoming",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_UY1200_CR80,0,630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=39udgGPyYMg")

deadpool = media.Movie("Deadpool",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_UY268_CR1,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=9vN6DHB6bJc")

capt_america = media.Movie("Captain America: Civil War",
                           "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                           "https://www.youtube.com/watch?v=uVdV-lxRPFo")

avengers = media.Movie("Avengers: Age of Ultron",
                       "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                       "https://www.youtube.com/watch?v=JAUoeqvedMo")

logan = media.Movie("Logan",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=RH3OxVFvTeg")

# put them together into a list called movies
movies = [x_men, spiderman, deadpool, capt_america, avengers, logan]

# call fresh tomatoes function to generate html file of movie trailer webiste
fresh_tomatoes.open_movies_page(movies)
