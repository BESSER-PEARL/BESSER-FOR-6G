# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalNRCellCU = Class(name="ExternalNRCellCU", synonyms=["Represents the ExternalNRCellCU IOC."])

# ExternalNRCellCU class attributes and methods
ExternalNRCellCU_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType, synonyms=["Identifies an NR cell of a gNB. Together with corresponding gNB ID it forms the NR Cell Identifier (NCI)."])
ExternalNRCellCU_nRFrequencyRef: Property = Property(name="nRFrequencyRef", type=StringType, synonyms=["Reference to corresponding NRFrequency instance."])
ExternalNRCellCU_nRPCI: Property = Property(name="nRPCI", type=IntegerType, synonyms=["The Physical Cell Identity (PCI) of the NR cell."])
ExternalNRCellCU_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["Defines which PLMNs that are assumed to be served by the NR cell in another gNB CU-CP. This list is either updated by the managed element itself (e.g. due to ANR, signalling over Xn, etc.) or by consumer over the standard interface."])
ExternalNRCellCU.attributes={ExternalNRCellCU_cellLocalId, ExternalNRCellCU_nRFrequencyRef, ExternalNRCellCU_nRPCI, ExternalNRCellCU_pLMNIdList}

ExternalNRCellCUWrapper = Class(name="ExternalNRCellCUWrapper")

# ExternalNRCellCUWrapper class attributes and methods
ExternalNRCellCUWrapper_ExternalNRCellCU: Property = Property(name="ExternalNRCellCU", type=list, synonyms=["Represents the properties of an NRCellCU controlled by another Management Service Provider."])
ExternalNRCellCUWrapper.attributes={ExternalNRCellCUWrapper_ExternalNRCellCU}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalnrcellcu",
    types={ExternalNRCellCU, ExternalNRCellCUWrapper},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the ExternalNRCellCU Information Object Class (IOC), that is part of the NR Network Resource Model (NRM)."]
