import sys
import os
import random
import time
from sys import stderr


Bl='\033[30m' # VARIABLE COLOR 
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

os.system('clear')

def autoketik(x): # AUTOKETIK CUY!!
    for y in x + "\n":
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(0.030)

while True: #wHILE TRUE
    print(f"\n{Wh}[{Gr}+{Wh}] {Ye}LOGIN YOUR GAME")
    name = input(f"\n{Gr}Input Full Name {Wh}:{Ye} ")
    status = int(input(f"{Gr}Age {Wh}            :{Ye} "))
    if status >= 100:
        print("LU DH TUA")
        sys.exit()
    os.system('clear')
    break

print()
def animasi():    
            for i in range(25):
                sys.stdout.write(f'\r{Wh}LOADING YOUR GAME{Gr}  🙂')
                time.sleep(0.3)
                sys.stdout.write(f'\r{Wh}LOADING YOUR GAME{Gr}  😜')
                time.sleep(0.3)
                sys.stdout.write(f'\r{Wh}LOADING YOUR GAME{Gr}  🙂')
                time.sleep(0.3)
            sys.stdout.write(f'\r{Wh}LOADING YOUR GAME{Gr}  😜')
            time.sleep(0.3)
            os.system('clear')
animasi()

def banner():
    stderr.writelines(f"""{Ye}
    __________                     .__                    __      __                .___
    \______   \__ _________________|  |   ____           /  \    /  \___________  __| _/
    |     ___/  |  \___   /\___   /  | _/ __ \   ______ \   \/\/   /  _ \_  __ \/ __ | 
    |    |   |  |  //    /  /    /|  |_\  ___/  /_____/  \        (  <_> )  | \/ /_/ | 
    |____|   |____//_____ \/_____ \____/\___  >           \__/\  / \____/|__|  \____ | 
                        \/      \/         \/                 \/                   \/ 
    <<  {Wh}WORD  PUZZLE  GAME   {Ye}<<{Wh}============================{Ye}>>    {Wh}AUTHOR  BY  HUNBYTS >>

                  {Gr} ----------------------------------------------- 
                    {Wh}|             {Ye}.:: {Wh}MENU GAME {Ye}::.             {Wh}| 
                    {Wh}|                                           {Wh}|
                    {Wh}|   {Ye}[{Gr}1{Ye}] {Wh}NOOB                                {Wh}|
                    {Wh}|   {Ye}[{Gr}2{Ye}] {Wh}MEDIUM                              {Wh}|
                    {Wh}|   {Ye}[{Gr}3{Ye}] {Wh}HIGH                 {Gr}[{Ye}COMING SOON{Gr}]  {Wh}|
                    {Wh}|   {Ye}[{Gr}4{Ye}] {Wh}LEGEND               {Gr}[{Ye}COMING SOON{Gr}]  {Wh}|
                    {Wh}|   {Ye}[{Gr}5{Ye}] {Wh}GLORY                {Gr}[{Ye}COMING SOON{Gr}]  {Wh}|
                    {Wh}|                                           {Wh}|
                   {Gr}----------------------------------------------- 
""")
banner()

