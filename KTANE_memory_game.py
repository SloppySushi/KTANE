# MEMORY GAME
# [position][label]
history=[
"  ",
"  ",
"  ",
"  ",
]

def print_position(position) :
    return(".------------.\n|position : "+str(position)+"|\n.------------.")

def print_label(label) :
    return(".---------.\n|label : "+str(label)+"|\n.---------.")

def print_position_stage(history,stage) :
    return(print_position(history[stage-1][0]))

def print_label_stage(history,stage) :
    return(print_label(history[stage-1][1]))

current_stage=0

while True :

    puzzle=[
    [print_position(2)                  ,print_position(2)                  ,print_position(3)                  ,print_position(4)],
    [print_label(4)                     ,print_position_stage(history,1)    ,print_position(1)                  ,print_position_stage(history,1)],
    [print_label_stage(history,2)       ,print_label_stage(history,1)       ,print_position(3)                  ,print_label(4)],
    [print_position_stage(history,1)    ,print_position(1)                  ,print_position_stage(history,2)    ,print_position_stage(history,2)],
    [print_label_stage(history,1)       ,print_label_stage(history,2)       ,print_label_stage(history,4)       ,print_label_stage(history,3)],
    ]

    nb_screen=input("Current stage : "+str(current_stage+1)+" -- number on screen >> ")

    # doing the heavy lifting
    print(puzzle[current_stage][int(nb_screen)-1])
    # doing jackshit

    current_position=input("position >> ")
    current_label=input("label >> ")

    history[current_stage]=current_position+current_label

    current_stage+=1





