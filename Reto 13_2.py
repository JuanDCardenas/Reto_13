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