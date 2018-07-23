import sys
import webbrowser


def ver_horas():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(
        'file:///C:/Users/daniel.perez/Documents/HorasCLI/horas/Horas.md')


def nuevas_horas():
    nueva_fila = '\n|'
    for arg in sys.argv[2:]:
        nueva_fila += ' '+arg+' |'
    return nueva_fila


def anadir_fila(nueva_fila):
    with open('Horas.md', 'a') as file:
        file.write(nueva_fila)
    file.close()


def main():
    if len(sys.argv) > 1:
        if (sys.argv[1] in ['-h', '--help']):
            print("""
                    __  __                           ______ __     ____
                   / / / /____   _____ ____ _ _____ / ____// /    /  _/
                  / /_/ // __ \ / ___// __ `// ___// /    / /     / /  
                 / __  // /_/ // /   / /_/ /(__  )/ /___ / /___ _/ /   
                /_/ /_/ \____//_/    \__,_//____/ \____//_____//___/    
                                                       
                Usage: 
                horas -h | --help 'Shows this help'
                horas -s | --show 'Open the schedule in Chrome'
                horas -n | --new <project name> <hours> <date (xx-xx)> 'Add row to the schedule'
            """)
        elif (sys.argv[1] in ['-s', '--show']):
            ver_horas()
            return
        elif (sys.argv[1] in ['-n', '--new']):
            nueva_fila = nuevas_horas()
            anadir_fila(nueva_fila)
            return
    else:
        print("""
                    __  __                           ______ __     ____
                   / / / /____   _____ ____ _ _____ / ____// /    /  _/
                  / /_/ // __ \ / ___// __ `// ___// /    / /     / /  
                 / __  // /_/ // /   / /_/ /(__  )/ /___ / /___ _/ /   
                /_/ /_/ \____//_/    \__,_//____/ \____//_____//___/    
                                                       
                Usage: 
                horas -h | --help 'Shows this help'
                horas -s | --show 'Open the schedule in Chrome'
                horas -n | --new <project name> <hours> <date (xx-xx)> 'Add row to the schedule'
            """)


if __name__ == '__main__':
    main()
