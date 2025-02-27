# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Enumerations
BwpContext = Enumeration(name="BwpContext")
BwpContext_DL = EnumerationLiteral(name="DL", owner=BwpContext)
BwpContext_SUL = EnumerationLiteral(name="SUL", owner=BwpContext)
BwpContext_UL = EnumerationLiteral(name="UL", owner=BwpContext)
BwpContext.literals = {BwpContext_DL, BwpContext_SUL, BwpContext_UL}

CyclicPrefix = Enumeration(name="CyclicPrefix")
CyclicPrefix_EXTENDED = EnumerationLiteral(name="EXTENDED", owner=CyclicPrefix)
CyclicPrefix_NORMAL = EnumerationLiteral(name="NORMAL", owner=CyclicPrefix)
CyclicPrefix.literals = {CyclicPrefix_EXTENDED, CyclicPrefix_NORMAL}

IsInitialBwp = Enumeration(name="IsInitialBwp")
IsInitialBwp_INITIAL = EnumerationLiteral(name="INITIAL", owner=IsInitialBwp)
IsInitialBwp_OTHER = EnumerationLiteral(name="OTHER", owner=IsInitialBwp)
IsInitialBwp.literals = {IsInitialBwp_INITIAL, IsInitialBwp_OTHER}

# Classes
BWP = Class(name="BWP", synonyms=["Represents a bandwidth part (BWP)."])

# BWP class attributes and methods
BWP_bwpContext: Property = Property(name="bwpContext", type=StringType, synonyms=["Identifies whether the object is used for downlink, uplink or supplementary uplink."])
BWP_cyclicPrefix: Property = Property(name="cyclicPrefix", type=StringType, synonyms=["Cyclic prefix, which may be normal or extended."])
BWP_isInitialBwp: Property = Property(name="isInitialBwp", type=StringType, synonyms=["Identifies whether the object is used for initial or other BWP."])
BWP_numberOfRBs: Property = Property(name="numberOfRBs", type=IntegerType, synonyms=["Number of physical resource blocks for a BWP."])
BWP_startRB: Property = Property(name="startRB", type=IntegerType, synonyms=["Offset in common resource blocks to common resource block 0 for the applicable subcarrier spacing for a BWP."])
BWP_subCarrierSpacing: Property = Property(name="subCarrierSpacing", type=IntegerType, synonyms=["Subcarrier spacing configuration for a BWP."])
BWP.attributes={BWP_bwpContext, BWP_cyclicPrefix, BWP_isInitialBwp, BWP_numberOfRBs, BWP_startRB, BWP_subCarrierSpacing}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-bwp",
    types={BWP, BwpContext, CyclicPrefix, IsInitialBwp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the BWP Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
