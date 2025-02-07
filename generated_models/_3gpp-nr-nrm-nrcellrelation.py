# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
NRCellRelation = Class(name="NRCellRelation")

# NRCellRelation class attributes and methods
NRCellRelation_nRTCI: Property = Property(name="nRTCI", type=IntegerType)
NRCellRelation_nRFreqRelationRef: Property = Property(name="nRFreqRelationRef", type=types3gpp:DistinguishedName)
NRCellRelation_adjacentNRCellRef: Property = Property(name="adjacentNRCellRef", type=types3gpp:DistinguishedName)
NRCellRelation_isRemoveAllowed: Property = Property(name="isRemoveAllowed", type=BooleanType)
NRCellRelation_isHOAllowed: Property = Property(name="isHOAllowed", type=BooleanType)
NRCellRelation_isESCoveredBy: Property = Property(name="isESCoveredBy", type=EnergySavingCoverage)
NRCellRelation.attributes={NRCellRelation_nRTCI, NRCellRelation_nRFreqRelationRef, NRCellRelation_adjacentNRCellRef, NRCellRelation_isRemoveAllowed, NRCellRelation_isHOAllowed, NRCellRelation_isESCoveredBy}

