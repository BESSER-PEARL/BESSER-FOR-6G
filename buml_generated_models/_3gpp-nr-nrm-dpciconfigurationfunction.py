# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

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

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-dpciconfigurationfunction",
    types={DPCIConfigurationFunction, NRPciList},
    associations={},
    generalizations={}
)
