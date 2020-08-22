from random import shuffle

def shuff(a):
     shuffle(a)
     return a   


def usergss():
    abc = ''
    while abc not in ['0','1','2']:
        abc = input("\nGuess 0 or 1 or 2 \n")
        
    return int(abc)
    
def check_gss(cc,bca):
    if a[bca] == '0':
        print("\nWIN")
    else:
        print("\n***WRONG GUESS***")
        #print(a)
        for index,valuee in enumerate(a):
            if valuee == '0':
                print("*Correct Ans is ==>  " +str(index))
            
        
        
a = ['','0','']        

shufflist = shuff(a)

bca = usergss()

check_gss(shufflist,bca)