# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
SMSFFunction = Class(name="SMSFFunction")

# SMSFFunction class attributes and methods
SMSFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
SMSFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
SMSFFunction_commModelList: Property = Property(name="commModelList", type=list)
SMSFFunction.attributes={SMSFFunction_pLMNIdList, SMSFFunction_managedNFProfile, SMSFFunction_commModelList}

