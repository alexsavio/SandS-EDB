import os
import sys

import socket
from mongoengine import *
# pip install fake-factory
from faker import Factory

hn = socket.gethostname()
if hn == 'ayerdi':
    sys.path.append('/home/ayerdi/Dropbox/SandS-EDB/repo/src')
else:    
    basedir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.join(basedir))

from keys import host_ip, generator_db, \
                 generator_user, generator_password

connect(generator_db, host=host_ip, 
        username=generator_user, password=generator_password)


from mongoengine_models import *
from random import randrange

fake = Factory.create()

##########################
# NO TIENEN DEPENDENCIAS #
##########################

def gen_Preference():
    insert = Preference()
    # MODIFY
    v1 = ['Criterion 1', 'Criterion 2', 'Criterion 3', 'Criterion 4', 'Criterion 5']
    # NOT MODIFY
    v2 = ['agree', 'neutral', 'disagree', 'partialAgree', 'partialDisagree']
    insert.criterion = v1[randrange(len(v1))]
    insert.value = v2[randrange(len(v2))]

    insert.save()
    return insert

def gen_Parameter():
    insert = Parameter()
    # MODIFY
    v1 = ['Name 1', 'Name 2', 'Name 3', 'Name 4', 'Name 5']
    # MODIFY
    v2 = ['Value 1', 'Value 2', 'Value 3', 'Value 4', 'Value 5']
    insert.name = v1[randrange(len(v1))]
    insert.value = v2[randrange(len(v2))]

    insert.save()
    return insert    

def gen_Evaluation():
    insert = Evaluation()
    # MODIFY
    v1 = ['Criterion 1', 'Criterion 2', 'Criterion 3', 'Criterion 4', 'Criterion 5']
    # NOT MODIFY
    v2 = ['optimum', 'good', 'neutral', 'bad', 'verybad']
    insert.criterion = v1[randrange(len(v1))]
    insert.value = v2[randrange(len(v2))]

    insert.save()
    return insert

def gen_Warning():
    insert = Warning()
    # MODIFY
    v1 = ['Message 1', 'Message 2', 'Message 3', 'Message 4', 'Message 5']
    # MODIFY
    v2 = [1,2,3,4,5]
    insert.message = v1[randrange(len(v1))]
    insert.instructionNum = v2[randrange(len(v2))]
    insert.save()
    return insert

def gen_Instruction():
    insert = Instruction()
    # MODIFY
    v1 = ['Name 1', 'Name 2', 'Name 3', 'Name 4', 'Name 5']
    # MODIFY
    v2 = ['Value 1', 'Value 2', 'Value 3', 'Value 4', 'Value 5']
    # MODIFY
    v3 = ['Type 1', 'Type 2', 'Type 3', 'Type 4', 'Type 5']
    # MODIFY
    v4 = [1,2,3,4,5]
    insert.name = v1[randrange(len(v1))]
    insert.value = v2[randrange(len(v2))]
    insert.type = v3[randrange(len(v3))]
    insert.duration = v4[randrange(len(v4))]

    insert.save()
    return insert


#######################
# TIENEN DEPENDENCIAS #
#######################

def gen_Request():
    insert = Request()
    # MODIFY
    v2 = ['Action 1', 'Action 2', 'Action 3', 'Action 4', 'Action 5']
    # NOT MODIFY
    v4 = ['waitingRecipe', 'waitingForExecution', 'executing', 'feedback', 'error', 'complete']
    insert.date = fake.date(pattern="%d/%m/%Y")
    insert.action = v2[randrange(len(v2))]
    insert.time = fake.time(pattern="%H:%M:%S") 
    insert.status = v4[randrange(len(v4))]

    # MODIFY?
    rangeInit = 1
    # MODIFY?
    rangeEnd = 11

    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_Parameter())
    insert.Parameters = lista

    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_Evaluation())
    insert.Evaluations = lista

    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_Warning())
    insert.Warnings = lista

    # Buscamos una receta aleatoria.
    dim = len(Recipe.objects)
    insert.Recipe = Recipe.objects[randrange(dim)]

    insert.EngagedAppliance = gen_EngagedAppliance()
    
    insert.save()
    return insert

