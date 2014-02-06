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

# Warning
class Warning(Document):
    message = StringField()
    instructionNum = IntField()

# Instruction
class Instruction(Document):
    name = StringField()
    value = StringField()

# Recipe
class Recipe(Document):
    numExecutions = IntField()
    qualityIndex = FloatField()
    isBasic = BooleanField()
    Instructions = ListField(ReferenceField(Instruction))

# Manufacturer
class Manufacturer(Document):
    userName = StringField(unique=True)
    pwd = StringField()
    url = StringField()


# BasicRecipe
class BasicRecipe(Document):
    Instructions = ListField(ReferenceField(Instruction))

# InstructionType
class InstructionType(Document):
    name = StringField()
    continuous = DictField(default={'minValue':0, 'maxValue':0,'step':0,'defaultValue':0})
    discrete = ListField(StringField())

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

# HomeRule
class HomeRule(Document):
    condition = StringField()
    action = StringField()

# HomeRuleFormat
class HomeRuleFormat(Document):
    parameter = StringField()

# Location
class Location(Document):
    address = DictField(default={'street':'', 'country':'','position':'','number':'','city':''})
    ipAddress = StringField()
    HomeRules = ListField(ReferenceField(HomeRule))
    HomeRuleFormats = ListField(ReferenceField(HomeRuleFormat))

# EngagedAppliance
class EngagedAppliance(Document):
    ipAddress = StringField()
    status = StringField()
    encrKey = StringField()
    ApplianceModel = ReferenceField(ApplianceModel)
    Location = ReferenceField(Location)
    #Requests = ReferenceField(Request)


# Request
class Request(Document):
    date = DayDateField()
    action = StringField()
    time = DayHourField()
    status = StringField(choices=('waitingRecipe', 'waitingForExecution', 'executing', 'feedback', 'error', 'complete'))
    Parameters = ListField(ReferenceField(Parameter))
    Evaluations = ListField(ReferenceField(Evaluation))
    Warnings = ListField(ReferenceField(Warning))
    Recipe = ReferenceField(Recipe)
    EngagedAppliance = ReferenceField(EngagedAppliance)

# Eahouker
class Eahouker(Document):
    userName = StringField(max_length=50, required=True, unique=True)
    pwd = StringField(max_length=50, required=True)
    birthday = DayDateField()
    sex = StringField(choices=('male', 'female', 'gay', 'lesbian', 'shemale', 'neutral', 'chaste'))
    numChildren = IntField()
    socialStatus = StringField(choices=('single', 'married', 'separated'))
    Preference = ListField(ReferenceField(Preference))
    Request = ListField(ReferenceField(Request))
    Location = ListField(ReferenceField(Location))


