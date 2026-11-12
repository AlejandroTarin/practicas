from Vehiculo import Vehiculo

from urllib.parse import parse_qs

def contenido(environ)->str:
    #leer cuerpo
    longitud= int (environ.get("CONTENT_LENGTH","0")or "0")
    #post
    cuerpo = environ.get("wgsi.input")
    query=cuerpo.decode("utf-8")
    #parsear para conseguir diccionario
    parametros=parse_qs(query)
    # obtener datos necesarios del diccionario
    direccion: str=parametros.get("direccion",[""])[0]
    tipoIntervencion
    numeroBomberos
    mostrarNoAptos : bool = "mostrasrNoAptos" in parametros

    #checkbox

    listaVehiculos: list[Vehiculo]=[]
    listaVehiculosAptos: list[Vehiculo]=[]
    listaVehiculosNoAptos: list[Vehiculo]=[]


    listaVehiculos.append(Vehiculo("B03","Bomba",6,False))




    html: str=f"""
    <h2>Datos de la solicitud</h2>
    <h2>Ubicacion: {direccion}</h2>
    <h2>Tipo intervencion: {tipoIntervencion}
    """