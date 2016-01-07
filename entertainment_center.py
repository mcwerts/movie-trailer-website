# 
# Michael Werts, mcwerts@gmail.com
#
# CHANGES
#   - Setup argument parsing.
#   - Read movie data from JSON file.
#   - Dynamically create TypedTrailer objects from the parsed JSON data,
#     in compliance with the 'type' parameter.
#
import media
import fresh_tomatoes
import argparse
import json

# Setup argument parsing.
#
# python entertainment_center.py [-h|--help][(-t|--type) ("honest"|"theatrical")]
#
# Defines two flags, 'show_theatrical' and 'show_honest', which ultimately
# control the generation of movies from the JSON data source. If a flag is 
# 'True' a 'TypedTrailer' object corresponding to the flag is created for
# each movie entry.
parser = argparse.ArgumentParser(
    description="Generate an HTML page disploying Theatrical and Honest trailers.")
parser.add_argument("-t", "--type", choices=['theatrical','honest','all'], default='all', 
    help="filter for only the designated trailer type")
args = parser.parse_args()
show_theatrical = False
show_honest = False
if "theatrical" == args.type:
    show_theatrical = True
elif "honest" == args.type:
    show_honest = True
else:
    show_theatrical = True
    show_honest = True

# Load and parse the data from the JSON file.
json_data = open('movies.json').read()
catalog = json.loads(json_data)

# For each movie in the catalog, create the desired objects.
movies = []
for movie in catalog:
    if show_theatrical:
        movies.append(media.TypedTrailer(
            movie['title'], movie['synopsis'], movie['poster'], movie['theatrical_trailer'], "Theatrical"))
    if show_honest:
        movies.append(media.TypedTrailer(
            movie['title'], movie['synopsis'], movie['poster'], movie['honest_trailer'], "Honest"))

# Create the page.
fresh_tomatoes.open_movies_page(movies)

