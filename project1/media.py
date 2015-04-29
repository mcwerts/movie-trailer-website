#
# Michael Werts, mcwerts@gmail.com
#
# CHANGES
#   Defined TypedTrailer subclass of Movie with additional 'type' field.
#
import webbrowser

class Movie():
    """ This class provides a way to store movie related information."""
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TypedTrailer(Movie):
	""" This class identifies whether it's trailer is Theatrical or Honest."""

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, type_string):
		Movie.__init__(self, movie_title, movie_storyline, poster_image, trailer_youtube)
		self.type = type_string # Trailer type: "Theatrical" or "Honest"