def gen_Eahouker():
    insert = Eahouker()
    # MODIFY
    v4 = ['male', 'female', 'gay', 'lesbian', 'shemale', 'neutral', 'chaste']
    # MODIFY
    v5 = [1,2,3,4,5]
    # MODIFY
    v6 = ['single', 'married', 'separated']

    insert.userName = fake.user_name()  
    insert.pwd = fake.password(length=14)
    insert.birthday = fake.date(pattern="%d/%m/%Y")
    insert.sex = v4[randrange(len(v4))]
    insert.numChildren = v5[randrange(len(v5))]
    insert.socialStatus = v6[randrange(len(v6))]

    # MODIFY?
    rangeInit = 1
    # MODIFY?
    rangeEnd = 11

    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_Preference())
    insert.Preference = lista

    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_Location())
    insert.Location = lista

    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_Request())
    insert.Request = lista

    insert.save()
    return insert


def gen_Instruction():
    insert = Instruction()
    # MODIFY
    v1 = ['Name 1', 'Name 2', 'Name 3', 'Name 4', 'Name 5']
    # MODIFY
    v2 = ['Value 1', 'Value 2', 'Value 3', 'Value 4', 'Value 5']

    insert.name = v1[randrange(len(v1))]
    insert.value = v2[randrange(len(v2))]
    insert.save()
    return insert

def gen_Recipe():
    insert = Recipe()
    # MODIFY
    v1 = [1,2,3,4,5]
    # MODIFY
    v2 = [1.0,2.0,3.0,4.0,5.0]
    # NOT MODIFY
    v3 = [True, False]

    insert.numExecutions = v1[randrange(len(v1))]
    insert.qualityIndex = v2[randrange(len(v2))]
    insert.isBasic = v3[randrange(len(v3))]

    # MODIFY?
    rangeInit = 1
    # MODIFY?
    rangeEnd = 11

    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_Instruction())
    insert.Instructions = lista

    insert.save()
    return insert
    
def gen_BasicRecipe():
    insert = BasicRecipe()
    
    # MODIFY?
    rangeInit = 1
    # MODIFY?
    rangeEnd = 11
    
    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_Instruction())
    insert.Instructions = lista
    
    insert.save()
    return insert

def gen_Manufacturer():
    insert = Manufacturer()
    insert.userName = fake.company()
    insert.pwd = fake.password(length=14)    
    insert.url = fake.url() 
    
    insert.save()
    return insert
    
def gen_ApplianceModel():
    insert = ApplianceModel()
    # MODIFY
    v3 = ['Certification 1', 'Certification 2', 'Certification 3', 'Certification 4', 'Certification 5']

    insert.brand = fake.company() 
    insert.model = fake.last_name()
    insert.certification = v3[randrange(len(v3))]
    

    dim = len(Manufacturer.objects)
    insert.Manufacturer = Manufacturer.objects[randrange(dim)]
    
    # Ponemos un valor random de 0 a 100
    insert.consume = {'gas':randrange(100), 'power':randrange(100),'water':randrange(100),'temperature':randrange(100)}
   
    # MODIFY
    v4 = ['Power 1', 'Power 2', 'Power 3', 'Power 4', 'Power 5']
    # MODIFY
    v5 = ['inletWaterFlow 1', 'inletWaterFlow 2', 'inletWaterFlow 3', 'inletWaterFlow 4', 'inletWaterFlow 5']
    # MODIFY
    v6 = ['maxInletWaterPressure 1', 'maxInletWaterPressure 2', 'maxInletWaterPressure 3', 'maxInletWaterPressure 4', 'maxInletWaterPressure 5']

    insert.TechnicalData = {'power':v4[randrange(len(v4))], 'inletWaterFlow':v5[randrange(len(v5))],'maxInletWaterPressure':v6[randrange(len(v6))]}
    
    # MODIFY
    v7 = ['Action 1', 'Action 2', 'Action 3', 'Action 4', 'Action 5']
    # MODIFY
    v8 = ['Criteria 1', 'Criteria 2', 'Criteria 3', 'Criteria 4', 'Criteria 5']
    # MODIFY
    v9 = ['Exception 1', 'Exception 2', 'Exception 3', 'Exception 4', 'Exception 5']
    # MODIFY
    v10 = ['Event 1', 'Event 2', 'Event 3', 'Event 4', 'Event 5']
    
    # MODIFY?
    rangeInit = 1
    # MODIFY?
    rangeEnd = 11
    
    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(v7[randrange(len(v7))])
    insert.actions = lista
    
    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(v8[randrange(len(v8))])
    insert.criteria = lista
    
    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(v9[randrange(len(v9))])
    insert.exceptions = lista
    
    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(v10[randrange(len(v10))])
    insert.events = lista

    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_BasicRecipe())
    insert.BasicRecipes = lista
    
    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_InstructionType())
    insert.InstructionTypes = lista

    insert.save()
    return insert

    
