# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
NGEIRFunction = Class(name="NGEIRFunction")

# NGEIRFunction class attributes and methods
NGEIRFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
NGEIRFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
NGEIRFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
NGEIRFunction_commModelList: Property = Property(name="commModelList", type=list)
NGEIRFunction.attributes={NGEIRFunction_pLMNIdList, NGEIRFunction_sNSSAIList, NGEIRFunction_managedNFProfile, NGEIRFunction_commModelList}

