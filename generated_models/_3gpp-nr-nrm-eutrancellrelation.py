# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
EUtranCellRelation = Class(name="EUtranCellRelation")

# EUtranCellRelation class attributes and methods
EUtranCellRelation_isRemoveAllowed: Property = Property(name="isRemoveAllowed", type=ActionAllowed)
EUtranCellRelation_isHOAllowed: Property = Property(name="isHOAllowed", type=ActionAllowed)
EUtranCellRelation_tCI: Property = Property(name="tCI", type=IntegerType)
EUtranCellRelation_isENDCAllowed: Property = Property(name="isENDCAllowed", type=ActionAllowed)
EUtranCellRelation_isICICInformationSendAllowed: Property = Property(name="isICICInformationSendAllowed", type=ActionAllowed)
EUtranCellRelation_isLBAllowed: Property = Property(name="isLBAllowed", type=ActionAllowed)
EUtranCellRelation_isESCoveredBy: Property = Property(name="isESCoveredBy", type=EnergySavingCoverage)
EUtranCellRelation_qOffset: Property = Property(name="qOffset", type=types3gpp:QOffsetRange)
EUtranCellRelation_cellIndividualOffset: Property = Property(name="cellIndividualOffset", type=types3gpp:QOffsetRange)
EUtranCellRelation_adjacentCell: Property = Property(name="adjacentCell", type=StringType)
EUtranCellRelation.attributes={EUtranCellRelation_isRemoveAllowed, EUtranCellRelation_isHOAllowed, EUtranCellRelation_tCI, EUtranCellRelation_isENDCAllowed, EUtranCellRelation_isICICInformationSendAllowed, EUtranCellRelation_isLBAllowed, EUtranCellRelation_isESCoveredBy, EUtranCellRelation_qOffset, EUtranCellRelation_cellIndividualOffset, EUtranCellRelation_adjacentCell}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-eutrancellrelation",
    types={EUtranCellRelation},
    associations={},
    generalizations={}
)
