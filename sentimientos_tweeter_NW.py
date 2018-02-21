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

url = 'http://localhost:5984/datosfinal/_design/limpiar/_view/textolimpioCuenca'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())


patron = re.compile('\+')
contPositivo = 0
contNegativo = 0
archivo = open("E:\pruebaCuenca.json","a")
archivo.write('[')
bandera=False
apoyo=""
for x in d['rows']:
    a= x['value']['text']
    text = ''

    for letra in a:
       if re.match('([A-Za-z0-9.:;,//\s])', letra):
          text += letra

    if ((text.contains("votaciones2018S")
            or text.contains("7VecesSi")
            or text.contains("VotaS")
            or text.contains("votaciones2018S")
            or text.contains("Votar")
            or text.contains("votoreflexivo")
            or text.contains("EcuadorDiceSi")
            or text.contains("TerceraVaECUADOR")
            or text.contains("SíRotundo")
            or text.contains("EcuadorVotaSí")
            or text.contains("Vota7vecesS.")
            or text.contains("TerceraVa")
            or text.contains("VotoEnCasa")
            or text.contains("votaciones2018SI")
            or text.contains("VotaTodoS")
            or text.contains("votaciones2018s")
            or text.contains("consulta2018")
            or text.contains("VotaTodoSi")
            or text.contains("VotaNulo")
            or text.contains("ATuFuturoDileSi")
            or text.contains("EcuadorDiceS")
            or text.contains("GuayasDiceS")
            or text.contains("TodoSi")
            or text.contains("TodoSI")
            or text.contains("TodoS")
            or text.contains("Si")
            or text.contains("NOALaViolencia")
            or text.contains("JuntosPorElS")
            or text.contains("ObvioQueS")
            or text.contains("vota si")
            or text.contains("7 veces s")
            or text.contains("NoBotesTuVoto")
            or text.contains("PichinchaDiceS")
            or text.contains("Todito S"))
            and (not text.contains("SiSePuede")) and (not text.contains("Sismo")) and (not text.contains("Sin"))) :
        bandera=True
        apoyo="si"
        contPositivo+=1

    elif (text.contains("7VecesNO")
            or text.contains("DilesNO")
            or text.contains("TodoNO")
            or text.contains("Todono")
            or text.contains("Nooo")
            or text.contains("7 veces n")
            or text.contains("YoVotoNO")
            or text.contains("PorLaPatriaDilesNO")
            or text.contains("YoVotNO")
            or text.contains("vota no")
            or text.contains("MoreNO")
            or text.contains("PichinchaDiceN")
            or text.contains("PichinchaConElNo")
            or text.contains("EcuadorDiceNO")
            or text.contains("NON")
            or text.contains("DilesN")
            or text.contains("SieteVecesN")
            or text.contains("NoN")
            or text.contains("ConsultaMentirosa")
            or text.contains("Todito N")
            or text.contains("Todo N")
            or text.contains("NoALaConsultaMa")
            or text.contains("ElPuebloContigoRafael")
            or text.contains("GuayasDiceN")
            or text.contains("traidor")):
        bandera=True
        apoyo="no"
        contNegativo+=1

    if bandera:
        data = {}
        data['label'] = apoyo
        data['text'] = text
        json_data = json.dumps(data)
        archivo.write(json_data)
        archivo.write(",")

archivo.write("\n"+']')
archivo.close
print("Contador a Favor: "+str(contPositivo))
print("Contador en Contra: "+str(contNegativo))


# sample data
#raw_data = {'Sentimientos': ['Positivo', 'Negativo', 'Neutro'],
#'Cantidad': [contPositivo, contNegativo, contNeutro]}

#df = pd.DataFrame(raw_data, columns = ['Sentimientos','Cantidad'])

#plt.figure(figsize=(16,8))
# plot chart
#ax1 = plt.subplot(121, aspect='equal')
#df.plot(kind='pie', y = 'Cantidad', ax=ax1, autopct='%1.1f%%',
# startangle=90, shadow=False, labels=df['Sentimientos'], legend = False, fontsize=14)


