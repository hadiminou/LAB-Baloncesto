from collections import defaultdict
from typing import*
from datetime import datetime, date
import csv

Equipo = NamedTuple("Equipo",[("nombre", str),("puntos", int),("faltas", int)])

PartidoBasket = NamedTuple("PartidoBasket",[("fecha", date), ("competicion", str), ("equipo1", Equipo),\
                                            ("equipo2", Equipo)])

def parsea_y_suma_resultados(cadena:str)->Tuple[int, int]:
    suma1=0
    suma2=0
    for elem in cadena.split("*"):
        suma1+=int(elem.split("-")[0])
        suma2+=int(elem.split("-")[1])
    return (suma1, suma2)
        
def lee_partidos(ruta_fichero:str)->List[PartidoBasket]:
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

def equipo_con_mas_faltas(partidos:List[PartidoBasket], equipos:Set=None)->Tuple[PartidoBasket]:
    aux = defaultdict(int)
    for i in partidos:
        if equipos == None or i.equipo1 in equipos:
            aux[i.equipo1.nombre]+=(i.equipo1.faltas)
        if equipos == None or i.equipo2 in equipos:
            aux[i.equipo2.nombre]+=(i.equipo2.faltas)
    return max(aux.items(), key = lambda e:e[1])

def media_puntos_por_equipo(partidos:List[PartidoBasket], competicion:str)->Dict[str,float]:
    res = defaultdict(list)
    for i in partidos:
        if i.competicion == competicion:
            res[i.equipo1.nombre].append(i.equipo1.puntos)
            res[i.equipo2.nombre].append(i.equipo2.puntos)
    return {c: sum(v)/len(v) for c,v in res.items()}

def diferencia_puntos_anotados(partidos:List[PartidoBasket], equipo:str)->List[int]:
    res = []
    for i in partidos:
        if i.equipo1.nombre == equipo:
            res.append((i.fecha, i.equipo1.puntos))
        elif i.equipo2.nombre == equipo:
            res.append((i.fecha, i.equipo2.puntos))
    res = sorted(res)
    return [tupla2[1] - tupla1[1] for tupla1, tupla2 in zip(res,res[1:])]

def victorias_por_equipo(partidos:List[PartidoBasket])->Dict[str,int]:
    res = defaultdict(int)
    for i in partidos:
        if i.equipo1.puntos > i.equipo2.puntos:
            res[i.equipo1.nombre]+=1
        elif i.equipo1.puntos < i.equipo2.puntos:
            res[i.equipo2.nombre]+=1
    return sorted(res.items(), key= lambda e:e[1], reverse = True)

def equipos_minimo_victorias(partidos:List[PartidoBasket], n:int)->List[str]:
    return [i[0] for i in victorias_por_equipo(partidos) if i[1] >= n]

def equipos_mas_victorias_por_ano(partidos:List[PartidoBasket], n:int)->Dict[date.year, List[str]]:
    res = defaultdict(list)
    for i in partidos:
        res[i.fecha.year].append(i)
    return {c: equipos_minimo_victorias(v, n) for c,v in res.items()}