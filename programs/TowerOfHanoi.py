def TOH(n,A,B,C):
    if(n>0):
        TOH(n-1,A,C,B)
        print(f"Move a Disc from {A} to {C}")
        TOH(n-1,B,A,C)

TOH(4,1,2,3)

#toh of 4 stnds