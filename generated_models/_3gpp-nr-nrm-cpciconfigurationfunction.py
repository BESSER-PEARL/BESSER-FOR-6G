# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
CPCIConfigurationFunction = Class(name="CPCIConfigurationFunction")

# CPCIConfigurationFunction class attributes and methods
CPCIConfigurationFunction_cPciConfigurationControl: Property = Property(name="cPciConfigurationControl", type=BooleanType)
CPCIConfigurationFunction_cSonPciList: Property = Property(name="cSonPciList", type=list)
CPCIConfigurationFunction.attributes={CPCIConfigurationFunction_cPciConfigurationControl, CPCIConfigurationFunction_cSonPciList}

CSonPciList = Class(name="CSonPciList")

# CSonPciList class attributes and methods
CSonPciList_NRPci: Property = Property(name="NRPci", type=IntegerType)
CSonPciList.attributes={CSonPciList_NRPci}

