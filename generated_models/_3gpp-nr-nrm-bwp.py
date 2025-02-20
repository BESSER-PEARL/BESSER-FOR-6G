# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
BWP = Class(name="BWP")

# BWP class attributes and methods
BWP_bwpContext: Property = Property(name="bwpContext", type=BwpContext)
BWP_isInitialBwp: Property = Property(name="isInitialBwp", type=IsInitialBwp)
BWP_subCarrierSpacing: Property = Property(name="subCarrierSpacing", type=IntegerType)
BWP_cyclicPrefix: Property = Property(name="cyclicPrefix", type=CyclicPrefix)
BWP_startRB: Property = Property(name="startRB", type=IntegerType)
BWP_numberOfRBs: Property = Property(name="numberOfRBs", type=IntegerType)
BWP.attributes={BWP_bwpContext, BWP_isInitialBwp, BWP_subCarrierSpacing, BWP_cyclicPrefix, BWP_startRB, BWP_numberOfRBs}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-bwp",
    types={BWP},
    associations={},
    generalizations={}
)
