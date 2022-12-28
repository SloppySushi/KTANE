# Red Blue Noir/N**** A/B/C
R_list=["c","b","a","ac","b","ac","abc","ab","a"]
B_list=["b","ac","b","a","b","bc","c","ac","a"]
N_list=["abc","ac","b","ac","b","bc","ab","c","c"]

letters=[]

def what_cut(color_list,position,letter):
    if letter in color_list[position]:
        print("-- CUT "+letter+" --")
    else :
        print("-- DONT CUT --")

while True :
    inputLetter=input(f'COLOR and LETTER : ra/bb/nc\n>> ')
    color=inputLetter[0]
    letter=inputLetter[1]
    letters.append(color)
    current_position=letters.count(color)-1

    if color == "r" :
        what_cut(R_list,current_position,letter)
    elif color == "b" :
        what_cut(B_list,current_position,letter)
    elif color == "n" :
        what_cut(N_list,current_position,letter)
