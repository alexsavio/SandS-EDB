DOMAIN = {}

#Authentication data model
account = {
    # the standard account entry point is defined as
    # '/accounts/<ObjectId>'. We define  an additional read-only entry
    # point accessible at '/accounts/<username>'.
    #'additional_lookup': {
    #    'url': '[\w]+',
    #    'field': 'username',
    #},

    # We also disable endpoint caching as we don't want client apps to
    # cache account data.
    'cache_control': '',
    'cache_expires': 0,

    'allowed_roles': ['superuser', 'admin'],

    # Finally, let's add the schema definition for this endpoint.
    'schema': {
        'username': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
        'password': {
            'type': 'string',
            'required': True,
        },
        'email': {
            'type': 'string',
        },
        'active': {
            'type': 'bool',
            'default': True,
        },
        'confirmed_at': {'type': 'datetime',},
        'roles': {
            'type': 'list',
            'allowed': 'string',
        },
    },
}
DOMAIN['account'] = account


# account_role = {
#     'allowed_roles': ['superuser', 'admin'],
#
#     # Finally, let's add the schema definition for this endpoint.
#     'schema': {
#         'name': {
#             'type': 'string',
#             'unique': True,
#         },
#         'description': {
#             'type': 'string',
#         },
#     },
# }
# DOMAIN['account_role'] = account_role
#Data model schema definition
#http://python-eve.org/config.html#schema-definition


#about users
Eahouker = {
    ## by default, the standard item entry point is defined as
    ## '/people/<ObjectId>/'. We leave it untouched, and we also enable an
    ## additional read-only entry point. This way consumers can also perform
    ## GET requests at '/people/<lastname>'.
    ##'additional_lookup': {
    ##    'url': 'regex("[\w]+")',
    ##    'field': 'name'
    ##},
    #
    ## We choose to override global cache-control directives for this resource.
    #'cache_control': 'max-age=10,must-revalidate',
    #'cache_expires': 10,
    #
    ## we only allow GET and POST at this resource endpoint.
    #'resource_methods': ['GET', 'POST', 'DELETE'],
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'userName'
    },

    #'allow_unknown': True,
    'schema': {
        'userName': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 50,
            'required': True,
            'unique': True,
        },
        'pwd': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 50,
            'required': True,
        },
        'birthday': {'type': 'daydate',},
        'sex': {
            'type': 'string',
            'allowed': ['male', 'female', 'gay', 'lesbian', 'shemale', 'neutral', 'chaste'],
        },
        'numChildren': {'type': 'integer',},
        'socialStatus': {
            'type': 'string',
            'allowed': ['single', 'married', 'separated'],
        },
        'Preference': {
            'type': 'list',
            'schema': {'type': 'objectid'}
        },
        'Request': {
            'type': 'list',
            'schema': {'type': 'objectid'}
        },
    },
}
DOMAIN['Eahouker'] = Eahouker


Preference = {
    #'allow_unknown': True,
    'schema': {
        'criterion': {'type': 'string',},
        'value': {
            'type': 'string',
            'allowed': ['agree', 'neutral', 'disagree', 'partialAgree', 'partialDisagree'],
        },

    },
}
DOMAIN['Preference'] = Preference


#about recipes
Request = {
    #'allow_unknown': True,
    'schema': {
        'date':   {'type': 'daydate',},
        'action': {'type': 'string',},
        'time':   {'type': 'dayhour',},
        'status': {
            'type': 'string',
            'allowed': ['waitingRecipe', 'waitingForExecution', 'executing', 'feedback', 'error', 'complete'],
        },
        'Parameters': {
            'type': 'list',
            'schema': {'type': 'objectid'}
        },
        'Evaluations': {
            'type': 'list',
            'schema': {'type': 'objectid'}
        },
        'Warningmsgs': {
            'type': 'list',
            'schema': {'type': 'objectid'}
        },

    },
}
#about recipes
DOMAIN['Request'] = Request


Parameter = {
    #'allow_unknown': True,
    'schema': {
        'name': {'type': 'string',},
        'value': {'type': 'string',},
    },
}
DOMAIN['Parameter'] = Parameter


Evaluation = {
    #'allow_unknown': True,
    'schema': {
        'criterion': {'type': 'string',},
        'value': {
            'type': 'string',
            'allowed': ['agree', 'neutral', 'disagree', 'partialAgree', 'partialDisagree'],
        },
    }
}
DOMAIN['Evaluation'] = Evaluation


Warningmsg = {
    #'allow_unknown': True,
    'schema': {
        'message': {'type': 'string',},
        'instructionNum': {'type': 'integer',},
    }

}
DOMAIN['Warning'] = Warningmsg


