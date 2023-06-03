#!/usr/bin/env python

import threading
import time
import subprocess
import os
import sys

os.system('clear')

pkg_missing = []
pkg_halo = []
pkg_tqdm = []
pkg_figlet = []
pkg_toilet = []

try:
    import halo
except ImportError:
    pkg_halo.append('halo')
    pkg_missing.append('halo')

try:
    import tqdm
except ModuleNotFoundError:
    pkg_tqdm.append('tqdm')
    pkg_missing.append('tqdm')

try:
    subprocess.run(['figlet', '-v'], capture_output=True, check=True)
except FileNotFoundError:
    pkg_figlet.append('figlet')
    pkg_missing.append('figlet')

try:
    subprocess.run(['toilet', '-v'], capture_output=True, check=True)
except FileNotFoundError:
    pkg_toilet.append('toilet')
    pkg_missing.append('toilet')

if pkg_missing:
    print('the following package are not installed:', ','.join(pkg_missing))

if pkg_halo:
    print('\033[1m' + '\033[33m{}'.format('\ninstalling package halo') + '\033[0m')
    os.system('pip install halo -y >/dev/null 2>&1')

try:
    from halo import Halo
except:
    Exception

if pkg_tqdm:
    try:
        with Halo(text='\033[1m\033[33mInstalling Tqdm\033[0m', spinner='dots'):
            os.system('pip install tqdm -y >/dev/null 2>&1')
    except:
        Exception

try:
    from tqdm import tqdm
except:
    Exception

if pkg_figlet:
    try:
        with Halo(text='\033[1m\033[33mInstalling Figlet\033[0m', spinner='dots'):
            os.system('pkg install figlet -y >/dev/null 2>&1')
    except:
        Exception

if pkg_toilet:
    try:
        with Halo(text='\033[1m\033[33mInstalling Toilet\033[0m', spinner='dots'):
            os.system('pkg install toilet -y >/dev/null 2>&1')
    except:
        Exception

time.sleep(2)

print('\033[1m' + '\033[33m{}'.format('\ntuturuan kta hon pano mag program') + '\033[0m')

try:
    with Halo(text='\033[1m\033[33mPlease Wait\033[0m', spinner='dots'):
        time.sleep(2)
except:
    Exception

print('\033[1m\033[33m\nprogram successfully started!\033[0m')

time.sleep(5)

os.system('clear')

def flag():
    try:
        os.system('figlet "\n\n"')
        os.system('toilet -f small -F metal "           Python\n        Tutorial"')
        print('                             \033[1m\033[31mby Kyle\033[0m')
    except:
        Exception

flag()

try:
    with Halo(text='\033[1m\033[33mStarting The Program\033[0m', spinner='dots'):
        time.sleep(2)
except:
    Exception

print('\033[1m' + '\033[33m{}'.format('Score: 100\n') + '\033[0m')

print('\033[1m' + '\033[31m{}'.format('Note:\n\033[33mAng overall score ay \033[31m100.. \033[33mNagbabawas ng \033[31m5 points \033[33m kada maling sagot\n\033[33mAng overall score mo dapat hon is \033[31m60 \033[33mabove para maging passed ka.. pero pag nag \033[31m60 \033[33mbelow ka failed kna\n\n') + '\033[0m')

input('\033[1m\033[31mPress\033[33m Enter \033[31mTo Continue\033[0m')

os.system('clear')

try:
    os.system('figlet "\n\n"')
    os.system('toilet -f big -F metal "       Round 1"')
except:
    Exception

def ask():
    print("Ano ang tamang pag print ng statement dito?\na. print done\nb. print+done\nc. print{done}\nd. print('done')")

ask()

a1 = []

authenticated = False
score = 100
while not authenticated:
    try:

        a = input('Answer: ')

        if a == 'a':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            a1.append('')
        elif a == 'b':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            a1.append('')
        elif a == 'c':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            a1.append('')
        elif a == 'd':
            print('\033[1m' + '\033[32m{}'.format('tama ang sagot mo hon, nice hahaha\n') + '\033[0m')
            authenticated = True

    except ValueError:
        print('\033[1m' + '\033[31m{}'.format('letter lng hon gamitin mo') + '\033[0m')
    except (EOFError, KeyboardInterrupt):
        print('\033[1m' + '\033[35m{}'.format('bawal ka mag exit haha') + '\033[0m')

time.sleep(2)

if score == 100:
    print('Your Score:', score)
    print('\033[1m\033[32mPerfect\033[0m\n\n')
elif score < 100:
    print('Your Score:', score, end='\n\n')

input('\033[1m\033[31mPress \033[33mEnter \033[31mTo Continue\033[0m')

os.system('clear')

