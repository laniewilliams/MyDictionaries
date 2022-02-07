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