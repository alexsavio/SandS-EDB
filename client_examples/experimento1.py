#Al estar la EDB inicialmente vacía, vamos a incluir 1 request
#(request_complet.json) . En esta request  se especifican:


import os
import sys
basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(basedir, '..')

from keys import *

from sands_client import SandsClient

#sands_url = 'http://localhost:5000/api/'
#SERVER_NAME = '158.227.113.136:8080'
#SERVER_NAME = 'api.sands-social-network-mockup.com:8080'

sands_url = 'http://api.sands-social-network-mockup.com:8080/api/'

sands_auth = ('sands', sands_password1)

req_json_hdrs = {'content-type': 'application/json'}
req_xml_hdrs = {'content-type': 'application/xml'}

resp_json_hdrs = {'accept': 'application/json'}
resp_xml_hdrs  = {'accept': 'application/xml'}

my_headers = {}
my_headers.update(req_json_hdrs)
my_headers.update(resp_json_hdrs)

#r = requests.get(sands_url + 'Evaluation', auth=sands_auth, headers=my_headers)


#Sands Client
sands_client = SandsClient(sands_url, sands_auth, my_headers)

#Evaluations
evals_url = 'Evaluation'

eval1_payload = {"criterion": "Fragrance",
                "value": "agree",}
#eval1_id = sands_client.post(evals_url, eval1_payload)


eval2_payload = {"criterion": "Softness",
                 "value": "agree",}
#eval2_id = sands_client.post(evals_url, eval2_payload)


eval3_payload = {"criterion": "Crust",
                 "value" : "neutral",}
#eval3_id = sands_client.post(evals_url, eval3_payload)

evals_payloads = [eval1_payload, eval2_payload, eval3_payload]

evals_ids = sands_client.post(evals_url, evals_payloads)

evals = sands_client.get(evals_url)

#param
params_url = 'Parameter'

param1_payload = {"name": "bread type",
                  "value": "white",}
#param1_id = sands_client.post(params_url, param1_payload)


param2_payload = {"name": "bread texture",
                  "value": "soft" ,}
#param2_id = sands_client.post(params_url, param2_payload)

params_payload = [param1_payload, param2_payload]
params_ids = sands_client.post(params_url, params_payload)

params = sands_client.get(params_url)


#Request
requests_url = 'Request'

req1_payload = {"eahouker": "eahouker1",
                "engAppliance": "engAppliance1",
                "date": "17/12/2013",
                "time": "18:30:00",
                "action": "cook bread",
                "status": "complete",
                "Parameters": params_ids,
                "Evaluations": evals_ids}

req1_id = sands_client.post(requests_url, req1_payload)

#Instructions
instructions_url = 'Instruction'

inst1_payload = {"name": "MOTOR ON",
                 "type": "**??**",
                 "value": "**??**",
                 "duration": -1}

inst2_payload = {"name": "WAIT 1s",
                 "type": "**??**",
                 "value": "**??**",
                 "duration": -1}

inst3_payload = {"name": "MOTOR OFF",
                 "type": "**??**",
                 "value": "**??**",
                 "duration": -1}

inst4_payload = {"name": "WAIT 1s",
                 "type": "**??**",
                 "value": "**??**",
                 "duration": -1}

inst5_payload = {"name": "MOTOR ON",
                 "type": "**??**",
                 "value": "**??**",
                 "duration": -1}

inst6_payload = {"name": "WAIT 30m",
                 "type": "**??**",
                 "value": "**??**",
                 "duration": -1}

inst7_payload = {"name": "SET TEMPERATURE 180",
                 "type": "**??**",
                 "value": "**??**",
                 "duration": -1}

inst8_payload = {"name": "HEATER ON",
                 "type": "**??**",
                 "value": "**??**",
                 "duration": -1}

inst9_payload = {"name": "WAIT 1h",
                 "type": "**??**",
                 "value": "**??**",
                 "duration": -1}

inst10_payload = {"name": "SET TEMPERATURE 220",
                  "type": "**??**",
                  "value": "**??**",
                  "duration": -1}

inst11_payload = {"name": "WAIT 10m",
                  "type": "**??**",
                  "value": "**??**",
                  "duration": -1}

inst12_payload = {"name": "HEATER OFF",
                  "type": "**??**",
                  "value": "**??**",
                  "duration": -1}

