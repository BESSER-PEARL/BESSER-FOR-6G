# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NRCellRelation = Class(name="NRCellRelation")

# NRCellRelation class attributes and methods
NRCellRelation_adjacentNRCellRef: Property = Property(name="adjacentNRCellRef", type=StringType)
NRCellRelation_isESCoveredBy: Property = Property(name="isESCoveredBy", type=StringType)
NRCellRelation_isHOAllowed: Property = Property(name="isHOAllowed", type=BooleanType)
NRCellRelation_isRemoveAllowed: Property = Property(name="isRemoveAllowed", type=BooleanType)
NRCellRelation_nRFreqRelationRef: Property = Property(name="nRFreqRelationRef", type=StringType)
NRCellRelation_nRTCI: Property = Property(name="nRTCI", type=IntegerType)
NRCellRelation.attributes={NRCellRelation_adjacentNRCellRef, NRCellRelation_isESCoveredBy, NRCellRelation_isHOAllowed, NRCellRelation_isRemoveAllowed, NRCellRelation_nRFreqRelationRef, NRCellRelation_nRTCI}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrcellrelation",
    types={NRCellRelation},
    associations={},
    generalizations={}
)
