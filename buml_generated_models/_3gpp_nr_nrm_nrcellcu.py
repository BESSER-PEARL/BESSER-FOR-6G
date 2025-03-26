# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Classes
NRCellCU = Class(name="NRCellCU", synonyms=["Represents the NRCellCU IOC."])

# NRCellCU class attributes and methods
NRCellCU_NRCellCU: Property = Property(name="NRCellCU", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Represents the information required by CU that is responsible for the management of inter-cell mobility and neighbour relations via ANR."])
NRCellCU_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType, synonyms=["Identifies an NR cell of a gNB. Together with corresponding gNB ID it forms the NR Cell Identifier (NCI)."])
NRCellCU_nRFrequencyRef: Property = Property(name="nRFrequencyRef", type=DataType('DistinguishedName'), synonyms=["Reference to corresponding NRFrequency instance."])
NRCellCU_pLMNInfoList: Property = Property(name="pLMNInfoList", type=DataType('PLMNInfo'), multiplicity=Multiplicity(1, "*"), synonyms=["The PLMNInfoList is a list of PLMNInfo data type. It defines which PLMNs that can be served by the NR cell, and which S-NSSAIs that can be supported by the NR cell for corresponding PLMN in case of network slicing feature is supported."])
NRCellCU.attributes={NRCellCU_NRCellCU, NRCellCU_cellLocalId, NRCellCU_nRFrequencyRef, NRCellCU_pLMNInfoList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrcellcu",
    types={NRCellCU},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the NRCellCU Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
