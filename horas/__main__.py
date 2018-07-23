import sys
import webbrowser
import datetime
import os.path
from pathlib import Path

now = datetime.datetime.now()
help_msg = """
                    __  __                           ______ __     ____
                   / / / /____   _____ ____ _ _____ / ____// /    /  _/
                  / /_/ // __ \ / ___// __ `// ___// /    / /     / /  
                 / __  // /_/ // /   / /_/ /(__  )/ /___ / /___ _/ /   
                /_/ /_/ \____//_/    \__,_//____/ \____//_____//___/    

                Usage: 
                horas -h | --help 'Shows this help'
                horas -s | --show 'Open the schedule in Chrome'
                horas -n | --new <project name> <hours> 'Add row to the schedule with today date'
                horas -n | --new <project name> <hours> <date (dd-mm)> 'Add row to the schedule with the given date'
            """
chrome_error = """
                    __  __                           ______ __     ____
                   / / / /____   _____ ____ _ _____ / ____// /    /  _/
                  / /_/ // __ \ / ___// __ `// ___// /    / /     / /  
                 / __  // /_/ // /   / /_/ /(__  )/ /___ / /___ _/ /   
                /_/ /_/ \____//_/    \__,_//____/ \____//_____//___/    

                You need Google Chrome in order to show the schedule because it's a Markdown file.
                Install extension Markdown Reader to get the best visualization.
            """
home = str(Path.home())
schedule_file = home+'/projectsSchedule.md'
schedule_file_path = Path(schedule_file)


def ver_horas():
    chrome_path = Path("C:/Program Files (x86)/Google/Chrome/Application")
    if chrome_path.is_dir():
        chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome).open(
            'file:///'+schedule_file)
    else:
        print(chrome_error)


def nuevas_horas():
    nueva_fila = '\n|'
    for arg in sys.argv[2:]:
        nueva_fila += ' '+arg+' |'
    if(len(sys.argv) == 4):
        nueva_fila += ' '+now.strftime("%d-%m")+' |'
    return nueva_fila


def anadir_fila(nueva_fila):
    with open(schedule_file, 'a') as file:
        file.write(nueva_fila)
    file.close()


def check_file():
    if os.path.exists(schedule_file):
        return True
    else:
        with open(schedule_file, 'a+', encoding='UTF-8') as file:
            file.write('| Proyecto | Horas |   Dia |\n')
            file.write('|----------|:-----:|------:|')
        file.close()
        main()


def main():
    if(check_file()):
        if len(sys.argv) > 1:
            if (sys.argv[1] in ['-h', '--help']):
                print(help_msg)
            elif (sys.argv[1] in ['-s', '--show']):
                ver_horas()
                return
            elif (sys.argv[1] in ['-n', '--new']):
                nueva_fila = nuevas_horas()
                anadir_fila(nueva_fila)
                return
        else:
            print(help_msg)


if __name__ == '__main__':
    main()
