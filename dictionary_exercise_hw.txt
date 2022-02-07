#-----------------PART 1---------------------------

course_room = {'CS101':'3004',
             'CS102':'4501',
             'CS103':'6755',
             'NT110':'1244',
             'CM241':'1411'}

course_instr = {'CS101':'Haynes',
             'CS102':'Alvarado',
             'CS103':'Rich',
             'NT110':'Burke',
             'CM241':'Lee'}

course_time = {'CS101':'8:00 a.m.',
             'CS102':'9:00 a.m.',
             'CS103':'10:00 a.m.',
             'NT110':'11:00 a.m.',
             'CM241':'1:00 p.m.'}

print('Please enter your course number and press enter.')
number = input()

if number in course_room:
    print('Room number:',course_room[number])
    print('Instructor:',course_instr[number])
    print('Meeting time:',course_time[number])
else:
    print('No information available.')


#--------------PART 2--------------------------------

codes = {'A':'!',
             'a':'@',
             'B':'#',
             'b':'$',
             'C':'%',
             'c':'^',
             'D':'&',
             'd':'*',
             'E':'j',
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
             'P':'z',
             'p':'v',
             'Q':':',
             'q':';',
             'R':'x',
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


output = ""

for letter in read_text:
    if letter in codes:
        output += codes[letter]
    else:
        output += letter

text.close()

encryption = open('encrypted.txt','w')
encryption.write(output)

encryption.close()