def gen_EngagedAppliance():
    insert = EngagedAppliance()
    
    # MODIFY
    v2 = ['Status 1', 'Status 2', 'Status 3', 'Status 4', 'Status 5']

    insert.ipAddress = fake.ipv4()
    insert.status = v2[randrange(len(v2))]
    insert.encrKey = fake.sha256()
    
    dim = len(ApplianceModel.objects)
    insert.ApplianceModel = ApplianceModel.objects[randrange(dim)]

    dim = len(Location.objects)
    insert.Location = Location.objects[randrange(dim)].to_dbref() 
    
    insert.save()
    return insert
    
    
def gen_Location():

    insert = Location()
    insert.address = {'street':fake.street_name() , 'country':fake.country() ,'position':fake.building_number(),'number':fake.building_number(),'city':fake.city()}
    insert.ipAddress = fake.ipv4()
    
    # MODIFY?
    rangeInit = 1
    # MODIFY?
    rangeEnd = 11

    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_HomeRule())
    insert.HomeRules = lista
 
    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_HomeRuleFormat())
    insert.HomeRuleFormats = lista 

    insert.save()
    return insert 
    
    
def gen_HomeRule():
    insert = HomeRule()
    # MODIFY
    v1 = ['Condition 1', 'Condition 2', 'Condition 3', 'Condition 4', 'Condition 5']
    # MODIFY
    v2 = ['Action 1', 'Action 2', 'Action 3', 'Action 4', 'Action 5']
    
    insert.condition = v1[randrange(len(v1))]
    insert.action = v2[randrange(len(v2))]
    
    insert.save()
    return insert
    
    
def gen_HomeRuleFormat():
    insert = HomeRuleFormat()
    # MODIFY
    v1 = ['Parameter 1', 'Parameter 2', 'Parameter 3', 'Parameter 4', 'Parameter 5']

    insert.parameter = v1[randrange(len(v1))]
    
    insert.save()
    return insert

def gen_InstructionType():
    insert = InstructionType()
    # MODIFY
    v1 = ['Name 1', 'Name 2', 'Name 3', 'Name 4', 'Name 5']

    insert.name = v1[randrange(len(v1))]

    # MODIFY
    v2 = ['Discrete 1', 'Discrete 2', 'Discrete 3', 'Discrete 4', 'Discrete 5']
    
    # MODIFY?
    rangeInit = 1
    # MODIFY?
    rangeEnd = 11
    
    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(v2[randrange(len(v2))])
    insert.discrete = lista
    
    min = randrange(100)
    max = min + randrange(400)
    step = randrange(200)
    default = randrange(100)
    
    insert.continuous = {'minValue':min, 'maxValue':max,'step':step,'defaultValue':default}
    
    insert.save()
    return insert


#
#for i in range(1000)
#gen_Manufacturer()
#gen_ApplianceModel()
#gen_Location()
#gen_EngagedAppliance()