insts_payloads = [inst1_payload, inst2_payload, inst3_payload,
                  inst4_payload, inst5_payload, inst6_payload,
                  inst7_payload, inst8_payload, inst9_payload,
                  inst10_payload, inst11_payload, inst12_payload,]

insts_ids = sands_client.post(instructions_url, insts_payloads)

#Recipe
recipes_url = 'Recipe'

rec1_payload = {"numExecutions": 5,
                "qualityIndex": 4.3,
                "isBasic": False,
                "Requests": [req1_id],
                "Instructions": insts_ids,}

rec1_id = sands_client.post(recipes_url, rec1_payload)


#1) parámetros de la propia request (id, action,date,time,status)
#2) parámetros que describen el problema de la request (name-value)
#3) las instrucciones de la request
#4) la evaluación

#1er EXPERIMENTO: Introducir una Request para obtener instrucciones y
#enviar una evaluación

#a) Suponemos que el DI envía al ESN un JSON con una request. #(asked_request.json). En este caso el DI, tendrá que enviar lo que se detalla como request y como param. (Bien todo en 1 json o bien en 2, como tu creas que será mas fácil para nosotros)

#New request
#param

req2_payload = {"eahouker": "eahouker2",
                "engAppliance": "engAppliance1",
                "date": "03/01/2014",
                "time": "13:50:00",
                "action": "cook bread",
                "status": "waitingRecipe",
                "Parameters": params_ids,}

req2_id = sands_client.post(params_url, req2_payload)


#b) Guardamos esta request (request+param) en la EDB.

#c) Simulamos que le enviamos esto al NI para que nos dé
#una solución.

#d) El NI nos envía un documento ask_info.json para enviarle
#documentos json que cumplan las especificaciones que nos indica.
#(esto podrá ser muy variable porque dependiendo del caso, nos pedirá una información u otra)
ni_actiondata_request = {"action": "cook bread",
                         "parameters": params_ids,}

#e) Le enviamos al NI el documento request_complet.json a
#modo de respuesta a su consulta.
####esto se encuentra al principio de este documento. (request+param+eval+recipe+instructions)
response_to_ni = sands_client.get_by_id(recipes_url, rec1_id)


#f) El NI nos genera una solución. Para este caso, suponemos que el
#NI ha modificado el STATUS de la receta. (asked_request_answered.json)
#Nos entregara lo que viene continuación

#request
req2_payload_patch = {"status": "waitingForExecution",}

req2_id = sands_client.patch(requests_url, req2_id, req2_payload_patch)


#recipe
rec1_payload_patch = {"request": req2_id,
                      "instructions": insts_payload}

#instructions
eq2_id = sands_client.patch(recipes_url, rec1_id, rec1_payload_patch)

#g)   actualizamos la Request de la EDB puesto que el NI solo le ha cambiado el status

#h) Guardamos lo que nos haya entregado el NI. el nuevo documento en la EDB que incluye
#la solución propuesta por el NI.

#i) Se la enviamos al DI.

#j) En algún momento, el DI nos pedirá que actualicemos el status
#de esa receta porque se está ejecutando.
#Para ello nos enviará un documento JSON (executing.json)
req2_payload_patch1 = {"status": "executing"}

#k) En otro momento, el DI nos comunicará que la ejecución ha finalizado
#y nos pedirá que actualicemos el status de esa receta.
#Para ello nos enviará un documento JSON (feedback.json)
req2_payload_patch2 = {"status": "feedback"}

#l) En ese momento, el DI nos enviará el documento de la receta
#"asked_request_answered)" con la evaluación que haya
#introducido el usuario. (request_finished.json).
#El DI incluye de oficio el nuevo STATUS de la receta: COMPLETE.
eval5_payload = {"criterion": "Fragrance",
                 "value": "agree",}

eval6_payload = {"criterion": "Softness",
                 "value": "agree",}

eval7_payload = {"criterion": "Crust",
                 "value": "neutral",}

evals2_payloads = [eval5_payload, eval6_payload, eval7_payload]

#m) Actualizamos la request (porque contiene la evaluacion y el status) y añadimos lo referente a la
# evaluación el documento de  la receta vieja "asked_request_answered" y guardamos esta nueva en la EDB.
req2_payload_patch3 = {"status" : "complete",
                       "evalutations" : evals2_payloads,}




