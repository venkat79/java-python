'''
Consider the following sequence of string manipulations -

abccba
abccba - "cc" is a couple as both appear together. Remove the couple from the string and count as "1 couple"
abba - Resulting string after removing the couple
abba - Now "bb" is a couple. Remove the couple from the string and increment the count to 2
aa - After removing the above couple
aa - Now "aa" is a couple. Remove the couple from the string and increment the count to 3

'''
import sys
def removeduplicate(string):
    l = []
    count = 0
    top = -1
    for ch in string:
        if len(l) == 0:
	    l.append(ch)
            top = 0
        elif ch == l[top]:
	    l.pop()
            top = top - 1
            count = count + 1
        else:
	    l.append(ch)
            top = top + 1
    return ''.join(l), count

if __name__ == "__main__":
    if len(sys.argv) < 2:
	print "Error:  Insufficient argument"
    else:
        res, count = removeduplicate(sys.argv[1]) 
        print res, count
            
        
        
       