try:
    os.system('figlet "\n\n"')
    os.system('toilet -f big -F metal "     Round 2"')
except:
    Exception

def ask1():
    print('paano mag print ng variable?\na. print("a")\nb. print a\nc. print(a)\nd. print"a"')

ask1()

b1 = []

authenticated = False
while not authenticated:
    try:

        b = input('Answer: ')

        if b == 'a':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            b1.append('')
        elif b == 'b':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            b1.append('')
        elif b == 'c':
            print('\033[1m' + '\033[32m{}'.format('tama ang sagot mo hon, nice hahaha\n') + '\033[0m')
            authenticated = True
        elif b == 'd':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            b1.append('')
    except ValueError:
        print('\033[1m' + '\033[35m{}'.format('letter lng hon gamitin mo') + '\033[0m')
    except (KeyboardInterrupt, EOFError):
        print('\033[1m' + '\033[35m{}'.format('bawal ka mag exit haha') + '\033[0m')

time.sleep(2)

if score == 100:
    print('Your Score:', score)
    print('\033[1m' + '\033[32m{}'.format('Perfect\n\n') + '\033[0m')
elif score < 100:
    print('Your Score:', score, end='\n\n')

input('\033[1m\033[31mPress \033[33mEnter \033[31mTo Continue\033[0m')

os.system('clear')

try:
    os.system('figlet "\n\n"')
    os.system('toilet -f big -F metal "     Round 3"')
except:
    Exception

def ask2():
    print("paano mag print ng variable?\na. print(f'{a}')\nb. print a\nc. print+a\nd. print('a')")

ask2()

c1 = []

authenticated = False
while not authenticated:

    try:

        c = input('Answer: ')

        if c == 'a':
            print('\033[1m' + '\033[32m{}'.format('tama ang sagot mo hon, nice haha\n') + '\033[0m')
            authenticated = True
        elif c == 'b':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            c1.append('')
        elif c == 'c':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            c1.append('')
        elif c == 'd':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            c1.append('')
    except ValueError:
        print('\033[1m' + '\033[35m{}'.format('letter lng hon gamitin mo') + '\033[0m')
    except (KeyboardInterrupt, EOFError):
        print('\033[1m' + '\033[35m{}'.format('bawal ka mag exit haha') + '\033[0m')

time.sleep(2)

if score == 100:
    print('Your Score:', score)
    print('\033[1m' + '\033[32m{}'.format('Perfect\n\n') + '\033[0m')
elif score < 100:
    print('Your Score:', score, end='\n\n')

input('\033[1m\033[31mPress \033[33mEnter \033[31mTo Continue\033[0m')

os.system('clear')

try:
    os.system('figlet "\n\n"')
    os.system('toilet -f big -F metal "     Round 4"')
except:
    Exception

def ask3():
    print("paano mag print ng variable?\na. print('a')\nb. print+a\nc. print(''.join(a))\nd. print()a")

ask3()

d1 = []

authenticated = False
while not authenticated:

    try:

        d = input('Answer: ')

        if d == 'a':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            d1.append('')
        elif d == 'b':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            d1.append('')
        elif d == 'c':
            print('\033[1m' + '\033[32m{}'.format('tama ang sagot mo hon, nice haha\n') + '\033[0m')
            authenticated = True
        elif d == 'd':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            d1.append('')
    except ValueError:
        print('\033[1m' + '\033[35m{}'.format('letter lng hon gamitin mo') + '\033[0m')
    except (KeyboardInterrupt, EOFError):
        print('\033[1m' + '\033[35m{}'.format('bawal ka mag exit haha') + '\033[0m')

time.sleep(2)

if score == 100:
    print('Your Score:', score)
    print('\033[1m' + '\033[32m{}'.format('Perfect\n\n') + '\033[0m')
elif score < 100:
    print('Your Score:', score, end='\n\n')

input('\033[1m\033[31mPress \033[33mEnter \033[31mTo Continue\033[0m')

os.system('clear')

try:
    os.system('figlet "\n\n"')
    os.system('toilet -f big -F metal "     Round 5"')
except:
    Exception

def ask4():
    print('Ano ang tamang sign ng newline?\na. n/\nb. /n\nc. \\n\nd. n\\')

ask4()

e1 = []

authenticated = False
while not authenticated:
    try:

        e = input('Answer: ')

        if e == 'a' or e == 'b' or e == 'd':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            e1.append('')
        elif e == 'c':
            print('\033[1m' + '\033[32m{}'.format('tama ang sagot mo hon, nice haha\n') + '\033[0m')
            authenticated = True
    except ValueError:
        print('\033[1m' + '\033[35m{}'.format('letter lng hon gamitin mo') + '\033[0m')
    except (KeyboardInterrupt, EOFError):
        print('\033[1m' + '\033[35m{}'.format('bawal ka mag exit haha') + '\033[0m')

