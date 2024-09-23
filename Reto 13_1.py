def valores_diccionario(dic_1:dict)->list:
    valores=list(dic_1.values())
    valores.sort()
    return valores
if __name__=="__main__":
    dict_1 = {
    "matematica": 85,
    "español": 90,
    "ciencias": 78,
    "historia": 88
    }
    ordenados=valores_diccionario(dict_1)
    print(ordenados)
