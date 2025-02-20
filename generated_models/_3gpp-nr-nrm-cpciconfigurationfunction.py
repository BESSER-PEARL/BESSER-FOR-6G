# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

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

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-cpciconfigurationfunction",
    types={CPCIConfigurationFunction, CSonPciList},
    associations={},
    generalizations={}
)
