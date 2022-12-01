import pprint as pp
class StudentsDataException(Exception):
    pass

class WrongLine(StudentsDataException):
    pass

class FileEmpty(StudentsDataException):
    pass

try:
    notes = open("notes.txt", "r")
    lines = notes.readlines()
    if len(lines) == 0:
        raise FileEmpty
    lista = []
    for line in lines:
        if len(line.split("\t")) != 3:
            raise WrongLine
        lista.append(line.split("\t")) 
    result = {}
    for i in lista:
        aux = i[2].strip() #strip() removes the newline character
        if i[0] + " " + i[1] not in result:
            result[i[0] + " " + i[1]] = float(aux)
        else:
            result[i[0] + " " + i[1]] =  float(result[i[0] + " " + i[1]]) + float(aux)
    pp.pprint(result)
    notes.close()   

    streamWrite = open("resultados.hist", "wt")
    for key in result:
        streamWrite.write(key + " -> " + str(result[key]) + "\n")
    streamWrite.close()

except StudentsDataException as e:
    print("Error: ", e)
except WrongLine as e:
    print("Wrong line")
    
except FileEmpty as e:
    print("El archivo está vacío")
    
