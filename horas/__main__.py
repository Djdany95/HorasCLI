# -*- coding: utf-8 -*-

import sys
import webbrowser
import datetime
import os.path
from pathlib import Path
from utils import get_OS, get_errors

now = datetime.datetime.now()
home = str(Path.home())
schedule_file = home+'/projectsSchedule.md'


def show_horas():
    chrome_path = Path(get_OS().get('chrome'))
    try:
        chrome_path.is_dir()
        chrome = get_OS().get('chrome')
        webbrowser.get(chrome).open(
            'file:///'+schedule_file)
    except:
        print(get_errors().get('chrome_error'))
        with open(schedule_file, 'r') as file:
            lines = file.readlines()
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
        if("es" in get_OS().get('lang')):
            file.write('## Registro de Proyectos  \n\n')
            file.write('| Proyecto | Horas |   Dia  |\n')
            file.write('|----------|:-----:|:------:|\n')
        else:
            file.write('## Project Schedule  \n\n')
            file.write('| Project | Hours |   Day  |\n')
            file.write('|---------|:-----:|:------:|\n')
        file.close()


def delete_last_line():
    with open(schedule_file, 'r') as file:
        lines = file.readlines()
        file.close()

    lines = lines[0:len(lines)-1]
    print(lines)
    with open(schedule_file, 'w') as file:
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
                print(get_errors().get('help_msg'))
            elif (sys.argv[1] in ['-s', '--show']):
                show_horas()
            elif (sys.argv[1] in ['-r', '--reset']):
                reset_horas()
            elif (sys.argv[1] in ['-n', '--new']):
                new_horas()
            elif (sys.argv[1] in ['-d', '--delete']):
                delete_last_line()
            else:
                print(get_errors().get('command_error'))
        else:
            print(get_errors().get('command_error'))


if __name__ == '__main__':
    main()
