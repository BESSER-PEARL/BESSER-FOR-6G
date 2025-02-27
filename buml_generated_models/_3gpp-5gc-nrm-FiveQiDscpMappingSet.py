# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

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

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-FiveQiDscpMappingSet",
    types={FiveQiDscpMapping, FiveQiDscpMappingSet, FiveQiDscpMappingSetSubtree},
    associations={},
    generalizations={}
)
