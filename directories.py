import os
def find(path,dir):
    os.chdir(path)
    
    for i in os.listdir():
        print(i)
        if i == dir:
            print(os.getcwd())
            break
        else:
            print("No se encontró el directorio")
            if os.path.isdir(i):
                find(i,dir)
            
        

# path = input("Ingresa el path donde empieza la busqueda: ")
# dir = input("Ingresa el dir que se busca: ")
find("tree","python")

############################################################################################################

# import os

# class DirectorySearcher:
#     def find(self, path, dir):
#         try:
#             os.chdir(path)
#         except OSError:
#             # No procesa un archivo que no es un directorio.
#             return

#         current_dir = os.getcwd()
#         for entry in os.listdir("."):
#             if entry == dir:
#                 print(os.getcwd() + "/" + dir)
#             self.find(current_dir + "/" + entry, dir)


# directory_searcher = DirectorySearcher()
# directory_searcher.find("./tree", "python")