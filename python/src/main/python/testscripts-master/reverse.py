'''
Write a recursive function which will take a string and return the reverse of that string. Define a function with a definition as below -

String reverse(String str)
'''
import sys
def reverse(s):
    '''
      return s[::-1] this is the shortcut that will also return the reverse of the string
      python string is immutable so we need to take it out either using list or some string
    
    return s[::-1]

    s = ''.join(reversed(s))
    return s
    '''

    str_list = []
    for i in range(len(s)-1, -1, -1):
        str_list.append(s[i])

    s = ''.join(str_list)
    return s

if __name__ == "__main__":
    if len(sys.argv) < 2:
	print "Error: Pass string from commond promt"
    else:
        print reverse(sys.argv[1])


