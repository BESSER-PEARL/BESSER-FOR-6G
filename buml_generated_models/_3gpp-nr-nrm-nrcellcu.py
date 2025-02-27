# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NRCellCU = Class(name="NRCellCU", synonyms=["Represents the information required by CU that is responsible for the management of inter-cell mobility and neighbour relations via ANR."])

# NRCellCU class attributes and methods
NRCellCU_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType, synonyms=["Identifies an NR cell of a gNB. Together with corresponding gNB ID it forms the NR Cell Identifier (NCI)."])
NRCellCU_nRFrequencyRef: Property = Property(name="nRFrequencyRef", type=StringType, synonyms=["Reference to corresponding NRFrequency instance."])
NRCellCU_pLMNInfoList: Property = Property(name="pLMNInfoList", type=list, synonyms=["The PLMNInfoList is a list of PLMNInfo data type. It defines which PLMNs that can be served by the NR cell, and which S-NSSAIs that can be supported by the NR cell for corresponding PLMN in case of network slicing feature is supported."])
NRCellCU.attributes={NRCellCU_cellLocalId, NRCellCU_nRFrequencyRef, NRCellCU_pLMNInfoList}

NRCellCUGrp = Class(name="NRCellCUGrp", synonyms=["Represents the NRCellCU IOC."])

# NRCellCUGrp class attributes and methods
NRCellCUGrp_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType, synonyms=["Identifies an NR cell of a gNB. Together with corresponding gNB ID it forms the NR Cell Identifier (NCI)."])
NRCellCUGrp_nRFrequencyRef: Property = Property(name="nRFrequencyRef", type=StringType, synonyms=["Reference to corresponding NRFrequency instance."])
NRCellCUGrp_pLMNInfoList: Property = Property(name="pLMNInfoList", type=list, synonyms=["The PLMNInfoList is a list of PLMNInfo data type. It defines which PLMNs that can be served by the NR cell, and which S-NSSAIs that can be supported by the NR cell for corresponding PLMN in case of network slicing feature is supported."])
NRCellCUGrp.attributes={NRCellCUGrp_cellLocalId, NRCellCUGrp_nRFrequencyRef, NRCellCUGrp_pLMNInfoList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrcellcu",
    types={NRCellCU, NRCellCUGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the NRCellCU Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
