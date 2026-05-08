# ex4.py
# Mohamed Boyauzan - Zakaria el Bourkkisi

import sys

# Mostrar ayuda
def mostrar_ayuda():
    print("USO: python ex4.py file [c] [-i -p -f] [--help]")
    print("")
    print("Arguments:")
    print(" file       : Nombre del archivo de texto a leer")
    print(" c          : Carácter a buscar en las líneas (opcional)")
    print(" -i         : Contar líneas que NO contienen el carácter c")
    print(" -p         : Contar líneas que empiezan por el carácter c")
    print(" -f         : Guardar el resultado en sortida.txt")
    print(" --help     : Mostrar esta ayuda")
    print("")
    print("Ejemplos:")
    print(" python ex4.py texto.txt")
    print(" python ex4.py texto.txt a")
    print(" python ex4.py texto.txt a -i")
    print(" python ex4.py texto.txt a -p")
    print(" python ex4.py texto.txt a -p -f")

# Contar lineas según opciones
def contar_lineas(nombre, c=None, invertir=False, empezar=False):
    contador = 0
    f = None
    try:
        f = open(nombre, "r")
        lineas = f.readlines()
        i = 0
        while i < len(lineas):
            linea = lineas[i].rstrip("\n")  # quitar salto de linea
            if c is None:
                contador = contador + 1
            else:
                if empezar:
                    # empezar por c
                    if len(linea) > 0:
                        if invertir:
                            if linea[0] != c:
                                contador = contador + 1
                        else:
                            if linea[0] == c:
                                contador = contador + 1
                else:
                    # contiene c
                    if invertir:
                        if c not in linea:
                            contador = contador + 1
                    else:
                        if c in linea:
                            contador = contador + 1
            i = i + 1
    except IOError:
        print("Error: el archivo no existe.")
        return None
    finally:
        if f:
            f.close()
    return contador

# PROGRAMA PRINCIPAL
def main():
    if len(sys.argv) == 1:
        print("Error: no se han proporcionado argumentos. Usa --help para ayuda.")
        return

    if sys.argv[1] == "--help":
        mostrar_ayuda()
        return

    nombre = sys.argv[1]
    c = None
    invertir = False
    empezar = False
    guardar_fichero = False

    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "-i":
            invertir = True
        elif arg == "-p":
            empezar = True
        elif arg == "-f":
            guardar_fichero = True
        else:
            if c is None:
                c = arg
            else:
                print("Error: argumento desconocido o mal colocado.")
                mostrar_ayuda()
                return
        i = i + 1

    if (invertir or empezar) and c is None:
        print("Error: -i o -p requieren especificar el caracter c.")
        mostrar_ayuda()
        return

    resultado = contar_lineas(nombre, c, invertir, empezar)
    if resultado is None:
        return

    mensaje = "Lineas contadas: " + str(resultado)

    if guardar_fichero:
        f = None
        try:
            f = open("sortida.txt", "w")
            f.write(mensaje + "\n")
            print("Resultado guardado en sortida.txt")
        except:
            print("Error al guardar el archivo")
        finally:
            if f:
                f.close()
    else:
        print(mensaje)

main()
