# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
CPCIConfigurationFunction = Class(name="CPCIConfigurationFunction", synonyms=["Represents the CPCICONFIGURATIONFunction IOC."])

# CPCIConfigurationFunction class attributes and methods
CPCIConfigurationFunction_cPciConfigurationControl: Property = Property(name="cPciConfigurationControl", type=BooleanType, synonyms=["This attribute determines whether the Cross Domain-Centralized SON PCI configuration function is enabled or disabled."])
CPCIConfigurationFunction_cSonPciList: Property = Property(name="cSonPciList", type=list, synonyms=["This holds a list of physical cell identities that can be assigned to the pci attribute by gNB. The assignment algorithm is not specified. This attribute shall be supported if and only if the C-SON PCI configuration is supported."])
CPCIConfigurationFunction.attributes={CPCIConfigurationFunction_cPciConfigurationControl, CPCIConfigurationFunction_cSonPciList}

CSonPciList = Class(name="CSonPciList", synonyms=["Represents the C-SON PCI list for the PCI configuration function."])

# CSonPciList class attributes and methods
CSonPciList_NRPci: Property = Property(name="NRPci", type=IntegerType, synonyms=["This attribute determines the NR PCI."])
CSonPciList.attributes={CSonPciList_NRPci}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-cpciconfigurationfunction",
    types={CPCIConfigurationFunction, CSonPciList},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the CPCIConfigurationFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
