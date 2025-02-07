# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
DPCIConfigurationFunction = Class(name="DPCIConfigurationFunction")

# DPCIConfigurationFunction class attributes and methods
DPCIConfigurationFunction_dPciConfigurationControl: Property = Property(name="dPciConfigurationControl", type=BooleanType)
DPCIConfigurationFunction_nRPciList: Property = Property(name="nRPciList", type=list)
DPCIConfigurationFunction.attributes={DPCIConfigurationFunction_dPciConfigurationControl, DPCIConfigurationFunction_nRPciList}

NRPciList = Class(name="NRPciList")

# NRPciList class attributes and methods
NRPciList_NRPci: Property = Property(name="NRPci", type=IntegerType)
NRPciList.attributes={NRPciList_NRPci}

