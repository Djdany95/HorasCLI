import sys
import webbrowser


def ver_horas():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open('file:///C:/Users/daniel.perez/Documents/HorasCLI/horas/Horas.md')


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
        if (sys.argv[1] in ['-m', '--mostrar']):
            ver_horas()
            return
        elif (sys.argv[1] in ['-n', '--nueva']):
            nueva_fila = nuevas_horas()
            anadir_fila(nueva_fila)
            return
    else:
        print("Formato incorrecto prueba lo siguiente:")
        print("horas -m")
        print("horas -n nombre horas fecha(xx-xx)")

if __name__ == '__main__':
    main()
