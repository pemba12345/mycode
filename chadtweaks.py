#!/usr/bin/env python3

zodiac = 'Your asian zodiac sign is '

#ask input for the year of birth
YOB = int(input("what year were you born?"))

# instead of having these as a bunch of different lists, why not make this one object?

lists= {
        "a_list":[1969,1981,1993], #year of a Rooster
        "b_list":[1970,1982,1994], #year of a dog
        "c_list":[1971,1983,1995], #year of a pig
        "d_list":[1972,1984,1996], #year of a rat
        "e_list":[1973,1985,1997], #year of an ox
        "f_list":[1974,1986,1998], #year of a tiger
        "g_list":[1975,1987,1999], #year of a rabbit
        "h_list":[1976,1988,2000], #year of a dragon
        "i_list":[1977,1989,2001], #year of a snake
        "j_list":[1978,1990,2002], #year of a horse
        "k_list":[1979,1991,2003], #year of a goat
        "l_list":[1980,1992,2004]} #year of a monkey

#creating dictioary for Birth years and their respective signs

# this dictionary is perfect! once we find a match to the list, you can match it to the zodiac symbol
zodiac_dict = {"a_list" : "Rooster", "b_list" : "dog", "c_list" : "pig", "d_list" : "rat", "e-list" : "ox", "f_list" : "tiger", "g_list" : "rabbit", "h_list" : "dragon", "i_list" : "snake", "j_list" : "horse", "k_list" : "goat", "l_list" : "monkey"}

# had to put "quotes" around all those names because otherwise python thinks they are variables

#if input value is in a_list
#if YOB in a_list
#    zodiac = zodiac + 'Rooster '
#print(zodiac)

# so what we need to do is go across ALL those lists and see if a match can be found
# the best way to do that is to use a for loop so you don't have to write something out for every single list


# this for loop is going across all the keys in the lists dictionary
# so each_key is first = to "a_list", then "b_list", etc.
for each_key in lists:
    # as we return each key, we use it to slice the dictionary
    # example: check if 1984 in lists["a_list"]
    if YOB in lists[each_key]:
        # if the year the user typed in is present in that list of years,
        # then we do this final print function
        # where we go to your zodiac_dict dictionary and use the key returned by the loop
        # to slice the zodiac_dict for what zodiac sign that is
        # example: zodiac_dict["a_list"] returns "Rooster"
        print(zodiac_dict[each_key])













