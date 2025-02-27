# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
NRCellRelation = Class(name="NRCellRelation", synonyms=["Represents a neighbour cell relation from a source cell to a target cell, where the target cell is an NRCellCU or ExternalNRCellCU instance."])

# NRCellRelation class attributes and methods
NRCellRelation_adjacentNRCellRef: Property = Property(name="adjacentNRCellRef", type=types3gpp_model.get_type_by_name('DistinguishedName'), synonyms=["Reference to an adjacent NR cell (NRCellCU or ExternalNRCellCU)."])
NRCellRelation_isESCoveredBy: Property = Property(name="isESCoveredBy", type=StringType, synonyms=["Indicates whether the adjacent cell provides no, partial or full coverage for the parent cell instance. Adjacent cells with this attribute equal to FULL are recommended to be considered as candidate cells to take over the coverage when the original cell is about to be changed to energy saving state. All adjacent cells with this property equal to PARTIAL are recommended to be considered as entirety of candidate cells to take over the coverage when the original cell is about to be changed to energy saving state."])
NRCellRelation_isHOAllowed: Property = Property(name="isHOAllowed", type=BooleanType, synonyms=["True if handovers are allowed over this relation."])
NRCellRelation_isRemoveAllowed: Property = Property(name="isRemoveAllowed", type=BooleanType, synonyms=["True if the ANR function in the node is allowed to remove this relation."])
NRCellRelation_nRFreqRelationRef: Property = Property(name="nRFreqRelationRef", type=types3gpp_model.get_type_by_name('DistinguishedName'), synonyms=["Reference to a corresponding NRFreqRelation instance."])
NRCellRelation_nRTCI: Property = Property(name="nRTCI", type=IntegerType, synonyms=["Target NR Cell Identifier. It consists of NR Cell Identifier (NCI) and Physical Cell Identifier of the target NR cell (nRPCI)."])
NRCellRelation.attributes={NRCellRelation_adjacentNRCellRef, NRCellRelation_isESCoveredBy, NRCellRelation_isHOAllowed, NRCellRelation_isRemoveAllowed, NRCellRelation_nRFreqRelationRef, NRCellRelation_nRTCI}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrcellrelation",
    types={NRCellRelation},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the NRCellRelation Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
