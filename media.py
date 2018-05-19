#to open the youtube trailers on the browser
import webbrowser

#python class to store my favourite movies inclluding their title, storyline, poster image and the youtube trailer
class Movie():
        def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)
