def EstBinaire(ch):
    for c in ch:
        if c== '0' or c == '1':
            pass
        else: 
            return False
    return True
        
        
print(EstBinaire("02"))

##def remplacee(ch, c1, c2):
##    output = ""
##    for i in range(0, len(ch)):
##    
##        if i == c2:
##            
##        else:
##            output += ch[i]
##    return (output)
##print(remplacee("hello"))
##        
##            
##            
##        
##
def remplace(ch,ch1,ch2):
    output = ""
    for x in range (0, len(ch)):
        if x == ch1:
            x == ch2
            output = x
        else:
            output += ch[x]
    return (output)
change = remplace("Hello", "H", "e")
print(change)
   
