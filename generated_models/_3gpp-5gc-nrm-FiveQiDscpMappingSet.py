# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
FiveQiDscpMapping = Class(name="FiveQiDscpMapping")

# FiveQiDscpMapping class attributes and methods
FiveQiDscpMapping_dscp: Property = Property(name="dscp", type=IntegerType)
FiveQiDscpMapping.attributes={FiveQiDscpMapping_dscp}

FiveQiDscpMappingSet = Class(name="FiveQiDscpMappingSet")

# FiveQiDscpMappingSet class attributes and methods
FiveQiDscpMappingSet_FiveQiDscpMappingList: Property = Property(name="FiveQiDscpMappingList", type=list)
FiveQiDscpMappingSet.attributes={FiveQiDscpMappingSet_FiveQiDscpMappingList}

FiveQiDscpMappingSetSubtree = Class(name="FiveQiDscpMappingSetSubtree")

# FiveQiDscpMappingSetSubtree class attributes and methods
FiveQiDscpMappingSetSubtree_FiveQiDscpMappingSet: Property = Property(name="FiveQiDscpMappingSet", type=list)
FiveQiDscpMappingSetSubtree.attributes={FiveQiDscpMappingSetSubtree_FiveQiDscpMappingSet}

