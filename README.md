# swapi_people
This is a lookup tool that queries the free online Star Wars API. It returns the Name, Birth Year, and Species of the character name passed as with the --name argument at the command line.

# Requirements
(built in) os\
argparse==1.1.0\
requests==2.21.0\

# Usage
swapi_people.py --name character name

# Example
swapi_people.py --name luke skywalker

  # Sample Output
  Name: Luke Skywalker\
  Birth Year: 19BBY\
  Species: Human\

# Alternate Usage
passing the word list as the name returns a list of character names available from the API.

swapi_people.py --name list

  # Sample Output
  Luke Skywalker\
  C-3PO\
  R2-D2\
  Darth Vader\
  Leia Organa\
  Owen Lars\
  Beru Whitesun lars\
  R5-D4\
  Biggs Darklighter\
  Obi-Wan Kenobi\
