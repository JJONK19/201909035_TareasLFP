
def automata(cad):
    e= 0

    for i in range(len(cad)):
        if e == 0:
            if cad[i] == '_':
                e = 1
            elif cad[i].lower() == 'a' or cad[i].lower() == 'b' or cad[i].lower() == 'c' or cad[i].lower() == 'd' or cad[i].lower() == 'e' or cad[i].lower() == 'f' or cad[i].lower() == 'g' or cad[i].lower() == 'h' or cad[i].lower() == 'i' or cad[i].lower() == 'j' or cad[i].lower() == 'k' or cad[i].lower() == 'l' or cad[i].lower() == 'm' or cad[i].lower() == 'n' or cad[i].lower() == 'ñ' or cad[i].lower() == 'o' or cad[i].lower() == 'p' or cad[i].lower() == 'q' or cad[i].lower() == 'r' or cad[i].lower() == 's' or cad[i].lower() == 't' or cad[i].lower() == 'u' or cad[i].lower() == 'v' or cad[i].lower() == 'w' or cad[i].lower() == 'y' or cad[i].lower() == 'z':
                e = 2
            else:
                print('Cadena no valida')
                return
        elif e == 1:
            if cad[i].lower() == 'a' or cad[i].lower() == 'b' or cad[i].lower() == 'c' or cad[i].lower() == 'd' or cad[i].lower() == 'e' or cad[i].lower() == 'f' or cad[i].lower() == 'g' or cad[i].lower() == 'h' or cad[i].lower() == 'i' or cad[i].lower() == 'j' or cad[i].lower() == 'k' or cad[i].lower() == 'l' or cad[i].lower() == 'm' or cad[i].lower() == 'n' or cad[i].lower() == 'ñ' or cad[i].lower() == 'o' or cad[i].lower() == 'p' or cad[i].lower() == 'q' or cad[i].lower() == 'r' or cad[i].lower() == 's' or cad[i].lower() == 't' or cad[i].lower() == 'u' or cad[i].lower() == 'v' or cad[i].lower() == 'w' or cad[i].lower() == 'y' or cad[i].lower() == 'z':
                e = 3
            elif cad[i] == '_':
                e = 1
            else:
                print('Cadena no valida')
                return
        elif e == 2:
            if cad[i] == '1' or cad[i] == '2' or cad[i] == '3' or cad[i] == '4' or cad[i] == '5' or cad[i] == '6' or cad[i] == '7' or cad[i] == '8' or cad[i] == '9' or cad[i] == '0':
                e = 4
            elif cad[i].lower() == 'a' or cad[i].lower() == 'b' or cad[i].lower() == 'c' or cad[i].lower() == 'd' or cad[i].lower() == 'e' or cad[i].lower() == 'f' or cad[i].lower() == 'g' or cad[i].lower() == 'h' or cad[i].lower() == 'i' or cad[i].lower() == 'j' or cad[i].lower() == 'k' or cad[i].lower() == 'l' or cad[i].lower() == 'm' or cad[i].lower() == 'n' or cad[i].lower() == 'ñ' or cad[i].lower() == 'o' or cad[i].lower() == 'p' or cad[i].lower() == 'q' or cad[i].lower() == 'r' or cad[i].lower() == 's' or cad[i].lower() == 't' or cad[i].lower() == 'u' or cad[i].lower() == 'v' or cad[i].lower() == 'w' or cad[i].lower() == 'y' or cad[i].lower() == 'z':
                e = 2
            else:
                print('Cadena no valida')
                return
        elif e == 3:
            if cad[i] == '1' or cad[i] == '2' or cad[i] == '3' or cad[i] == '4' or cad[i] == '5' or cad[i] == '6' or cad[i] == '7' or cad[i] == '8' or cad[i] == '9' or cad[i] == '0':
                e = 4
            else:
                print('Cadena no valida')
                return
    print("Cadena Valida")

automata("_servidor1")
automata("3servidor")