import couchdb
import sys
import urllib2
import json
import re



URL = 'localhost'
db_name = 'datosfinal'


'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()

url = 'http://localhost:5984/datosfinal/_design/limpiar/_view/textolimpioGuayaquil'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())


patron = re.compile('\+')
contPositivo = 0
contNegativo = 0
contNeutro=0
archivo = open("E:\pruebaGuayaquil2.json","a")
archivo.write('[')
bandera=False
apoyo=""
for x in d['rows']:
    a= x['value']['text']
    text = ''

    for letra in a:
       if re.match('([A-Za-z0-9.:;,//\s])', letra):
          text += letra

    if (("votaciones2018S" in text
                    or "7VecesS" in text
                    or "stasEC" in text
                    or "siete veces SI" in text
                    or "stoyConLenin" in text
                    or "sConLenin" in text
                    or "DiceS" in text
                    or "sEcu" in text
                    or "Vota todo si" in text
                    or "VotaS" in text
                    or "votaciones2018S" in text
                    or "Votar" in text
                    or "votoreflexivo" in text
                    or "EcuadorDiceSi" in text
                    or "TerceraVaECUADOR" in text
                    or "SiRotundo" in text
                    or "EcuadorVotaSi" in text
                    or "Vota7vecesS." in text
                    or "TerceraVa" in text
                    or "VotoEnCasa" in text
                    or "votaciones2018SI" in text
                    or "VotaTodoS" in text
                    or "votaciones2018s" in text
                    or "consulta2018" in text
                    or "VotaTodoSi" in text
                    or "VotaNulo" in text
                    or "ATuFuturoDileSi" in text
                    or "EcuadorDiceS" in text
                    or "GuayasDiceS" in text
                    or "TodoSi" in text
                    or "TodoSI" in text
                    or "TodoS" in text
                    or "NOALaViolencia" in text
                    or "JuntosPorElS" in text
                    or "ObvioQueS" in text
                    or "vota si" in text
                    or "7 veces s" in text
                    or "NoBotesTuVoto" in text
                    or "PichinchaDiceS" in text
                    or "Todito S" in text in text)
            and ("SiSePuede" not in text) and ("Sismo" not in text) and ("Sin" not in text)) :
        bandera = True
        apoyo = "si"
        contPositivo += 1

    elif ("7VecesNO" in text
                or "DilesNO" in text
                or "TodoNO" in text
                or "Todono" in text
                or "Nooo" in text
                or "7 veces n" in text
                or "YoVotoNO" in text
                or "PorLaPatriaDilesNO" in text
                or "YoVotNO" in text
                or "vota no" in text
                or "MoreNO" in text
                or "PichinchaDiceN" in text
                or "PichinchaConElNo" in text
                or "EcuadorDiceNO" in text
                or "NON" in text
                or "DilesN" in text
                or "SieteVecesN" in text
                or "NoN" in text
                or "ConsultaMentirosa" in text
                or "Todito N" in text
                or "Todo N" in text
                or "NoALaConsultaMa" in text
                or "ElPuebloContigoRafael" in text
                or "GuayasDiceN" in text
                or "traidor" in text):
        bandera = True
        apoyo = "no"
        contNegativo += 1

    elif ("ConsultaPopular2018" in text
                            or "ReferendumConsultaPopular2018febrero04" in text
                            or "Lenin" in text
                            or "VotacionesEcuador" in text
                            or "consulta2018" in text
                            or "votonacional" in text
                            or "votaciones" in text
                            or "MashiRafael" in text
                            or "GuayasDiceN" in text
                            or "PichinchaDiceN" in text
                            or "PichinchaConElNo" in text
                            or "votaconresponsabilidad" in text
                            or "votaconconciencia" in text
                            or "EcuadorSaleAVotar" in text):
        bandera = True
        apoyo = "nu"
        contNeutro += 1

    if bandera:
        archivo.write("\n" + "\t")
        data = {}
        data['label'] = apoyo
        data['text'] = text
        json_data = json.dumps(data)
        archivo.write(json_data)
        archivo.write(",")
        bandera=False
        apoyo=""

archivo.write("\n"+']')
archivo.close
print("Contador a Favor: "+str(contPositivo))
print("Contador en Contra: "+str(contNegativo))
print("Contador Neutros: "+str(contNeutro))


