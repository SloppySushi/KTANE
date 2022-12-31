# PASSWORD
words = [
"about","after","again","below",
"could","every","first","found",
"great","house","large","learn",
"never","other","place","plant",
"point","right","small","sound",
"spell","still","study","their",
"there","these","thing","think",
"three","water","where","which",
"world","would","write",]

letters=[]
skipped=[]

while True :
    inputLetter=input(f'Insert characters to solve password\n>> ')
    letters.append(inputLetter)
    for i in range(len(letters)) :
        for word in words :
            if word in skipped :
                pass
            elif word[i] in letters[i] :
                pass
            else :
                skipped.append(word)

    print("-------------")
    for word in words :
        if word not in skipped :
            print(word)
    print("-------------")
