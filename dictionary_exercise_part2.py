codes = {'A':'!',
             'a':'@',
             'B':'#',
             'b':'$',
             'C':'%',
             'c':'^',
             'D':'&',
             'd':'*',
             'E':'-',
             'e':'+',
             'F':'=',
             'f':'<',
             'G':'>',
             'g':'/',
             'H':'?',
             'h':'~',
             'I':'1',
             'i':'2',
             'J':'3',
             'j':'4',
             'K':'5',
             'k':'6',
             'L':'7',
             'l':'8',
             'M':'9',
             'm':'0',
             'N':'[',
             'n':']',
             'O':'{',
             'o':'}',
             'P':'_',
             'p':'|',
             'Q':':',
             'q':';',
             'R':'o',
             'r':'p',
             'S':'e',
             's':'b',
             'T':'y',
             't':'a',
             'U':'u',
             'u':'m',
             'V':'q',
             'v':'w',
             'W':'r',
             'w':'t',
             'X':'i',
             'x':'s',
             'Y':'d',
             'y':'f',
             'Z':'g',
             'z':'h'}

text = open('info_security.txt','r')
read_text = text.read()
print(read_text)
#encryption = open('encrypted.txt','w')

output = ""

for letter in read_text:
    if letter in codes:
        output += codes[letter]
print(output)

text.close()