from collections import defaultdict
from typing import*
from datetime import datetime, date
import csv

Equipo = NamedTuple("Equipo",[("nombre", str),("puntos", int),("faltas", int)])

PartidoBasket = NamedTuple("PartidoBasket",[("fecha", date), ("competicion", str), ("equipo1", Equipo), ("equipo2", Equipo)])

def parsea_y_suma_resultados(cadena:str)->tuple[int, int]:
    suma1=0
    suma2=0
    for elem in cadena.split("*"):
        suma1+=int(elem.split("-")[0])
        suma2+=int(elem.split("-")[1])
    return (suma1, suma2)
        
def lee_partidos(ruta_fichero:str)->list[PartidoBasket]:
    res = []
    with open (ruta_fichero, "rt", encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        for fecha,equipo1,equipo2,competicion,cuartos,faltas1,faltas2 in lector:
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            faltas1 = int(faltas1)
            faltas2 = int(faltas2)
            equipo1=(Equipo(equipo1, parsea_y_suma_resultados(cuartos)[0],faltas1))
            equipo2=(Equipo(equipo2, parsea_y_suma_resultados(cuartos)[1],faltas2))
            res.append(PartidoBasket(fecha, competicion, equipo1, equipo2))
    return res

def equipo_con_mas_faltas(partidos:list[PartidoBasket], equipos:set=None)->tuple:
    aux = defaultdict(int)
    for i in partidos:
        if equipos == None or i.equipo1 in equipos:
            aux[i.equipo1.nombre]+=(i.equipo1.faltas)
        if equipos == None or i.equipo2 in equipos:
            aux[i.equipo2.nombre]+=(i.equipo2.faltas)
    return max(aux.items(), key = lambda e:e[1])

#def media_puntos_por_equipo(patidos:list[PartidoBasket], competicion:str)->dict[str,float]

def victorias_por_equipo(partidos:list[PartidoBasket])->dict[str,int]:
    res = defaultdict(int)
    for i in partidos:
        if i.equipo1.puntos > i.equipo2.puntos:
            res[i.equipo1.nombre]+=1
        elif i.equipo1.puntos < i.equipo2.puntos:
            res[i.equipo2.nombre]+=1
    return sorted(res.items(), key= lambda e:e[1], reverse = True)

