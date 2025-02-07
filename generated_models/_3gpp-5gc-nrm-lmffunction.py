# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
LMFFunction = Class(name="LMFFunction")

# LMFFunction class attributes and methods
LMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
LMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
LMFFunction_commModelList: Property = Property(name="commModelList", type=list)
LMFFunction.attributes={LMFFunction_pLMNIdList, LMFFunction_managedNFProfile, LMFFunction_commModelList}