for i in range(100):
    gen_Manufacturer()

for i in range(25000):
    gen_ApplianceModel()

for i in range(2000000):
    gen_Recipe()

for i in range(1000000):
    gen_Eahouker()

#gen_Preference()
#gen_Parameter()
#gen_Evaluation()
#gen_Warning()
#gen_Instruction()
#gen_Recipe()
#gen_Request()
#gen_HomeRule()
#gen_HomeRuleFormat()
#gen_Location()
#gen_Eahouker()
#gen_BasicRecipe()
#gen_Manufacturer()
#gen_InstructionType()
#gen_ApplianceModel()
#gen_EngagedAppliance()

imprimir = False
if imprimir:
    print '### PREFERENCE ###'
    for examples in Preference.objects:
        print examples.criterion
        print examples.value   

    print '### PARAMETER ###'
    for examples in Parameter.objects:
        print examples.name
        print examples.value   

    print '### EVALUATION ###'
    for examples in Evaluation.objects:
        print examples.criterion
        print examples.value 

    print '### WARNING ###'
    for examples in Warning.objects:
        print examples.message
        print examples.instructionNum 

    print '### INSTRUCTION ###'
    for examples in Instruction.objects:
        print examples.name
        print examples.value 

    print '### RECIPE ###'
    for examples in Recipe.objects:
        print examples.numExecutions
        print examples.qualityIndex 
        print examples.isBasic 
        print examples.Instructions 

    print '### REQUEST ###'
    for examples in Request.objects:
        print examples.date
        print examples.action 
        print examples.time
        print examples.status
        print examples.Parameters
        print examples.Evaluations
        print examples.Warnings
        print examples.Recipe

    print '### HOME RULE ###'
    for examples in HomeRule.objects:
        print examples.condition
        print examples.action 

    print '### HOME RULE FORMAT ###'
    for examples in HomeRuleFormat.objects:
        print examples.parameter

    print '### LOCATION ###'
    for examples in Location.objects:
        print examples.address
        print examples.ipAddress 
        print examples.HomeRules 
        print examples.HomeRuleFormats 

    print '### EAHOUKER ###'
    for examples in Eahouker.objects:
        print examples.userName
        print examples.pwd 
        print examples.birthday 
        print examples.sex 
        print examples.numChildren 
        print examples.socialStatus 
        print examples.Preference 
        print examples.Request 
        print examples.Location 

    print '### BASIC RECIPE ###'
    for examples in BasicRecipe.objects:
        print examples.Instructions

    print '### MANUFACTURER ###'
    for examples in Manufacturer.objects:
        print examples.userName
        print examples.pwd
        print examples.url

    print '### INSTRUCTION TYPE ###'
    for examples in InstructionType.objects:
        print examples.name
        print examples.continuous 
        print examples.discrete 

    print '### APPLIANCE MODEL ###'
    for examples in ApplianceModel.objects:
        print examples.brand
        print examples.model 
        print examples.certification 
        print examples.Manufacturer 
        print examples.consume 
        print examples.TechnicalData 
        print examples.actions 
        print examples.criteria 
        print examples.exceptions
        print examples.events 
        print examples.BasicRecipes 
        print examples.InstructionTypes 

    print '### ENGAGED APPLIANCE ###'
    for examples in EngagedAppliance.objects:
        print examples.ipAddress
        print examples.status 
        print examples.encrKey 
        print examples.ApplianceModel 
        print examples.Location 



borrar = False
if borrar:
    Preference.drop_collection()
    Parameter.drop_collection()
    Evaluation.drop_collection()
    Warning.drop_collection()
    Instruction.drop_collection()
    Recipe.drop_collection()
    Request.drop_collection()
    HomeRule.drop_collection()
    HomeRuleFormat.drop_collection()
    Location.drop_collection()
    Eahouker.drop_collection()
    BasicRecipe.drop_collection()
    Manufacturer.drop_collection()
    InstructionType.drop_collection()
    ApplianceModel.drop_collection()
    EngagedAppliance.drop_collection()

