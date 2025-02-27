# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NRCellRelation = Class(name="NRCellRelation", synonyms=["Represents a neighbour cell relation from a source cell to a target cell, where the target cell is an NRCellCU or ExternalNRCellCU instance."])

# NRCellRelation class attributes and methods
NRCellRelation_adjacentNRCellRef: Property = Property(name="adjacentNRCellRef", type=StringType, synonyms=["Reference to an adjacent NR cell (NRCellCU or ExternalNRCellCU)."])
NRCellRelation_isESCoveredBy: Property = Property(name="isESCoveredBy", type=StringType, synonyms=["Indicates whether the adjacent cell provides no, partial or full coverage for the parent cell instance. Adjacent cells with this attribute equal to FULL are recommended to be considered as candidate cells to take over the coverage when the original cell is about to be changed to energy saving state. All adjacent cells with this property equal to PARTIAL are recommended to be considered as entirety of candidate cells to take over the coverage when the original cell is about to be changed to energy saving state."])
NRCellRelation_isHOAllowed: Property = Property(name="isHOAllowed", type=BooleanType, synonyms=["True if handovers are allowed over this relation."])
NRCellRelation_isRemoveAllowed: Property = Property(name="isRemoveAllowed", type=BooleanType, synonyms=["True if the ANR function in the node is allowed to remove this relation."])
NRCellRelation_nRFreqRelationRef: Property = Property(name="nRFreqRelationRef", type=StringType, synonyms=["Reference to a corresponding NRFreqRelation instance."])
NRCellRelation_nRTCI: Property = Property(name="nRTCI", type=IntegerType, synonyms=["Target NR Cell Identifier. It consists of NR Cell Identifier (NCI) and Physical Cell Identifier of the target NR cell (nRPCI)."])
NRCellRelation.attributes={NRCellRelation_adjacentNRCellRef, NRCellRelation_isESCoveredBy, NRCellRelation_isHOAllowed, NRCellRelation_isRemoveAllowed, NRCellRelation_nRFreqRelationRef, NRCellRelation_nRTCI}

NRCellRelationGrp = Class(name="NRCellRelationGrp", synonyms=["Represents the NRCellRelation IOC."])

# NRCellRelationGrp class attributes and methods
NRCellRelationGrp_adjacentNRCellRef: Property = Property(name="adjacentNRCellRef", type=StringType, synonyms=["Reference to an adjacent NR cell (NRCellCU or ExternalNRCellCU)."])
NRCellRelationGrp_isESCoveredBy: Property = Property(name="isESCoveredBy", type=StringType, synonyms=["Indicates whether the adjacent cell provides no, partial or full coverage for the parent cell instance. Adjacent cells with this attribute equal to FULL are recommended to be considered as candidate cells to take over the coverage when the original cell is about to be changed to energy saving state. All adjacent cells with this property equal to PARTIAL are recommended to be considered as entirety of candidate cells to take over the coverage when the original cell is about to be changed to energy saving state."])
NRCellRelationGrp_isHOAllowed: Property = Property(name="isHOAllowed", type=BooleanType, synonyms=["True if handovers are allowed over this relation."])
NRCellRelationGrp_isRemoveAllowed: Property = Property(name="isRemoveAllowed", type=BooleanType, synonyms=["True if the ANR function in the node is allowed to remove this relation."])
NRCellRelationGrp_nRFreqRelationRef: Property = Property(name="nRFreqRelationRef", type=StringType, synonyms=["Reference to a corresponding NRFreqRelation instance."])
NRCellRelationGrp_nRTCI: Property = Property(name="nRTCI", type=IntegerType, synonyms=["Target NR Cell Identifier. It consists of NR Cell Identifier (NCI) and Physical Cell Identifier of the target NR cell (nRPCI)."])
NRCellRelationGrp.attributes={NRCellRelationGrp_adjacentNRCellRef, NRCellRelationGrp_isESCoveredBy, NRCellRelationGrp_isHOAllowed, NRCellRelationGrp_isRemoveAllowed, NRCellRelationGrp_nRFreqRelationRef, NRCellRelationGrp_nRTCI}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrcellrelation",
    types={NRCellRelation, NRCellRelationGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the NRCellRelation Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
