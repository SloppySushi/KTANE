## r == red
## w == white
## b == blue
## n == black(noir)

provided_wires=""
last_serial_odd=False

def printt(text) :
    formated_text="| "+str(text)+" |"
    print("-"*len(formated_text))
    print(formated_text)
    print("-"*len(formated_text))

def three_wires(provided_wires) :
    if "r" not in provided_wires :
        printt("Cut second")
    elif provided_wires[-1] == "w" :
        printt("Cut last")
    elif provided_wires.count("b")>1 :
        printt("Cut last blue")
    else :
        printt("Cut the last")

def four_wires(provided_wires,last_serial_odd) :
    if provided_wires.count("r")>1 and last_serial_odd :
        printt("Cut last red")
    elif provided_wires[-1] == "y" and ("r" not in provided_wires) :
        printt("Cut the first")
    elif provided_wires.count("b")==1 :
        printt("Cut first")
    elif provided_wires.count("y")>1 :
        printt("Cut the last")
    else :
        printt("cut second")

def five_wires(provided_wires,last_serial_odd) :
    if provided_wires[-1] == "n" and last_serial_odd :
        printt("Cut the fourth")
    elif provided_wires.count("r")==1 and provided_wires.count("y")>1 :
        printt("Cut the first")
    elif "n" not in provided_wires :
        printt("Cut the second")
    else :
        printt("Cut the first")

def six_wires(provided_wires,last_serial_odd) :
    if "y" not in provided_wires and last_serial_odd :
        printt("Cut the third")
    elif provided_wires.count("y")==1 and provided_wires.count("w")>1:
        printt("Cut the fourth")
    elif "r" not in provided_wires :
        printt("Cut the last")
    else :
        printt("Cut the fourth")

def solver(wires_list, last_serial_odd) :
    match len(wires_list) :
        case 3 :
            three_wires(wires_list)
        case 4 :
            four_wires(wires_list,last_serial_odd)
        case 5 :
            five_wires(wires_list,last_serial_odd)
        case 6 :
            six_wires(wires_list,last_serial_odd)
        case _ :
            print("Min number of wires is 3.\nMax number of wires is 6.")

while True :
    wires_list=input("wires colors from top to bottom ==> write from left to right\nExemple : rbnw ==> red blue white black(noir)\n>>").strip()
    if len(wires_list)>= 4 :
        input_odd = input("last digit of serial number is odd y/n\n>>")
        if input_odd in ["y","yes","Y","YES"] :
            last_serial_odd = True
        elif input_odd in ["n","no","non","N","NO","NON"] :
            last_serial_odd = False
        else:
            print("provided input "+input_odd+" doesnt match 'y' or 'n'")
    solver(wires_list,last_serial_odd)
