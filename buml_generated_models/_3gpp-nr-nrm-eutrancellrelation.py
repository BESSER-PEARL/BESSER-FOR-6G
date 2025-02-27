# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Enumerations
ActionAllowed = Enumeration(name="ActionAllowed")
ActionAllowed_NO = EnumerationLiteral(name="NO", owner=ActionAllowed)
ActionAllowed_YES = EnumerationLiteral(name="YES", owner=ActionAllowed)
ActionAllowed.literals = {ActionAllowed_NO, ActionAllowed_YES}

EnergySavingCoverage = Enumeration(name="EnergySavingCoverage")
EnergySavingCoverage_NO = EnumerationLiteral(name="NO", owner=EnergySavingCoverage)
EnergySavingCoverage_PARTIAL = EnumerationLiteral(name="PARTIAL", owner=EnergySavingCoverage)
EnergySavingCoverage_YES = EnumerationLiteral(name="YES", owner=EnergySavingCoverage)
EnergySavingCoverage.literals = {EnergySavingCoverage_NO, EnergySavingCoverage_PARTIAL, EnergySavingCoverage_YES}

# Classes
EUtranCellRelation = Class(name="EUtranCellRelation")

# EUtranCellRelation class attributes and methods
EUtranCellRelation_adjacentCell: Property = Property(name="adjacentCell", type=StringType)
EUtranCellRelation_cellIndividualOffset: Property = Property(name="cellIndividualOffset", type=StringType)
EUtranCellRelation_isENDCAllowed: Property = Property(name="isENDCAllowed", type=StringType)
EUtranCellRelation_isESCoveredBy: Property = Property(name="isESCoveredBy", type=StringType)
EUtranCellRelation_isHOAllowed: Property = Property(name="isHOAllowed", type=StringType)
EUtranCellRelation_isICICInformationSendAllowed: Property = Property(name="isICICInformationSendAllowed", type=StringType)
EUtranCellRelation_isLBAllowed: Property = Property(name="isLBAllowed", type=StringType)
EUtranCellRelation_isRemoveAllowed: Property = Property(name="isRemoveAllowed", type=StringType)
EUtranCellRelation_qOffset: Property = Property(name="qOffset", type=StringType)
EUtranCellRelation_tCI: Property = Property(name="tCI", type=IntegerType)
EUtranCellRelation.attributes={EUtranCellRelation_adjacentCell, EUtranCellRelation_cellIndividualOffset, EUtranCellRelation_isENDCAllowed, EUtranCellRelation_isESCoveredBy, EUtranCellRelation_isHOAllowed, EUtranCellRelation_isICICInformationSendAllowed, EUtranCellRelation_isLBAllowed, EUtranCellRelation_isRemoveAllowed, EUtranCellRelation_qOffset, EUtranCellRelation_tCI}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-eutrancellrelation",
    types={ActionAllowed, EUtranCellRelation, EnergySavingCoverage},
    associations={},
    generalizations={}
)
