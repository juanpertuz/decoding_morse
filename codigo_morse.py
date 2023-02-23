def codificar(mensaje):
    msj = mensaje.upper()
    msj_morse = []
    dict_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..'}
    for letra in msj:
        if letra in dict_morse:
            msj_morse.append(dict_morse[letra])
        else:
            msj_morse.append('  ')
    print(';'.join(msj_morse))


def decodificar(mensaje_morse):
    msj_morse = list(mensaje_morse.split(';'))
    mensaje = []
    dict_morse_r = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                    '-.--': 'Y', '--..': 'Z'}
    for simbol in msj_morse:
        if simbol in dict_morse_r:
            mensaje.append(dict_morse_r[simbol])
        else:
            mensaje.append('')
    msj_final = str(''.join(mensaje))
    print(msj_final)


codificar('telefono')
decodificar('-;.;.-..;.;..-.;---;-.;---')
