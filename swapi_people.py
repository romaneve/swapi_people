#!/usr/bin/python3
"""
 /(_)\ Honeyman
 \* */ Last Update: 12-12-2018
  \_/  day of year: 346
Star Wars People Query:
    pass a character name to return their
    birth year and species.
"""

import os, requests, argparse

def clr():
    # clear the screen before displaying output
    # for a easier reading.
    os.system('clear')


def prep_name(raw_name):
    # take the name input from argparse which is a list
    # and combine and trim the elements to return a usable
    # name.
    name = ''
    for n in raw_name:
        name += n
        name += ' '
    return name.rstrip()

def list_characters(url):
    # pull and return all names from the dataset. returns
    # a dictionary containing the return code and a list
    # of characters.
    l_out = []
    try:
        j = requests.get(url).json()['results']
    except:
        out = {'code': 3, 'message': f"{url}\nis unavailable"}
        return out

    for i in j:
        l_out.append(i['name'])
    out = {'code': 1, 'names': l_out}
    return out


def get_character(name, url):
    # compare the name against the returned dataset to return
    # a dictionary containing the return code, name, birth_year
    # and species
    try:
        j = requests.get(url).json()['results']
    except:
        out = {'code': 3, 'message': f"{url}\nis unavailable"}
        return out

    for i in j:
        if i['name'].lower() == name.lower():
            s_url = i['species'][0]
            s_out = requests.get(s_url).json()['name']
            out = {'code': 0,
                    'name': i['name'],
                    'birth_year': i['birth_year'],
                    'species': s_out}
            return out
    out = {'code': 2, 'message': f"{name} is not in the database."}
    return out


if __name__ == "__main__":
    # gathering the command line arguments
    # name is passed from the command line
    # as --name character name. if --name is not
    # passed it returns sample data using Luke
    # Skywalker.
    url = f"https://swapi.co/api/people/?format=json"
    CLI = argparse.ArgumentParser()
    CLI.add_argument(
            "--name",
            nargs = "*",
            type = str,
            default = ['Luke', 'Skywalker'],
            )

    # take the raw name, which is a list
    # and pass it to prep_name to format
    # it for use in get_character.
    raw_name = CLI.parse_args().name
    name = prep_name(raw_name)
    if name == "list":
        response = list_characters(url)
    else:
        response = get_character(name, url)
    clr()
    
    # print out the results to the command line
    # the set includes a return code used below
    # to direct the output.
    # code values:
    #   code 0 = get_name success
    #   code 1 = list_characters success
    #   code 2 = name is not in the database
    #   code 3 = api url is unavailable
    if response['code'] == 0:
        print(f"Name: {response['name']}\n"
                f"Birth Year: {response['birth_year']}\n"
                f"Species: {response['species']}\n")
    elif response['code'] == 1:
        for n in response['names']:
            print(f"{n}")
    elif response['code'] == 2:
        print(f"{response['message']}\n")
    elif response['code'] == 3:
        print(f"{response['message']}\n")