time.sleep(2)

if score == 100:
    print('Your Score:', score)
    print('\033[1m' + '\033[32m{}'.format('Perfect\n\n') + '\033[0m')
elif score < 100:
    print('Your Score:', score, end='\n\n')

input('\033[1m\033[31mPress \033[33mEnter \033[31mTo Continue\033[0m')

os.system('clear')

try:
    os.system('figlet "\n\n"')
    os.system('toilet -f big -F metal "     Round 6"')
except:
    Exception

def ask5():
    print("Ano ang tamang pag print ng variable? Except!\na. print(a)\nb. print(f'{a}')\nc.print(''.join(a))\nd. print(f'a')")

ask5()

f1 = []

authenticated = False
while not authenticated:
    try:

        f = input('Answer: ')

        if f == 'a' or f == 'b' or f == 'c':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            f1.append('')
        elif f == 'd':
            print('\033[1m' + '\033[32m{}'.format('tama ang sagot mo hon, nice haha\n') + '\033[0m')
            authenticated = True
    except ValueError:
        print('\033[1m' + '\033[35m{}'.format('letter lng hon gamitin mo') + '\033[0m')
    except (KeyboardInterrupt, EOFError):
        print('\033[1m' + '\033[35m{}'.format('bawal ka mag exit haha') + '\033[0m')

time.sleep(2)

if score == 100:
    print('Your Score:', score)
    print('\033[1m' + '\033[32m{}'.format('Perfect\n\n') + '\033[0m')
elif score < 100:
    print('Your Score:', score, end='\n\n')

input('\033[1m\033[31mPress \033[33mEnter \033[31mTo Continue\033[0m')

os.system('clear')

try:
    os.system('figlet "\n\n"')
    os.system('toilet -f big -F metal "     Round 7"')
except:
    Exception

def ask6():
    print("a = 'I Love You Honey Ko'\n\nPaano iprint ang variable 'a' na nasa taas?\na. print('', a)\nb. print('a')\nc. print(', a')\nd. print(,a)")

ask6()

g1 = []

authenticated = False
while not authenticated:
    try:

        g = input('Answer: ')

        if g == 'b' or g == 'c' or g == 'd':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            g1.append('')
        elif g == 'a':
            print('\033[1m' + '\033[32m{}'.format('tama ang sagot mo hon, nice haha\n') + '\033[0m')
            authenticated = True
    except ValueError:
        print('\033[1m' + '\033[35m{}'.format('letter lng hon gamitin mo') + '\033[0m')
    except (KeyboardInterrupt, EOFError):
        print('\033[1m' + '\033[35m{}'.format('bawal ka mag exit haha') + '\033[0m')

time.sleep(2)

if score == 100:
    print('Your Score:', score)
    print('\033[1m' + '\033[32m{}'.format('Perfect\n\n') + '\033[0m')
elif score < 100:
    print('Your Score:', score, end='\n\n')

input('\033[1m\033[31mPress \033[33mEnter \033[31mTo Continue\033[0m')

os.system('clear')

try:
    os.system('figlet "\n\n"')
    os.system('toilet -f big -F metal "     Round 8"')
except:
    Exception

def ask7():
    print("a = 'I Love You Honey Ko'\n\nPaano ang iprint ang variable 'a' na nasa taas? Kumpletuhin ang binigay na print statement na nasa baba.\n\nprint(f'____)\n\na. print(f'a')\nb. print(f'', {a})\nc. print(f'{a})\nd. print(f'{a}')")

ask7()

h1 = []

authenticated = False
while not authenticated:
    try:
        h = input('Answer: ')

        if h == 'a' or h == 'b' or h == 'c':
            print('\033[1m' + '\033[31m{}'.format('mali ang sagot mo, ulitin mo') + '\033[0m')
            score -= 5
            h1.append('')
        elif h == 'd':
            print('\033[1m' + '\033[32m{}'.format('tama ang sagot mo hon, nice haha\n') + '\033[0m')
            authenticated = True
    except ValueError:
        print('\033[1m' + '\033[35m{}'.format('letter lng hon gamitin mo') + '\033[0m')
    except (KeyboardInterrupt, EOFError):
        print('\033[1m' + '\033[35m{}'.format('bawal ka mag exit haha') + '\033[0m')

time.sleep(2)

if score == 100:
    print('Your Score:', score)
    print('\033[1m' + '\033[32m{}'.format('Perfect\n\n') + '\033[0m')
elif score < 100:
    print('Your Score:', score, end='\n\n')

