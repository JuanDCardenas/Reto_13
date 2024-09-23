# Reto_13
### 1) Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
```python
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

````
### 2) Desarrollar una funcion que reciba dos diccionarios como parametros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.
```python
def union_diciconarios (dicc_1:dict, dicc_2:dict)->dict:
    dicc_2.update(dicc_1)
    return dicc_2
if __name__=="__main__":
    dicc_1= {
    1: "Auto",
    2: "Bicicleta",
    3: "Avion",
    }
    dicc_2 = {
    2: "Barco", 
    3: "Tren",   
    4: "Motocicleta",
    }
    unido=union_diciconarios(dicc_1,dicc_2)
    print(unido)
````
