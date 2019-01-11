import re

def cleanLugar(string):
  """
  i.e: " Valle del  Cauca : Cali"
      => {'departamento': "valle del cauca", "ciudad": "cali"}
  """
  split_str = string.split(":")
  if len(split_str)>1:
    departamento = split_str[0]
    ciudad = split_str[1]

  if len(split_str)==1:
    departamento = split_str[0]
    ciudad = split_str[0]

  departamento = cleanStr(departamento)
  ciudad = cleanStr(ciudad)
  # lugar = {"departamento": departamento, "ciudad": ciudad}
  lugar = departamento + ', ' + ciudad
  return lugar

def cleanStr(string):
  return string.strip().lower()

def cleanPrecio(precio):
  """
  i.e: "$10,000,123 pesos"
      => "10000123"
  """
  return int(re.findall('\d+', precio.strip().replace("$","").replace(",", ""))[0])

def cleanFecha(fecha):
  """
   i.e 13 de March de 2012
   => {'dia': 13, 'mes':3, 'anio':2012}
  """

  months_map = {
      "enero":"01",
      "febrero":"02",
      "marzo":"03",
      "abril":"04",
      "mayo":"05",
      "junio":"06",
      "julio":"07",
      "agosto":"08",
      "septiembre":"09",
      "octubre":"10",
      "noviembre":"11",
      "diciembre":"12",
      "january":"01",
      "february":"02",
      "march":"03",
      "april":"04",
      "may":"05",
      "june":"06",
      "july":"07",
      "august":"08",
      "september":"09",
      "october":"10",
      "november":"11",
      "december":"12"
  }

  fecha = cleanStr(fecha)
  try:
    (dia, mes, anio) = re.findall('([\d]+) de ([\w\W]+) de (\d\d\d\d)', fecha)[0]
    dia = cleanStr(dia)
    mes = cleanStr(mes)
    mes = months_map[mes]
    anio = cleanStr(anio)

    # date = {"dia":dia, "mes":mes, "anio": anio}
    date = anio + '-' + mes + '-' + dia

    return date
  except Exception:
    # return {"dia":-1, "mes":-1, "anio": -1}
    return "-1-1-1"

def cleanIdentificacion(identificacion):
  '''
    i.e: "c.c 123456"
    => { "numero": 123456, "tipo":"cc" }
  '''
  try:
    identificacion = identificacion.strip().lower()
    re_cc_and_id = r'\s*([a-z]+)\s*(\d+)\s*'

    match = re.search(re_cc_and_id, re.sub(r'\.|\,|\-', '', identificacion))

    if match is not None:
        tipo   = match.group(1)
        numero = int(match.group(2))
        # tipo_numero = {"tipo": tipo, "numero": numero}
        tipo_numero = tipo + ' ' + numero
        return tipo_numero
    else:
        return identificacion
  except Exception:
    # return {"numero": int(identificacion), "tipo": ""}
    return identificacion

def cleanProponentes(proponentes):
  return proponentes.split("\r\n")

def cleanPlazo(plazo):
    '''
    i.e.: 3 Meses => 90
    i.e.: 200 Días => 200
    '''
    re_meses = r'\s*(\d+)\s*Meses\s*'
    re_dias = r'\s*(\d+)\s*Días\s*'
    match_meses = re.search(re_meses, plazo)
    match_dias = re.search(re_dias, plazo)

    try:
        if match_meses is not None:
            return int(match_meses.group(1)) * 30
        elif match_dias is not None:
            return int(match_dias.group(1))
        else:
            return plazo
    except Exception:
        return plazo
