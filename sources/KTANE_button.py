
provided_color=input("color >> ")
provided_word=input("word >> ")

hold_message="""
HOLD if :
Blue   - release at 4
White  - release at 1
Yellow - release at 5
Other  - release at 1
"""

def solver(provided_color,provided_word) :
    if provided_color=="b" and provided_word in ["abort","Abort"] :
        print(hold_message)
    elif 