# NAVAL BATTLE

# -- START CLASS -----------------------------------
class naval_map :
    def __init__(self, segments):
        self.segments=segments
        self.final=list()

    def __str__(self):
        result="---- layout of the map - len : "+str(len(self.segments))+" ----\n"
        for i in self.segments :
            result+=str(i)+"\n"
        return result+"----------------------------------------"

    def init_start(self,start):
        result=[]
        to_append=[]
        to_remove=[]

        for current_segment in self.segments :
            if start in current_segment :
                # we are in a segment
                if (start != current_segment[0] and start != current_segment[-1]):
                    half = current_segment.index(start)
                    list_aa, list_bb = current_segment[:half+1], current_segment[half:]
                    # not appending since this is the only result we want and should get
                    result=[list_aa[::-1],list_bb]
                    to_append=[list_aa[::-1],list_bb]
                    to_remove=[current_segment]
                    break
                # we are on an edge
                elif start == current_segment[-1] :
                    result.append(current_segment[::-1])
                    to_append.append(current_segment[::-1])
                    to_remove.append(current_segment)
                elif start == current_segment[0] :
                    # on the previous elif we add a new segment that we have a ignore or its present 2 times
                    if current_segment not in result :
                        result.append(current_segment)
                else :
                    print("YOU SHOULDNT BE HERE. suicide is advised.")

        for i in to_append :
            self.segments.append(i)
        for i in to_remove :
            self.segments.remove(i)
        return result

    # return a list of the segments starting or ending on the provided edge
    def get_segments(self,point,provided_segment=[]):
        result=[]
        for i in self.segments :
            if ( i == provided_segment ) or ( i[::-1] == provided_segment):
                #doing nothing
                pass
            elif  i[0] == point : 
                result.append(i)
            elif  i[-1] == point :
                result.append(i[::-1])
                self.segments[self.segments.index(i)][::-1]
        return result

    def solve_magic(self,start,stop) :
        self.init_start((start))
        segments=self.get_segments((start),[])
        for seg in segments:
            result=self.get_path(start,stop,seg,[])
        road = [item for sublist in self.final for item in sublist]
        #print(list(dict.fromkeys(road)))
        return self.get_instruction(list(dict.fromkeys(road))),list(dict.fromkeys(road))


    def get_path(self,current_position,stop,current_segment,pathing):
        if stop in current_segment:
            pathing.append(current_segment)
            self.final=pathing.copy()
            return

        if not current_segment:
            return

        # starting at the end of the segment
        current_position=current_segment[-1]

        next_segments=self.get_segments(current_position,current_segment)

        if next_segments:
            for potential_segement in next_segments:
                previous_position = current_position
                pathing.append(current_segment)
                self.get_path(current_position,stop,potential_segement,pathing)
                current_position = previous_position
                pathing.pop()

    def get_instruction(self,road) :
        instructions=[]
        for i in range(len(road)-1) :
            if road[i][0] > road[i+1][0] :
                instructions.append("←LEFT")
            elif road[i][0] < road[i+1][0] :
                instructions.append("RIGHT→")
            else:
                if road[i][1] > road[i+1][1] :
                    instructions.append("UP↑")
                elif road[i][1] < road[i+1][1] :
                    instructions.append("DOWN↓")
                else:
                    print("ERROR YOU SHOULDNT BE HERE. suicide is advised.")
        return instructions
# -- END CLASS -------------------------------------

# -- START HARD CODE MAP ---------------------------
segments_a=[]
segment_a_1=[(5,6),(6,6),(6,5),(6,4)]
segment_a_2=[(6,4),(5,4)]
segment_a_3=[(6,4),(6,3)]
segment_a_4=[(6,3),(5,3),(4,3),(4,4),(3,4)]
segment_a_5=[(6,3),(6,2),(5,2),(4,2),(4,1),(5,1),(6,1)]
segment_a_6=[(3,4),(2,4)]
segment_a_7=[(3,4),(3,3),(2,3),(2,2),(3,2),(3,1),(2,1),(1,1),(1,2),(1,3),(1,4),(1,5)]
segment_a_8=[(1,5),(2,5),(3,5),(3,6),(4,6),(4,5),(5,5)]
segment_a_9=[(1,5),(1,6),(2,6)]
segments_a=[segment_a_1,segment_a_2,segment_a_3,segment_a_4,segment_a_5,segment_a_6,segment_a_7,segment_a_8,segment_a_9]