input('\033[1m\033[31mPress \033[33mEnter \033[31mTo Continue In Test Result\033[0m')

os.system('clear')

os.system('toilet -f small -F metal "    Test  Result"')

try:
    with Halo(text='\033[1m\033[33mProcessing Test Result\033[0m', spinner='dots'):
        time.sleep(5)
except:
    Exception

if score == 100:
    print('Your Score:', score)
    print('\033[1m' + '\033[32m{}'.format('Perfect\n\n') + '\033[0m')
elif score < 100:
    print('Your Score:', score, end='\n\n')

if score == 100:
    print('\033[1m' + '\033[33m{}'.format('You Have Passed The Test With Perfect Score, Congrats Honeeyy Koo') + '\033[0m')
    print('\033[1m' + '\033[32m{}'.format('Ginalingan HAHAHAHA\n') + '\033[0m')
elif score >= 60:
    print('\033[1m' + '\033[33m{}'.format('You Have Passed The Test, Congrats Honeeyy Koo\n') + '\033[0m')
elif score < 60:
    print('\033[1m' + '\033[31m{}'.format('You Have Failed The Test, Better Luck Next Time Honeeyy Koo\n') + '\033[0m')

if score == 100:
    print('\033[1m' + '\033[33m{}'.format('Knowledge Grade: Outstanding\n\n') + '\033[0m')
elif score >= 80:
    print('\033[1m' + '\033[33m{}'.format('Knowledge Grade: Very Good\n\n') + '\033[0m')
elif score >= 60:
    print('\033[1m' + '\033[33m{}'.format('Knowledge Grade: Good\n\n') + '\033[0m')
elif score <= 60:
    print('\033[1m' + '\033[33m{}'.format('Knowledge Grade: Poor\n\n') + '\033[0m')

input('\033[1m\033[31mPress \033[33mEnter \033[31mTo Continue In Reviewer\033[0m')

os.system('clear')

try:
    os.system('toilet -f small -F metal "       Reviewer"')
    print('                                 \033[1m\033[31mBy Kyle\033[0m')
except:
    Exception

if a1:
    print('\033[1m' + '\033[31m{}'.format('Question 1: Mistake') + '\033[0m')
else:
    print('\033[1m' + '\033[31m{}'.format('Question 1: \033[32mCorrect') + '\033[0m')
ask()
print("\nAnswer: d. print('done')\n\n")

if b1:
    print('\033[1m' + '\033[31m{}'.format('Question 2: Mistake') + '\033[0m')
else:
    print('\033[1m' + '\033[31m{}'.format('Question 2: \033[32mCorrect') + '\033[0m')
ask1()
print('\nAnswer: c. print(a)\n\n')

if c1:
    print('\033[1m' + '\033[31m{}'.format('Question 3: Mistake') + '\033[0m')
else:
    print('\033[1m' + '\033[31m{}'.format('Question 3: \033[32mCorrect') + '\033[0m')
ask2()
print("\nAnswer: a. print(f'{a}')\n\n")

if d1:
    print('\033[1m' + '\033[31m{}'.format('Question 4: Mistake') + '\033[0m')
else:
    print('\033[1m' + '\033[31m{}'.format('Question 4: \033[32mCorrect') + '\033[0m')
ask3()
print("\nAnswer: c. print(''.join(a))\n\n")

if e1:
    print('\033[1m' + '\033[31m{}'.format('Question 5: Mistake') + '\033[0m')
else:
    print('\033[1m' + '\033[31m{}'.format('Question 5: \033[32mCorrect') + '\033[0m')
ask4()
print('\nAnswer: c. \\n\n\n')

if f1:
    print('\033[1m' + '\033[31m{}'.format('Question 6: Mistake') + '\033[0m')
else:
    print('\033[1m' + '\033[31m{}'.format('Question 6: \033[32mCorrect') + '\033[0m')
ask5()
print("\nAnswer: d. print(f'a')\n\n")

if g1:
    print('\033[1m' + '\033[31m{}'.format('Question 7: Mistake') + '\033[0m')
else:
    print('\033[1m' + '\033[31m{}'.format('Question 7: \033[32mCorrect') + '\033[0m')
ask6()
print("\nAnswer: a. print('', a)\n\n")

if h1:
    print('\033[1m' + '\033[31m{}'.format('Question 8: Mistake') + '\033[0m')
else:
    print('\033[1m' + '\033[31m{}'.format('Question 8: \033[32mCorrect') + '\033[0m')
ask7()
print("\nAnswer: d. print(f'{a}')\n\n")

input('\033[1m\033[31mPress \033[33mEnter \033[31mTo Exit\033[0m')

os.system('clear')
sys.exit()