def Manusia(name):
    user = input(f"\n   {Wh}[{Gr}+{Wh}] {Gr}Chose option game {Wh}:{Ye} ")
    Score = 0

    SOALNOOB = [
        {
            "soal":"A - C - R",
            "jawaban":"CAR"
        },
        { 
            "soal":"D - L - R - O - W",
            "jawaban":"WORLD"
        },
        { 
            "soal":"O - L - E - V",
            "jawaban":"LOVE"
        },
        { 
            "soal":"X - I - U - N - L",
            "jawaban":"LINUX"
        },
        { 
            "soal":"M - H - T - L",
            "jawaban":"HTML"
        },
        { 
            "soal":"C - S - S",
            "jawaban":"CSS"
        },
        { 
            "soal":"D - R - E",
            "jawaban":"RED"
        },
        { 
            "soal":"S - B - H - A",
            "jawaban":"BASH"
        },
        { 
            "soal":"Y - B - E - T",
            "jawaban":"BYTE"
        },
        { 
            "soal":"E - L - B - U",
            "jawaban":"BLUE"
        },
        { 
            "soal":"L - I - S - T",
            "jawaban":"LIST"
        },
        {
            "soal":"T - C - A",
            "jawaban":"CAT"
        },
        {
            "soal":"T - U - E - R",
            "jawaban":"TRUE"
        },
        {
            "soal":"L - F - E - S - A",
            "jawaban":"FALSE"
        },
        {
            "soal":"O - O - M - N",
            "jawaban":"MOON"
        },
        {
            "soal":"T - S - R - A - H ",
            "jawaban":"TRASH"
        },
        {
            "soal":"G - O - O - D",
            "jawaban":"GOOD"
        },
        {
            "soal":"Y - D - A",
            "jawaban":"DAY"
        },
        {
            "soal":"E - L - P - A - P",
            "jawaban":"APPLE"
        },
        {
            "soal":"T - M - I - S - E",
            "jawaban":"TIMES"
        }
    ]

    SOALMEDIUM = [
        {
            "soalM":"T - N - O - U - M - N - I ",
            "jawaban":"MOUNTIN"
        },
        { 
            "soalM":"N - D - C - A - E - B - R - A - L - A  ",
            "jawaban":"CANDELBARA"
        },
        { 
            "soalM":"S - T - U - R - A - U",
            "jawaban":"TAURUS"
        },
        { 
            "soalM":"W - O - L - O - L - F",
            "jawaban":"FOLLOW"
        },
        { 
            "soalM":"T - Q - B - U - O - E - U",
            "jawaban":"BOUQUET"
        },
        { 
            "soalM":"F - A - C - T - I - R - F - R",
            "jawaban":"AIRCRAFT"
        },
        { 
            "soalM":"E - A - K - L",
            "jawaban":"LAKE"
        },
        { 
            "soalM":"E - M - A - I - N",
            "jawaban":"ANIME"
        },
        { 
            "soalM":"M - G - I - I - N - E",
            "jawaban":"GEMINI"
        },
        { 
            "soalM":"Z - N - E - R - E - B - U - L - I",
            "jawaban":"NEBULIZER"
        },
        { 
            "soalM":"D - L -  N - O - I - M - A - N",
            "jawaban":"MANDOLIN"
        },
        {
            "soalM":"O - M - O - N - K - I",
            "jawaban":"KIMONO"
        },
        {
            "soalM":"H - T - E - L - P - E - N - A",
            "jawaban":"ELEPHANT"
        },
        {
            "soalM":"R - I - D - A - O - N - D",
            "jawaban":"ANDROID"
        },
        {
            "soalM":"S - D - O - W - I - N - W",
            "jawaban":"WINDOWS"
        },
        {
            "soalM":"K - W - T - E - N - O - R",
            "jawaban":"NETWORK"
        },
        {
            "soalM":"G - A - L - A - U - E - N - G ",
            "jawaban":"LANGUAGE"
        },
        {
            "soalM":"G - P - A - R - A - O - N",
            "jawaban":"PARAGON"
        },
        {
            "soalM":"T - P - U - R - O - M - C - E",
            "jawaban": "COMPUTER"
        },
        {
            "soalM":"N - O - M - H - P - M - N - E - E - O - N ",
            "jawaban":"PHENOMENON"
        }
    ]

    random.shuffle(SOALNOOB)
    if user == '1':
        os.system('clear')
        print()
        def animasi():    
            for i in range(10):
                sys.stdout.write(f'\r{Wh}LOADING YOUR LEVEL{Gr}  🙂')
                time.sleep(0.2)
                sys.stdout.write(f'\r{Wh}LOADING YOUR LEVEL{Gr}  😎')
                time.sleep(0.2)
                sys.stdout.write(f'\r{Wh}LOADING YOUR LEVEL{Gr}  🙂')
                time.sleep(0.2)
            sys.stdout.write(f'\r{Wh}LOADING YOUR LEVEL{Gr}  😎 ')
            time.sleep(0.2)
            os.system('clear')
        animasi()

        for i,soal in enumerate(SOALNOOB):
            print(f"""
    {Wh}LEVEL {Ye}{i+1} {Wh}| {Gr}NOOB
            
        {Ye}{"QUESTION"}:             
        {Gr}{soal["soal"]}           
            
    """)
            asw = input(f"{Wh}[{Gr}+{Wh}] {Ye}{name} {Wh}- {Gr}Answer {Wh}: {Ye}")
            if asw.upper() == soal["jawaban"]:
                print(f"{Wh}Good Job!")
                time.sleep(1)
                os.system('clear')
                Score += (5)
            else:
                print(f"{Re}Defeet!")
                time.sleep(1)
                os.system('clear')
        print(f"{Ye}{name}{Wh}, Your score: {Score}/10\n")

        pilih = input(f"\n{Wh}[{Gr}+{Wh}] {Gr}NEXT GAME {Ye}Y{Wh}/{Ye}N {Wh}:{Ye} ")
        if  pilih == 'Y'  or  pilih == 'y':
            banner()
            Manusia(name)
        elif pilih == 'N'  or  pilih == 'n':
            print(f"\n{Wh}[{Gr}+{Wh}] {Ye}CLOSE GAME...")
            time.sleep(1)
            sys.exit()
        else:
            print(f"\n{Wh}[{Gr}+{Wh}] {Ye}YOUR OPTION NOT FOUND")
        
        random.shuffle(SOALMEDIUM)
    elif  user == '2' :
        os.system('clear')
        print()
        def animasi():    
            for i in range(10):
                sys.stdout.write(f'\r{Wh}LOADING YOUR LEVEL{Gr}  🙂')
                time.sleep(0.2)
                sys.stdout.write(f'\r{Wh}LOADING YOUR LEVEL{Gr}  😎')
                time.sleep(0.2)
                sys.stdout.write(f'\r{Wh}LOADING YOUR LEVEL{Gr}  🙂')
                time.sleep(0.2)
            sys.stdout.write(f'\r{Wh}LOADING YOUR LEVEL{Gr}  😎 ')
            time.sleep(0.2)
            os.system('clear')
        animasi()

        for x,soalM in enumerate(SOALMEDIUM):
            print(f"""
    {Wh}LEVEL {Ye}{x+1} {Wh}| {Gr}MEDIUM
            
        {Ye}{"QUESTION"}:             
        {Gr}{soalM["soalM"]}           
            
    """)
            asw = input(f"{Wh}[{Gr}+{Wh}] {Ye}{name} {Wh}- {Gr}Answer {Wh}: {Ye}")
            if asw.upper() == soalM["jawaban"]:
                print(f"{Wh}Good Job!")
                time.sleep(1)
                os.system('clear')
                Score += (5)
            else:
                print(f"{Re}Defeet!")
                time.sleep(1)
                os.system('clear')
        print(f"{Ye}{name}{Wh}, Your score: {Score}/10\n")

        pilih = input(f"\n{Wh}[{Gr}+{Wh}] {Gr}NEXT GAME {Ye}Y{Wh}/{Ye}N {Wh}:{Ye} ")
        if  pilih == 'Y'  or  pilih == 'y':
            banner()
            Manusia(name)
        elif pilih == 'N'  or  pilih == 'n':
            print(f"\n{Wh}[{Gr}+{Wh}] {Ye}CLOSE GAME...")
            time.sleep(1)
            sys.exit()
        else:
            print(f"\n{Wh}[{Gr}+{Wh}] {Ye}YOUR OPTION NOT FOUND")
Manusia(name)

