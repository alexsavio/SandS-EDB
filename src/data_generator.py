
import os
import sys

import socket
from mongoengine import *

hn = socket.gethostname()
if hn == 'ayerdi':
    sys.path.append('/home/ayerdi/Dropbox/SandS-EDB/src')
else:    
    basedir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.join(basedir))

from keys import host_ip, generator_db, \
                 generator_user, generator_password

connect(generator_db, host=host_ip, 
        username=generator_user, password=generator_password)


from mongoengine_models import *
from random import randrange

##########################
# NO TIENEN DEPENDENCIAS #
##########################

def gen_Preference(Eahouker):
    insert = Preference()
    # MODIFY
    v1 = ['Criterion 1', 'Criterion 2', 'Criterion 3', 'Criterion 4', 'Criterion 5']
    # NOT MODIFY
    v2 = ['agree', 'neutral', 'disagree', 'partialAgree', 'partialDisagree']
    insert.criterion = v1[randrange(len(v1))]
    insert.value = v2[randrange(len(v2))]
    insert.Eahouker = Eahouker

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

def gen_Request(Recipe):
    insert = Request()
    # MODIFY
    v1 = ['03/02/2014', '03/02/2014', '03/02/2014', '03/02/2014', '03/02/2014']
    # MODIFY
    v2 = ['Action 1', 'Action 2', 'Action 3', 'Action 4', 'Action 5']
    # MODIFY
    v3 = ['10:20:45', '10:20:45', '10:20:45', '10:20:45', '10:20:45']
    # NOT MODIFY
    v4 = ['waitingRecipe', 'waitingForExecution', 'executing', 'feedback', 'error', 'complete']
    insert.date = v1[randrange(len(v1))]
    insert.action = v2[randrange(len(v2))]
    insert.time = v3[randrange(len(v3))]
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

    insert.Recipe = Recipe
    
    insert.save()
    return insert

def gen_Eahouker():
    insert = Eahouker()
    # MODIFY
    v1 = ['UserName 1', 'UserName 2', 'UserName 3', 'UserName 4', 'UserName 5']
    # MODIFY
    v2 = ['Password 1', 'Password 2', 'Password 3', 'Password 4', 'Password 5']
    # MODIFY
    v3 = ['03/02/2014', '03/02/2014', '03/02/2014', '03/02/2014', '03/02/2014']
    # MODIFY
    v4 = ['male', 'female', 'gay', 'lesbian', 'shemale', 'neutral', 'chaste']
    # MODIFY
    v5 = [1,2,3,4,5]
    # MODIFY
    v6 = ['single', 'married', 'separated']

    insert.userName = v1[randrange(len(v1))]
    insert.pwd = v2[randrange(len(v2))]
    insert.birthday = v3[randrange(len(v3))]
    insert.sex = v4[randrange(len(v4))]
    insert.numChildren = v5[randrange(len(v5))]
    insert.socialStatus = v6[randrange(len(v6))]

    # MODIFY?
    rangeInit = 1
    # MODIFY?
    rangeEnd = 11

    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_Preference(insert))
    insert.Preference = lista

    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_Request(insert))
    insert.Request = lista

    insert.Location = gen_Location()

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

    #lista = []
    #for i in range(randrange(rangeInit,rangeEnd)):
    #    lista.append(gen_Request(insert))
    #insert.Requests = lista

    lista = []
    for i in range(randrange(rangeInit,rangeEnd)):
        lista.append(gen_Instruction())
    insert.Instructions = lista

    insert.save()
    return insert
    
def gen_InstructionForAppliance()
    insert = InstructionForAppliance()
    insert.Instruction = gen_Instruction()
    insert.range = 


# Print 
for examples in Preference.objects:
    print examples.criterion
    print examples.value    

# Print 
for examples in Parameter.objects:
    print examples.name
    print examples.value   

for examples in Request.objects:
    print examples.date
    print examples.Evaluations 
    print examples.Warnings

for examples in Eahouker.objects:
    print examples.Preference
    print examples.Request 
