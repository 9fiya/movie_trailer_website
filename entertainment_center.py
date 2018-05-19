#to import the class that is created to make several instances of it
import media
#to use this file to display the movies in a HTML file
import fresh_tomatoes

smurfs = media.Movie("The Smurfs",
                    "The story of small, blue creatures that live happily in their mushroom houses",
                    "https://fontmeme.com/images/The-Smurfs-Poster.jpg",
                    "https://www.youtube.com/watch?v=yhBpgqXwrt8")


the_boss_baby = media.Movie("The Boss Baby",
                            "A story of a baby that wears a suit and carries a briefcase, while he is on a secret mission",
                            "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg",
                            "https://www.youtube.com/watch?v=tquIfapGVqs")




tangled = media.Movie("Tangled",
                      "A story of beautiful princess Rapunzel with long, golden, magical hair",
                      "https://s-media-cache-ak0.pinimg.com/originals/1e/c7/6d/1ec76dc4c59d319711b5dd393a454796.jpg",
                      "https://www.youtube.com/watch?v=ip_0CFKTO9E")

brave = media.Movie("Brave",
                    "Merida, the daughter of a King and a Queen, is determined change her destiny",
                    "http://t0.gstatic.com/images?q=tbn:ANd9GcSuKUcpKMfuY1En5kWsJB2Xe-dqu-yYrQM6KTps3-Mti04lgmSY",
                    "https://www.youtube.com/watch?v=TEHWDA_6e3M")

finding_nemo = media.Movie("Finding Nemo",
                           "A story about two clownfish",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Finding_Nemo.jpg/220px-Finding_Nemo.jpg",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")

up = media.Movie("Up",
                 "A story about an old man who want to fly his house with thousands of balloons",
                 "http://www.pixartalk.com/wp-content/uploads/2009/06/upbraziltheatrical.jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")


#the list of all movies
movies = [smurfs, the_boss_baby, tangled, brave, finding_nemo, up]
# input the previous list to build the HTML file,to display the website.
fresh_tomatoes.open_movies_page(movies)
