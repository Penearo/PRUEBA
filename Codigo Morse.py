#Definimos el primer diccionario de letra a morse
def letra_a_morse(letra):
    morse_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
        'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
        'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..'
    }
    return morse_dict.get(letra.lower(), '')
#Aqui definimos el diccionario de codigo morse a letra para poder crear las plabras
def morse_a_letra(morse):
    morse_dict = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd',
        '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h',
        '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l'}
    return morse_dict.get(morse, '')
#Aqui vamos a definir nuestra tabla que vamos a mostrar despues usando los dos diccionarios ya antes usados
def mostrar_tabla():
    print("Letra  Código Morse")
    for letra in 'abcdefghijkl':
        print(f"  {letra} = {letra_a_morse(letra)}")
#Vamos a crear las palabras que queremos que se muestren en pantalla
def crear_palabras():
    palabras = ['hola', 'caja', 'gafa']
    for palabra in palabras:
        morse = ' '.join(letra_a_morse(letra) for letra in palabra)
        print(f"{palabra} > {morse}")

# Tabla
mostrar_tabla()
print("Palabras en Morse:")
crear_palabras()