Recipe = {
    #'allow_unknown': True,
    'schema': {
        'numExecutions': {'type': 'integer',},
        'qualityIndex': {'type': 'float',},
        'isBasic': {'type': 'bool',},
        'Requests': {
            'type': 'list',
            'schema': {'type': 'objectid'}
        },
        'Instructions': {
            'type': 'list',
            'schema': {'type': 'objectid'}
        },
    },
}
DOMAIN['Recipe'] = Recipe


Instruction = {
    #'allow_unknown': True,
    'schema': {
        'name': {'type': 'string',},
        'value': {'type': 'string',},
        'type': {'type': 'string',},
        'duration': {'type': 'integer'},
    },
}
DOMAIN['Instruction'] = Instruction


#about manufacturer
Manufacturer = {
    #'allow_unknown': True,

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'userName'
    },

    'schema': {
        'userName': {
            'type': 'string',
            'unique': True,
        },
        'pwd': {'type': 'string',},
        'url': {'type': 'string',},

        'ApplianceModels': {
            'type': 'list',
            'schema': {'type': 'objectid'}
        },
    },
}
DOMAIN['Manufacturer'] = Manufacturer


#about EngagedAppliance
EngagedAppliance = {
    #'allow_unknown': True,
    'schema': {
        'ipAddress': {'type': 'string',},
        'status': {'type': 'string',},
        'encrKey': {'type': 'string',},

        'ApplianceModel': {'type': 'objectid',},

        'Requests': {
            'type': 'list',
            'schema': {'type': 'objectid'}
        },
    },
}
DOMAIN['EngagedAppliance'] = EngagedAppliance


#about location
Location = {
    #'allow_unknown': True,
    'schema': {
        'address': {
            'type': 'dict',
            'schema': {
                'street': {'type': 'string',},
                'country': {'type': 'string',},
                'position': {'type': 'string',},
                'number': {'type': 'string',},
                'city': {'type': 'string',},
            },
        },

        'ipAddress': {'type': 'string',},

        'EngagedAppliances': {
            'type': 'list',
            'schema': {'type': 'objectid'}
        },
        'Eahoukers': {
            'type': 'list',
            'schema': {'type': 'objectid'}
        },
    },
}
DOMAIN['Location'] = Location


HomeRule = {
    #'allow_unknown': True,
    'schema': {
        'condition': {'type': 'string',},
        'action': {'type': 'string',},
    },
}
DOMAIN['HomeRule'] = HomeRule


HomeRuleFormat = {
    #'allow_unknown': True,
    'schema': {
        'parameter': {'type': 'string',},
    }
}
DOMAIN['HomeRuleFormat'] = HomeRuleFormat


#about Appliances in general
ApplianceModel = {
    'allow_unknown': True,

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'model'
    },

    'schema': {
        'brand': {'type': 'string',},
        'model': {'type': 'string',},
        'certification': {'type': 'string',},

        'consume': {
            'nullable': True,
            'type': 'dict',
            'schema': {
                'gas': {'type': 'integer',},
                'power': {'type': 'integer',},
                'water': {'type': 'integer',},
                'temperature': {'type': 'integer',},
            },
        },
        'actions': {
            'type': 'list',
            'schema': {'type': 'string'}
        },
        'criteria': {
            'type': 'list',
            'schema': {'type': 'string'}
        },
        'exceptions': {
            'type': 'list',
            'schema': {'type': 'string'}
        },
        'events': {
            'type': 'list',
            'schema': {'type': 'string'}
        },
        'BasicRecipes': {
            'type': 'list',
            'schema': {'type': 'objectid'}
        },
    },
}
DOMAIN['ApplianceModel'] = ApplianceModel


BasicRecipe = {
    #'allow_unknown': True,
    'schema': {
        'Instructions': {
            'type': 'list',
            'schema': {'type': 'objectid'}
        },
    },

}
DOMAIN['BasicRecipe'] = BasicRecipe


InstructionDefault = {
    'allow_unknown': True,

    'schema': {
        'type': {'type': 'integer',},
        'name': {'type': 'string',},

        'rangeContinuous': {
            'nullable': True,
            'type': 'dict',
            'schema': {
                'minValue': {'type': 'integer',},
                'maxValue': {'type': 'integer',},
                'step': {'type': 'integer',},
                'defaultValue': {'type': 'integer',},
            },
        },

        'rangeDiscrete': {
            'type': 'list',
            'schema': {'type': 'objectid'},
            'nullable': True,
        },
    },
}
DOMAIN['InstructionDefault'] = InstructionDefault


InstructionForAppliance = {
    'allow_unknown': True,
    'schema': {
        'Instruction': {
            'type': 'objectid',
            'required': True,
        },
        'range': {
            'type': 'dict',
            'schema': {
                'range': {'type': 'string'},
                'accuracy': {'type': 'string'},
            },
        },
    },
}

DOMAIN['InstructionForAppliance'] = InstructionForAppliance
