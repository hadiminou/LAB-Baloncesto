from baloncesto import*

def test_lee_partidos(partidos:list[PartidoBasket]):
    print("numero de registros leidos:", len(partidos))
    print("\nlos tres primeros son: ", partidos[:3])

def test_equipo_con_mas_faltas(partidos:list[PartidoBasket]):
    print("\ntest_equipo_con_mas_faltas")
    print(equipo_con_mas_faltas(partidos))

def test_victorias_por_equipo(partidos:list[PartidoBasket]):
    print("\ntest_victorias_por_equipo")
    print(victorias_por_equipo(partidos))

if __name__=="__main__":
    datos = lee_partidos("LAB-Baloncesto\data/resultados_baloncesto.csv")
    test_lee_partidos(datos)
    test_equipo_con_mas_faltas(datos)
    test_victorias_por_equipo(datos)