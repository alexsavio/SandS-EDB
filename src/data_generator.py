
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

# Preference no depende de nadie
insert = Preference()
# StringField()
insert.criterion = 'Preference 1'
# 'agree', 'neutral', 'disagree', 'partialAgree', 'partialDisagree'
insert.value = 'agree'
insert.save()

# Parameter no depende de nadie
insert = Parameter()
# StringField()
insert.name = 'Name 1'
# StringField()
insert.value = 'Value 1'
insert.save()

# Evaluation no depende de nadie
insert = Evaluation()
# StringField()
insert.criterion = 'Evaluation 1'
# 'agree', 'neutral', 'disagree', 'partialAgree', 'partialDisagree'
insert.value = 'agree'
insert.save()

# Warningmsg no depende de nadie
insert = Warningmsg()
# StringField()
insert.message = 'Message 1'
IntField()
insert.instructionNum = 1
insert.save()

# Request
insert = Request()
# DayDateField
insert.date = '03/02/2014'
# StringField
insert.action = 'clean'
# DayHourField
insert.time = '10:20:45'
# 'waitingRecipe', 'waitingForExecution', 'executing', 'feedback', 'error', 'complete'
insert.status = 'waitingRecipe'
# ListField(ReferenceField(Parameter))
lista = []
for examples in Parameter.objects:
    lista.append(examples)
insert.Parameters = lista
# ListField(ReferenceField(Evaluation))
lista = []
for examples in Evaluation.objects:
    lista.append(examples)
insert.Evaluations = lista
# ListField(ReferenceField(Warningmsg))
lista = []
for examples in Warningmsg.objects:
    lista.append(examples)
insert.Warningmsgs = lista
insert.save()


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
    print examples.Warningmsgs
