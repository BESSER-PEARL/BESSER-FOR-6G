# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model

# Classes
FiveQiDscpMapping = Class(name="FiveQiDscpMapping")

# FiveQiDscpMapping class attributes and methods
FiveQiDscpMapping_dscp: Property = Property(name="dscp", type=IntegerType)
FiveQiDscpMapping.attributes={FiveQiDscpMapping_dscp}

FiveQiDscpMappingSet = Class(name="FiveQiDscpMappingSet", synonyms=["Represents the FiveQiDscpMappingSet IOC."])

# FiveQiDscpMappingSet class attributes and methods
FiveQiDscpMappingSet_FiveQiDscpMappingList: Property = Property(name="FiveQiDscpMappingList", type=list, multiplicity=Multiplicity(0, "*"))
FiveQiDscpMappingSet.attributes={FiveQiDscpMappingSet_FiveQiDscpMappingList}

FiveQiDscpMappingSetSubtree = Class(name="FiveQiDscpMappingSetSubtree")

# FiveQiDscpMappingSetSubtree class attributes and methods
FiveQiDscpMappingSetSubtree_FiveQiDscpMappingSet: Property = Property(name="FiveQiDscpMappingSet", type=DataType('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["Specifies the mapping between 5QIs and DSCPs."])
FiveQiDscpMappingSetSubtree.attributes={FiveQiDscpMappingSetSubtree_FiveQiDscpMappingSet}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-FiveQiDscpMappingSet",
    types={FiveQiDscpMapping, FiveQiDscpMappingSet, FiveQiDscpMappingSetSubtree},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the set of mapping between 5QIs and DSCP."]