segments_b=[]
segment_b_1=[(6,6),(6,5),(6,4)]
segment_b_2=[(6,4),(6,3),(6,2)]
segment_b_3=[(6,2),(6,1),(5,1),(4,1),(3,1)]
segment_b_4=[(6,4),(5,4),(4,4)]
segment_b_5=[(4,4),(4,3),(4,2)]
segment_b_6=[(4,4),(4,3),(5,3)]
segment_b_7=[(6,2),(5,2),(4,2),(3,2),(3,3),(2,3),(2,2),(2,1),(1,1),(1,2),(1,3),(1,4),(1,5)]
segment_b_8=[(1,5),(1,6),(2,6),(3,6),]
segment_b_9=[(1,5),(2,5),(3,5),(4,5),(5,5),(5,6),(4,6)]
segments_b=[segment_b_1,segment_b_2,segment_b_3,segment_b_4,segment_b_5,segment_b_6,segment_b_7,segment_b_8,segment_b_9]

segments_c=[]
segment_c_1=[(6,4),(6,5),(6,6),(5,6)]
segment_c_2=[(5,6),(5,5),(4,5),(3,5),(3,4)]
segment_c_3=[(5,6),(5,6),(4,6),(3,6),(2,6),(1,6),(1,5),(1,4),(2,4),(2,5)]
segment_c_4=[(3,4),(3,3),(4,3)]
segment_c_5=[(3,4),(4,4),(5,4),(5,3),(6,3),(6,2),(6,1),(5,1),(5,2),(4,2),(4,1),(3,1),(2,1),(1,1),(1,2),(1,3),(2,3),(2,2),(3,2)]
segments_c=[segment_c_1,segment_c_2,segment_c_3,segment_c_4,segment_c_5]

segments_d=[]
segment_d_1=[(5,4),(5,5),(4,5),(4,6),(5,6),(6,6),(6,5),(6,4),(6,3)]
segment_d_2=[(6,3),(5,3),(4,3),(4,4),(3,4),(3,5),(3,6),(2,6),(2,5)]
segment_d_3=[(6,3),(6,2),(5,2),(5,1)]
segment_d_4=[(5,1),(6,1)]
segment_d_5=[(5,1),(4,1),(4,2),(3,2),(3,3),(2,3),(2,4),(1,4)]
segment_d_6=[(1,4),(1,5),(1,6)]
segment_d_7=[(1,4),(1,3),(1,2),(2,2),(2,1)]
segment_d_8=[(2,1),(1,1)]
segment_d_9=[(2,1),(3,1)]
segments_d=[segment_d_1,segment_d_2,segment_d_3,segment_d_4,segment_d_5,segment_d_6,segment_d_7,segment_d_8,segment_d_9]

segments_e=[]
segment_e_1=[(5,4),(5,3),(6,3),(6,4),(6,5),(6,6),(5,6),(4,6),(3,6),(2,6),(2,5),(3,5),(4,5)]
segment_e_2=[(4,5),(5,5)]
segment_e_3=[(4,5),(4,4),(3,4),(2,4),(2,3),(1,3)]
segment_e_4=[(1,3),(1,4),(1,5),(1,6)]
segment_e_5=[(1,3),(1,2),(2,2),(3,2),(4,2)]
segment_e_6=[(4,2),(4,3),(3,3)]
segment_e_7=[(4,2),(5,2),(5,1)]
segment_e_8=[(5,1),(6,1),(6,2)]
segment_e_9=[(5,1),(4,1),(3,1),(2,1),(1,1)]
segments_e=[segment_e_1,segment_e_2,segment_e_3,segment_e_4,segment_e_5,segment_e_6,segment_e_7,segment_e_8,segment_e_9]

segments_f=[]
segment_f_1=[(6,6),(5,6),(4,6),(3,6),(2,6)]
segment_f_2=[(2,6),(2,5)]
segment_f_3=[(2,6),(1,6),(1,5),(1,4),(1,3),(1,2)]
segment_f_4=[(1,2),(1,1)]
segment_f_5=[(1,2),(2,2)]
segment_f_6=[(2,2),(3,2)]
segment_f_7=[(2,2),(2,1),(3,1),(4,1),(4,2),(5,2),(5,1),(6,1),(6,2),(6,3),(6,4),(5,4)]
segment_f_8=[(5,4),(3,4)]
segment_f_9=[(5,4),(5,3),(4,3),(3,3),(2,3),(2,4),(3,4),(3,5),(4,5),(5,5),(5,6)]
segments_f=[segment_f_1,segment_f_2,segment_f_3,segment_f_4,segment_f_5,segment_f_6,segment_f_7,segment_f_8,segment_f_9]

