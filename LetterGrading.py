"""Prompt user for a grade in numbers and output their grade in the letter scale"""


number = int(input('Enter your numeric grade: '))

if number>=93:
    print(f'Your letter grade for {number} is A')
if number>=90 and number<= 92:
    print(f'Your letter grade for {number} is A-')
if number>=87 and number<= 89:
    print(f'Your letter grade for {number} isB+')
if number>=83 and number<= 86:
    print(f'Your letter grade for {number} is B')
if number>=80 and number<= 82:
    print(f'Your letter grade for {number} is B-')
if number>=77 and number<= 79:
    print(f'Your letter grade for {number} is C+')
if number>=73 and number<= 76:
    print(f'Your letter grade for {number} is C')
if number>=70 and number<= 72:
    print(f'Your letter grade for {number} is C-')
if number>=67 and number<= 69:
    print(f'Your letter grade for {number} is D+')
if number>=63 and number<= 66:
    print(f'Your letter grade for {number} is D')
if number>=60 and number<= 62:
    print(f'Your letter grade for {number} is D-')
if number < 60:
    print(f'Your letter grade for {number} is F')
