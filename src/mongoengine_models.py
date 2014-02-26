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
    Eahouker = ReferenceField(Eahouker)
    
# Parameter
class Parameter(Document):
    name = StringField()
    value = StringField()

# Evaluation
class Evaluation(Document):
    criterion = StringField()
    value = StringField(choices=('optimum', 'good', 'neutral', 'bad', 'verybad'))

# Warning
class Warning(Document):
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
    Warnings = ListField(ReferenceField(Warning))
    Recipe = ReferenceField(Recipe)

# Eahouker
class Eahouker(Document):
    userName = StringField(max_length=50, required=True, unique=True)
    pwd = StringField(max_length=50, required=True)
    # Daydate
    birthday = DayDateField()
    sex = StringField(choices=('male', 'female', 'gay', 'lesbian', 'shemale', 'neutral', 'chaste'))
    numChildren = IntField()
    socialStatus = StringField(choices=('single', 'married', 'separated'))
    Preference = ListField(ReferenceField(Preference))
    Request = ListField(ReferenceField(Request))
    Location = ReferenceField(Location)

# Instruction
class Instruction(Document):
    name = StringField()
    value = StringField()
    #type = StringField()
    #duration = IntField()

# Recipe
class Recipe(Document):
    numExecutions = IntField()
    qualityIndex = FloatField()
    isBasic = BooleanField()
    #Requests = ListField(ReferenceField(Request))
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
    Manufacturer = ReferenceField(Manufacturer)
    consume = DictField(default={'gas':0, 'power':0,'water':0,'temperature':0})
    TechnicalData = DictField(default={'power':'', 'inletWaterFlow':'','maxInletWaterPressure':''})
    actions = ListField(StringField())
    criteria = ListField(StringField())
    exceptions = ListField(StringField())
    events = ListField(StringField())
    BasicRecipes = ListField(ReferenceField(BasicRecipe))
    InstructionTypes = ListField(ReferenceField(InstructionType))

# Manufacturer
class Manufacturer(Document):
    userName = StringField(unique=True)
    pwd = StringField()
    url = StringField()
    #ApplianceModels = ListField(ReferenceField(ApplianceModel))

# EngagedAppliance
class EngagedAppliance(Document):
    ipAddress = StringField()
    status = StringField()
    encrKey = StringField()
    ApplianceModel = ReferenceField(ApplianceModel)
    Location = ReferenceField(Request)
    Requests = ListField(ReferenceField(Request))
    

# Location
class Location(Document):
    address = DictField(default={'street':'', 'country':'','position':'','number':'','city':''})
    ipAddress = StringField()
    HomeRules = ListField(ReferenceField(HomeRules))
    HomeRuleFormats = ListField(ReferenceField(HomeRuleFormats))
    #EngagedAppliances = ListField(ReferenceField(EngagedAppliance))
    #Eahoukers = ListField(ReferenceField(Eahouker))

# HomeRule
class HomeRule(Document):
    condition = StringField()
    action = StringField()

# HomeRuleFormat
class HomeRuleFormat(Document):
    parameter = StringField()

# InstructionType
class InstructionType(Document):
    #type = IntField()
    name = StringField()
    continuous = DictField(default={'minValue':0, 'maxValue':0,'step':0,'defaultValue':0})
    discrete = ListField(StringField())

