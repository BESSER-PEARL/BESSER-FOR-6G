# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
# from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
# from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Classes
NRCellCU = Class(name="NRCellCU", synonyms=["Represents the information of a cell known by CU."])

# NRCellCU class attributes and methods
NRCellCU_cellLocalId = Property(name="cellLocalId", type=IntegerType, synonyms=["Identifies an NR cell of a gNB. Together with the corresponding gNB identifier it forms the NR Cell Identity (NCI)."])
NRCellCU_pLMNInfoList = Property(name="pLMNInfoList", type=DataType("PLMNInfo"), multiplicity=Multiplicity(1, "*"), synonyms=["List of PLMN information for the cell."])
NRCellCU_nRFrequencyRef = Property(name="nRFrequencyRef", type=StringType, synonyms=["Reference to the NR frequency the cell belongs to."])
NRCellCU_nRSectorCarrierRef = Property(name="nRSectorCarrierRef", type=StringType, synonyms=["Reference to the corresponding NR sector carrier."])
NRCellCU_nRPCI = Property(name="nRPCI", type=IntegerType, synonyms=["The Physical Cell Identity (PCI) of the NR cell."])
NRCellCU_cellState = Property(name="cellState", type=DataType("CellState"), synonyms=["Cell state of the NRCellCU instance."])
NRCellCU.attributes={NRCellCU_cellLocalId, NRCellCU_pLMNInfoList, NRCellCU_nRFrequencyRef, NRCellCU_nRSectorCarrierRef, NRCellCU_nRPCI, NRCellCU_cellState}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrcellcu",
    types={NRCellCU},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the NRCellCU Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