segments_g=[]
segment_g_1=[(4,1),(4,2),(5,2),(5,1),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(5,6),(5,5),(5,4),(5,3),(4,3),(4,4),(4,5),(4,6),(3,6),(2,6),(1,6),(1,5),(1,4),(1,3),(2,3)]
segment_g_2=[(2,3),(2,2)]
segment_g_3=[(2,3),(2,4),(2,5),(3,5),(3,4),(3,3),(3,2),(3,1),(2,1),(1,1),(1,2)]
segments_g=[segment_g_1,segment_g_2,segment_g_3]

segments_h=[]
segment_h_1=[(5,6),(6,6),(6,5)]
segment_h_2=[(6,5),(6,4)]
segment_h_3=[(6,5),(5,5),(5,4),(5,3),(6,3),(6,2),(6,1),(5,1)]
segment_h_4=[(5,1),(4,1)]
segment_h_5=[(5,1),(5,2),(4,2),(4,3),(4,4)]
segment_h_6=[(4,4),(3,4),(3,5)]
segment_h_7=[(4,4),(4,5),(4,6),(3,6),(2,6),(1,6),(1,5),(2,5),(2,4),(1,4),(1,3)]
segment_h_8=[(1,3),(1,2),(1,1)]
segment_h_9=[(1,3),(2,3),(2,2),(2,1),(3,1),(3,2),(3,3)]
segments_h=[segment_h_1,segment_h_2,segment_h_3,segment_h_4,segment_h_5,segment_h_6,segment_h_7,segment_h_8,segment_h_9]

segments_i=[]
segment_i_1=[(6,5),(6,4)]
segment_i_2=[(6,4),(5,4)]
segment_i_3=[(6,4),(6,3),(6,2),(6,1),(5,1)]
segment_i_4=[(5,1),(5,2),(5,3),(4,3),(4,4),(3,4),(3,5),(3,6),(4,6),(4,5),(5,5),(5,6),(6,6)]
segment_i_5=[(5,1),(4,1),(3,1),(2,1),(2,2),(2,3)]
segment_i_6=[(2,3),(3,3),(3,2),(4,2)]
segment_i_7=[(2,3),(1,3)]
segment_i_8=[(1,3),(1,2),(1,1)]
segment_i_9=[(1,3),(1,4),(1,5),(1,6),(2,6),(2,5),(2,4)]
segments_i=[segment_i_1,segment_i_2,segment_i_3,segment_i_4,segment_i_5,segment_i_6,segment_i_7,segment_i_8,segment_i_9]

all_segment=[segments_a,segments_b,segments_c,segments_d,segments_e,segments_f,segments_g,segments_h,segments_i]

# -- END HARD CODE MAP -----------------------------

# -- START MAIN ------------------------------------

identifications_array = [
[(1,2),(6,3)],
[(1,1),(1,4)],
[(2,1),(2,6)],
[(5,2),(2,4)],
[(5,3),(4,6)],
[(4,1),(3,4)],
[(4,4),(6,4)],
[(5,1),(3,5)],
[(3,2),(1,6)]
]

def getNavalMap():
    userInput = input("'map identification point' 'start' 'stop'\ninput : ").replace(" ","")
    map_id    = tuple(map(int,userInput[:2]))
    start     = tuple(map(int,userInput[2:4]))
    stop      = tuple(map(int,userInput[4:6]))

    for index,_list in enumerate(identifications_array) :
        if map_id in _list :
            return index,start,stop
    print("ERROR : provided identification number "+str(map_id)+" doesnt match any known map")

def main():

    map_index,start,stop = getNavalMap()

    #print("-- MAP IDENTIFICATION : "+str(map_index))
    print("-- START POSITION     : "+str(start))
    print("-- STOP  POSITION     : "+str(stop))

    # create the map object
    chosen_map=naval_map(all_segment[map_index])
    instruction, result=chosen_map.solve_magic(start,stop)

    # print result
    print("-- PATH TO FOLLOW     : "+str(len(instruction))+" instructions")
    for i in instruction:
        print("     "+i)

    # -- END MAIN --------------------------------------

    # -- PRINT VISUAL ----------------------------------
    # create empty matrix
    rows = 6
    cols = 6
    matrix = [[ "0" for _ in range(cols)] for _ in range(rows)]

    # adding indicators for start and end
    instruction[0]="*"+instruction[0]
    instruction.append("FINISH")

    position=0
    for i in result:
        matrix[i[1]-1][i[0]-1]=instruction[position]
        position+=1

    # adding missing "|"
    matrix[0][0]="|"+matrix[0][0]
    matrix[-1][-1]=matrix[-1][-1]+"\t|"


    print("-- PATH TO FOLLOW     : ")
    print("•-----------------------------------------------•")
    print('\t|\n|'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
    print("•-----------------------------------------------•")


while True:
    main()