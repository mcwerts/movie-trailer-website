INTRO

In addition to being a fan of movies I also enjoy the Honest trailers on the 
YouTube Screen Junkies channel. This Python program generates a web page 
displaying a combination of theatrical and Honest trailers for movies. 

USAGE

From the project directory launch the program as follows. 

python entertainment_center.py [-h|--help] [(-t|--type) ("honest"|"theatrical"|"all")]

-h, --help  Display help.
-t, --type  Filter the display of movies. The choices are "honest", "theatrical",
            and "all". The default is "all".

To modify the selection of movies, edit the file "movies.json".

CHANGES

Modifications to the Python code were emphasized, rather than changes to the 
HTML/CSS. 

1. Defined a TypedTrailer class by inheriting from Movie and adding
   a 'type' field to hold a string indicating the type of trailer 
   ("Theatrical" or "Honest").
2. Moved the raw data to a JSON file and wrote code to read the JSON
   and dynamically create TypedTrailer objects from it. This code sets the 
   trailer type as appropriate when creating the TypedTrailer object. Well-
   formed data is expected.
3. Added argument handling to enable filtering of the trailers. All trailers 
   can be displayed or just theatrical or honest trailers.
4. The fresh_tomatoes.py code was modified to display the trailer type 
   below the movie title.

FILES

fresh_tomatoes.py
media.py
entertainment_center.py
movies.json

ISSUES

- Longer movie names can disrupt the regular column layout. This was a 
  preexising issue with the Fresh Tomatoes code.

AUTHOR

Michael Werts, mcwerts@gmail.com
