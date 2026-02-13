import time
from typing import Tuple



"""
   -- 0 --
  |       |
  5       1
  |       |
   -- 6 --
  |       |
  4       2
  |       |
   -- 3 --
"""




def printDivider(bIn,x):
    if(bIn[x] == "1"): 
        print("   -------   ")
    else:
        print("             ") 




def render_digit(bIn):

    printDivider(bIn,-1)
        
    
    for i in range(3):
        
        lineStr = ""
    
        lineStr += "  |" if bIn[-6]  == "1" else "   "
        lineStr += "       |" if bIn[-2]  == "1" else "        "

        print(lineStr)


    printDivider(bIn,-7)

    for i in range(3):
        
        lineStr = ""
    
        lineStr += "  |" if bIn[-5] == "1" else "   "
        lineStr += "       |" if bIn[-3] == "1" else "        "
        print(lineStr)

    printDivider(bIn,-4)

    




def printSequence(sequenceList: Tuple[str, ...] ,Tdt = .5,repCnt = 1 ):
    """
    Docstring for printSequence
    
    :param sequenceList: A tuple containing strings with a 7 bit binary string representing each display section
    :type sequenceList: Tuple[str, ...]
    :param Tdt: Time delay in between character displays
    :param repCnt: how many times the sequence should be looped over 
    """

    
    print("\n \n \n")
    
    for foo in range(repCnt):
        for digit in sequenceList:
            render_digit(digit)
            time.sleep(Tdt)
            print("\n \n \n")
        
        

test_digits_rtl = [
    "0111111",  # 0 → LSB is a (rightmost)
    "0000110",  # 1
    "1011011",  # 2
    "1001111",  # 3
    "1100110",  # 4
    "1101101",  # 5
    "1111101",  # 6
    "0000111",  # 7
    "1111111",  # 8
    "1101111"   # 9
]


printSequence(test_digits_rtl)










    

