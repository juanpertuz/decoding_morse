def codificar(mensaje):
    """
    Programa que codifica o convierte a código morse una palabra o un mensaje.
    :param mensaje: palabra o frase a convertir en código morse.
    :return: mensaje codificado (convertido) a morse, separando cada letra por punto y coma (;).
    """
    msj_morse = ''
    dict_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..'}
    for letra in mensaje:
        if letra.upper() in dict_morse:
            msj_morse += (dict_morse[letra.upper()]) + ';'
        else:
            msj_morse += ' ;'
    print(msj_morse)


def decodificar(mensaje_morse):
    """
    Función que recibe una palabra u oración en código morse y la convierte a texto.
    :param mensaje_morse: Palabra u oración en código morse separada por (;) y espacios
    :return: mensaje en texto con letra mayúscula.
    """
    msj_morse = mensaje_morse.split(';')
    mensaje = ''
    dict_morse_r = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                    '-.--': 'Y', '--..': 'Z'}
    for simbol in msj_morse:
        if simbol in dict_morse_r:
            mensaje += dict_morse_r[simbol]
        else:
            mensaje += ' '
    print(mensaje)


codificar('el edificio esta en llamas')
decodificar('.;.-..; ;.;-..;..;..-.;..;-.-.;..;---; ;.;...;-;.-; ;.;-.; ;.-..;.-..;.-;--;.-;...;')
