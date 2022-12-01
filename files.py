from os import strerror

try:
    alphabet = {chr(ch): 0 for ch in range(ord('A'), ord('z') + 1)}
    texto = input("Introduce el nombre del texto: ")
    character_counter = line_counter = 0
    stream = open(texto, 'rt')
    lines = stream.readlines(20)
    while len(lines) != 0:
        for line in lines:
            line_counter += 1
            for char in line:
                if char in alphabet and char.isalpha():
                    alphabet[char] += 1
                character_counter += 1
        lines = stream.readlines(10)
    stream.close()
    print("\n\nCaracteres en el archivo:", character_counter)
    print("Líneas en el archivo:     ", line_counter)
    alphabet = dict(sorted(alphabet.items(), key=lambda x: x[1], reverse=True))
    for key in alphabet:
        print(key, "->", alphabet[key])

    streamWrite = open("resultados.hist", "wt")
    for key in alphabet:
        streamWrite.write(key + " -> " + str(alphabet[key]) + "\n")
    streamWrite.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno)) 
