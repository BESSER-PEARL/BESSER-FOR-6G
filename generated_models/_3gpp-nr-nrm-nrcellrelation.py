# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
NRCellRelation = Class(name="NRCellRelation")

# NRCellRelation class attributes and methods
NRCellRelation_nRTCI: Property = Property(name="nRTCI", type=IntegerType)
NRCellRelation_nRFreqRelationRef: Property = Property(name="nRFreqRelationRef", type=StringType)
NRCellRelation_adjacentNRCellRef: Property = Property(name="adjacentNRCellRef", type=StringType)
NRCellRelation_isRemoveAllowed: Property = Property(name="isRemoveAllowed", type=BooleanType)
NRCellRelation_isHOAllowed: Property = Property(name="isHOAllowed", type=BooleanType)
NRCellRelation_isESCoveredBy: Property = Property(name="isESCoveredBy", type=EnergySavingCoverage)
NRCellRelation.attributes={NRCellRelation_nRTCI, NRCellRelation_nRFreqRelationRef, NRCellRelation_adjacentNRCellRef, NRCellRelation_isRemoveAllowed, NRCellRelation_isHOAllowed, NRCellRelation_isESCoveredBy}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrcellrelation",
    types={NRCellRelation},
    associations={},
    generalizations={}
)
