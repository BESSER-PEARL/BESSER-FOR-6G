# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
AMFRegion = Class(name="AMFRegion")

# AMFRegion class attributes and methods
AMFRegion_aMFRegionId: Property = Property(name="aMFRegionId", type=types3gpp:AmfRegionId)
AMFRegion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AMFRegion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AMFRegion.attributes={AMFRegion_aMFRegionId, AMFRegion_pLMNIdList, AMFRegion_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-amfregion",
    types={AMFRegion},
    associations={},
    generalizations={}
)
