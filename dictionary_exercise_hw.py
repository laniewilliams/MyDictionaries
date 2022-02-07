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

print('Please enter your course number.')
number = input()

if number in course_room:
    print('The room number is',course_room[number])
    print('The instructor is',course_instr[number])
    print('The meeting time is',course_time[number])
else:
    print('No information available.')