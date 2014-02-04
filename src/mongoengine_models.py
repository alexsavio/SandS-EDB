from mongoengine import *

class DayDateField(StringField):
    def validate(self, value):
        """
        Enables validation for `DayDateField` schema attribute.
        :param value: field value.
        """
        from time import strptime
    
        try:
            strptime(value, "%d/%m/%Y")
        except ValueError as e:
            self.error('Invalid DayDate (format: DD/MM/YYYY): %s' % value)
            super(DayDateField, self).validate(value)

class DayHourField(StringField):
    def validate(self, value):
        """
        Enables validation for `DayHourField` schema attribute.
        :param value: field value.
        """
        from time import strptime

        try:
            strptime(value, "%H:%M:%S")
        except ValueError as e:
            self.error('Invalid DayHour (format: H:M:S): %s' % value)
            super(DayHourField, self).validate(value)

# Preference
class Preference(Document):
    criterion = StringField()
    value = StringField(choices=('agree', 'neutral', 'disagree', 'partialAgree', 'partialDisagree'))

# Parameter
class Parameter(Document):
    name = StringField()
    value = StringField()

# Evaluation
class Evaluation(Document):
    criterion = StringField()
    value = StringField(choices=('optimum', 'good', 'neutral', 'bad', 'verybad'))

# Warningmsg
class Warningmsg(Document):
    message = StringField()
    instructionNum = IntField()

# Request
class Request(Document):
    # Daydate
    date = DayDateField()
    action = StringField()
    # dayhour
    time = DayHourField()
    status = StringField(choices=('waitingRecipe', 'waitingForExecution', 'executing', 'feedback', 'error', 'complete'))
    Parameters = ListField(ReferenceField(Parameter))
    Evaluations = ListField(ReferenceField(Evaluation))
    Warningmsgs = ListField(ReferenceField(Warningmsg))

# Eahouker
class Eahouker(Document):
    userName = StringField(max_length=50, required=True, unique=True)
    pwd = StringField(max_length=50, required=True)
    # Daydate
    birthday = DayDateField()
    sex = StringField(choices=('male', 'female', 'gay', 'lesbian', 'shemale', 'neutral', 'chaste', 'NA'))
    numChildren = IntField()
    socialStatus = StringField(choices=('single', 'married', 'separated'))
    Preference = ListField(ReferenceField(Preference))
    Request = ListField(ReferenceField(Request))

# Instruction
class Instruction(Document):
    name = StringField()
    value = StringField()
    type = StringField()
    duration = IntField()

# Recipe
class Recipe(Document):
    numExecutions = IntField()
    qualityIndex = FloatField()
    isBasic = BooleanField()
    Requests = ListField(ReferenceField(Request))
    Instructions = ListField(ReferenceField(Instruction))

# InstructionForAppliance
class InstructionForAppliance(Document):
    Instruction = ReferenceField(Instruction))
    range = DictField(default={'range':'', 'accuracy':''})

# BasicRecipe
class BasicRecipe(Document):
    Instructions = ListField(ReferenceField(Instruction))

# ApplianceModel
class ApplianceModel(Document):
    brand = StringField()
    model = StringField()
    certification = StringField()
    consume = DictField(default={'gas':0, 'power':0,'water':0,'temperature':0})
    actions = ListField(StringField())
    criteria = ListField(StringField())
    technicalData = DictField(default={'power':'', 'inletWaterFlow':'','maxInletWaterPressure':''})
    exceptions = ListField(StringField())
    events = ListField(StringField())
    BasicRecipes = ListField(ReferenceField(BasicRecipe))

# Manufacturer
class Manufacturer(Document):
    userName = StringField(unique=True)
    pwd = StringField()
    url = StringField()
    ApplianceModels = ListField(ReferenceField(ApplianceModel))

# EngagedAppliance
class EngagedAppliance(Document):
    ipAddress = StringField()
    status = StringField()
    encrKey = StringField()
    ApplianceModel = ReferenceField(ApplianceModel)
    Requests = ListField(ReferenceField(Request))

# Location
class Location(Document):
    address = DictField(default={'street':'', 'country':'','position':'','number':'','city':''})
    ipAddress = StringField()
    EngagedAppliances = ListField(ReferenceField(EngagedAppliance))
    Eahoukers = ListField(ReferenceField(Eahouker))

# HomeRule
class HomeRule(Document):
    condition = StringField()
    action = StringField()

# HomeRuleFormat
class HomeRuleFormat(Document):
    parameter = StringField()

# InstructionDefault
class InstructionDefault(Document):
    type = IntField()
    name = StringField()
    rangeContinuous = DictField(default={'minValue':0, 'maxValue':0,'step':0,'defaultValue':0})
    # rangeDiscrete?
    rangeDiscrete = ListField(IntField())

