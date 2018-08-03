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
                horas -s | --show 'Opens the schedule in Chrome if exists or as command line'
                horas -r | --reset 'Resets the schedule file'
                horas -n | --new <project name> <hours> 'Adds row to the schedule with today date'
                horas -n | --new <project name> <hours> <date (dd-mm)> 'Adds row to the schedule with the given date'
                horas -d | --delete 'Deletes the last hour added'
            """
command_error = """
                    __  __                           ______ __     ____
                   / / / /____   _____ ____ _ _____ / ____// /    /  _/
                  / /_/ // __ \ / ___// __ `// ___// /    / /     / /
                 / __  // /_/ // /   / /_/ /(__  )/ /___ / /___ _/ /
                /_/ /_/ \____//_/    \__,_//____/ \____//_____//___/

                Error: Command not found or invalid.
                Try horas -h | --help 'Shows help'
            """
chrome_error = """
                    __  __                           ______ __     ____
                   / / / /____   _____ ____ _ _____ / ____// /    /  _/
                  / /_/ // __ \ / ___// __ `// ___// /    / /     / /
                 / __  // /_/ // /   / /_/ /(__  )/ /___ / /___ _/ /
                /_/ /_/ \____//_/    \__,_//____/ \____//_____//___/

                Install Chrome and Markdown Reader extension to get the best visualization.
            """
home = str(Path.home())
schedule_file = home+'/projectsSchedule.md'
schedule_file_path = Path(schedule_file)


def show_horas():
    chrome_path = Path(":/Program Files (x86)/Google/Chrome/Application")
    try:
        chrome_path.is_dir()
        chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome).open(
            'file:///'+schedule_file)
    except:
        print(chrome_error)
        with open(schedule_file, 'r') as file:
            lines=file.readlines()
            for line in lines:
                print(line)
            file.close()


def new_horas():
    nueva_fila = '|'
    for arg in sys.argv[2:]:
        nueva_fila += ' '+arg+' |'
    if(len(sys.argv) == 4):
        nueva_fila += ' '+now.strftime("%d-%m")+' |\n'

    with open(schedule_file, 'a') as file:
        file.write(nueva_fila)
        file.close()


def reset_horas():
    with open(schedule_file, 'w', encoding='UTF-8') as file:
        file.write('| Proyecto | Horas |   Dia  |\n')
        file.write('|----------|:-----:|:------:|\n')
        file.close()

def delete_last_line():
    with open(schedule_file, 'r') as file:
        lines = file.readlines()
        file.close()

    lines=lines[0:len(lines)-1]
    print(lines)
    with open (schedule_file, 'w') as file:
        for line in lines:
            file.write(line)
        file.close()


def check_horas_file():
    if os.path.exists(schedule_file):
        return True
    else:
        reset_horas()
        main()


def main():
    if(check_horas_file()):
        if len(sys.argv) > 1:
            if (sys.argv[1] in ['-h', '--help']):
                print(help_msg)
            elif (sys.argv[1] in ['-s', '--show']):
                show_horas()
            elif (sys.argv[1] in ['-r', '--reset']):
                reset_horas()
            elif (sys.argv[1] in ['-n', '--new']):
                new_horas()
            elif (sys.argv[1] in ['-d', '--delete']):
                delete_last_line()
            else:
                print(command_error)
        else:
            print(command_error)


if __name__ == '__main__':
    main()
