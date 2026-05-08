# Funcio per demanar un numero enter segur
import doctest
doctest.testmod()


def introduir_int_segur(missatge, minim=None, maxim=None):
    """
    Demana un numero enter a l'usuari fins que sigui valid i dins del rang si s'especifica.
    
    Parametres:
        missatge (str): text que es mostra per demanar el numero.
        minim (int): valor minim permes (opcional).
        maxim (int): valor maxim permes (opcional).
    
    Retorna:
        int: el numero enter introduit.

    NOTA: No es pot fer Doctest perque usa input().
    """
    ok = False
    while not ok:
        entrada = input(missatge)
        if entrada.isdigit():
            valor = int(entrada)
            if (minim is None or valor >= minim) and (maxim is None or valor <= maxim):
                ok = True
            else:
                print(f"El numero ha d'estar entre {minim} i {maxim}. Torna-ho a intentar.")
        else:
            print("Entrada no valida. Torna-ho a intentar.")
    return valor


# Funcio per comptar majuscules i minuscules
# Funcio per comptar majuscules i minuscules
def comptar_majuscules_minuscules(cadena):
    """
    Compta majuscules i minuscules d'una cadena.

    Parametres:
        cadena (str): text a analitzar.

    Retorna:
        tuple: (num_majuscules, num_minuscules)

    >>> comptar_majuscules_minuscules("Hola")
    (2, 3)   # ERROR a proposito
    >>> comptar_majuscules_minuscules("Python3")
    (1, 5)
    >>> comptar_majuscules_minuscules("")
    (0, 0)
    """
    majuscules = 0
    minuscules = 0
    for lletra in cadena:
        if lletra.isupper():
            majuscules += 1
        elif lletra.islower():
            minuscules += 1
    return majuscules, minuscules


# Funcio per calcular si un any es de traspas
def calcular_any_traspas(any):
    """
    Comprova si un any es de traspas.
    
    Parametres:
        any (int): any a comprovar.
    
    Retorna:
        bool: True si es de traspas, False si no.
    
    >>> calcular_any_traspas(2020)
    True
    >>> calcular_any_traspas(1900)
    False
    >>> calcular_any_traspas(2000)
    True
    >>> calcular_any_traspas(2023)
    False
    """
    if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
        return True
    else:
        return False


# Funcio per comptar dies d'un mes
def comptar_dies_mes(mes, any):
    """
    Retorna el nombre de dies d'un mes concret.
    
    Parametres:
        mes (int): numero del mes (1-12).
        any (int): any a considerar.
    
    Retorna:
        int: nombre de dies del mes.
    
    >>> comptar_dies_mes(1, 2023)
    31
    >>> comptar_dies_mes(2, 2020)
    29
    >>> comptar_dies_mes(2, 2021)
    28
    >>> comptar_dies_mes(4, 2022)
    30
    """
    dies_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
    if mes == 2:
        if calcular_any_traspas(any):
            return 29
        else:
            return 28
    return dies_mes[mes - 1]


# Funcio per comprovar si un numero es perfecte
def comprovar_num_perfecte(numero):
    """
    Comprova si un numero es perfecte.
    
    Parametres:
        numero (int): numero a comprovar.
    
    Retorna:
        bool: True si es perfecte, False si no.
    
    >>> comprovar_num_perfecte(6)
    True
    >>> comprovar_num_perfecte(28)
    True
    >>> comprovar_num_perfecte(12)
    False
    >>> comprovar_num_perfecte(1)
    False
    """
    suma_divisors = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisors += i
    if suma_divisors == numero:
        return True
    else:
        return False


# Funcio per mostrar el menu
def mostrar_menu(opcio):
    """
    Mostra el menu d'opcions.
    
    Parametres:
        opcio (int): valor no usat, es manté per compatibilitat.
    
    Retorna:
        None
    """
    print("\n--- MENU ---")
    print("1. Introduir un numero enter segur")
    print("2. Comptar majuscules i minuscules en una cadena")
    print("3. Comprovar si un any es de traspas")
    print("4. Comptar els dies d'un mes")
    print("5. Comprovar si un numero es perfecte")
    print("0. Sortir")


# Funcio principal
def main():
    """
    Executa el programa principal amb el menu i les opcions.
    
    Retorna:
        None
    """
    validar = False
    opcio = -1
    while not validar:
        mostrar_menu(opcio)
        opcio = int(input("introduce una una opcion : "))

        if opcio == 1:
            edat = introduir_int_segur("Introdueix la teva edat: ", 18, 120)
            print(f"La teva edat es {edat}")
        elif opcio == 2:
            cadena = input("Introdueix una cadena: ")
            maj, minusc = comptar_majuscules_minuscules(cadena)
            print(f"Majuscules: {maj}, Minuscules: {minusc}")
        elif opcio == 3:
            any = introduir_int_segur("Introdueix un any: ")
            if calcular_any_traspas(any):
                print(f"{any} es un any de traspas")
            else:
                print(f"{any} no es un any de traspas")
        elif opcio == 4:
            mes = introduir_int_segur("Introdueix el numero del mes (1-12): ")
            any = introduir_int_segur("Introdueix un any: ")
            dies = comptar_dies_mes(mes, any)
            print(f"El mes {mes} de l'any {any} te {dies} dies")
        elif opcio == 5:
            numero = introduir_int_segur("Introdueix un numero per comprovar si es perfecte: ")
            if comprovar_num_perfecte(numero):
                print(f"{numero} es un numero perfecte")
            else:
                print(f"{numero} no es un numero perfecte")
        elif opcio == 0:
            print("Fins aviat!")
            validar = True
        else:
            print("Opcio no valida. Torna a intentar")


# Executem doctest i el programa principal
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
