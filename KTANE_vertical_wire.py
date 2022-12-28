# VERTICAL WIRES
all_possibilities=[]

C_list=[
"CUT THE WIRE",
"rs",
"rsw",
"w",
"sw",
]
D_list=[
"DONT CUT THE WIRE",
"bs",
"bsw",
"lw",
"blrs",
]
S_list=[
"CUT IF LAST DIGIT OF SERIAL NUMBER IS EVEN",
"r",
"rw",
"b",
"bw",
"br",
"blr",
]
P_list=[
"CUT IF THE BOMBE HAS PARALLEL PORT",
"bl",
"blw",
"bls",
"blsw",
"brs",
]
B_list=[
"CUT IF THE BOMBE HAS 2 OR MORE BATTERIES",
"lr",
"lrw",
"lrs",
"lrsw",
"lsw",
]

all_possibilities.append(C_list)
all_possibilities.append(D_list)
all_possibilities.append(S_list)
all_possibilities.append(P_list)
all_possibilities.append(B_list)

while True :
    provided=input("sequence >>")
    for possibilities in all_possibilities :
        for entry in possibilities :
            if "".join(sorted(provided)) == entry :
                print(possibilities[0])
                pass

