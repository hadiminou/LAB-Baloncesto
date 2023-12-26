from baloncesto import*

def test_lee_partidos(partidos:List[PartidoBasket]):
    print("numero de registros leidos:", len(partidos))
    print("\nlos tres primeros son: ", partidos[:3])

def test_equipo_con_mas_faltas(partidos:List[PartidoBasket]):
    print("\ntest_equipo_con_mas_faltas")
    print(equipo_con_mas_faltas(partidos))

def test_media_puntos_por_equipo(partidos:List[PartidoBasket]):
    print("\ntest_media_puntos_por_equipo")
    print(media_puntos_por_equipo(partidos, competicion="Copa del Rey"))

def test_diferencia_puntos_anotados(Partidos:List[PartidoBasket]):
    print("\ntest_diferencia_puntos_anotados")
    print(diferencia_puntos_anotados(Partidos, equipo = 'Barcelona'))

def test_victorias_por_equipo(partidos:List[PartidoBasket]):
    print("\ntest_victorias_por_equipo")
    print(victorias_por_equipo(partidos))

def test_equipos_minimo_victorias(partidos:List[PartidoBasket]):
    print("\ntest_equipos_minimo_victorias")
    print(equipos_minimo_victorias(partidos, n = 8))

def test_equipos_mas_victorias_por_ano(partidos:List[PartidoBasket]):
    print("\ntest_equipos_mas_victorias_por_ano")
    print(equipos_mas_victorias_por_ano(partidos, n = 8))

if __name__=="__main__":
    datos = lee_partidos("data/resultados_baloncesto.csv")
    test_lee_partidos(datos)
    test_equipo_con_mas_faltas(datos)
    test_media_puntos_por_equipo(datos)
    test_diferencia_puntos_anotados(datos)
    test_victorias_por_equipo(datos)
    test_equipos_minimo_victorias(datos)
    test_equipos_mas_victorias_por_ano(datos)