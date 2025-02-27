# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
DPCIConfigurationFunction = Class(name="DPCIConfigurationFunction", synonyms=["Represents the DPCICONFIGURATIONFunction IOC."])

# DPCIConfigurationFunction class attributes and methods
DPCIConfigurationFunction_dPciConfigurationControl: Property = Property(name="dPciConfigurationControl", type=BooleanType, synonyms=["This attribute determines whether the Distributed SON or Domain-Centralized SON PCI configuration Function is enabled or disabled."])
DPCIConfigurationFunction_nRPciList: Property = Property(name="nRPciList", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["This holds a list of physical cell identities that can be assigned to the NR cells. This attribute shall be supported if D-SON PCI configuration or domain Centralized SON PCI configuration function is supported."])
DPCIConfigurationFunction.attributes={DPCIConfigurationFunction_dPciConfigurationControl, DPCIConfigurationFunction_nRPciList}

NRPciList = Class(name="NRPciList", synonyms=["Represents the NR PCI list for the PCI configuration function."])

# NRPciList class attributes and methods
NRPciList_NRPci: Property = Property(name="NRPci", type=IntegerType, synonyms=["This attribute determines the NR PCI."])
NRPciList.attributes={NRPciList_NRPci}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-dpciconfigurationfunction",
    types={DPCIConfigurationFunction, NRPciList},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the DPCIConfigurationFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
