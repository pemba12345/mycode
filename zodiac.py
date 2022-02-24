#!/usr/bin/env python3

zodiac = 'Your chinese zodiac sign is '

#ask input for the year of birth
YOB = int(input("Enter the  year, you were born? Choose between 1969-2004: "))

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
                             
zodiac_dict = {"a_list": "Rooster", "b_list" : "dog", "c_list" : "pig", "d_list" : "rat", "e_list" : "ox", "f_list" : "tiger", "g_list" : "rabbit", "h_list" : "dragon", "i_list" : "snake", "j_list" : "horse", "k_list" : "goat", "l_list" : "monkey"}


for each_key in lists: 
    if YOB in lists[each_key]:
        print("Your chinese zodiac sign is", zodiac_dict[each_key],'.')

#If user enters year < 1969
if YOB <= 1968:
    print("There is no way that you are older than 54.")

#If user enters year > 2004
elif YOB >= 2005:
    print("There is no way that you are younger than 18.")

#try:
 #   print("the year should be entered in integers")



