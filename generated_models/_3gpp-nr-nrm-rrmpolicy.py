# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
RRMPolicyRatio = Class(name="RRMPolicyRatio")

# RRMPolicyRatio class attributes and methods
RRMPolicyRatio_RRMPolicyRatio: Property = Property(name="RRMPolicyRatio", type=list)
RRMPolicyRatio_rRMPolicyDedicatedRatio: Property = Property(name="rRMPolicyDedicatedRatio", type=IntegerType)
RRMPolicyRatio_rRMPolicyMaxRatio: Property = Property(name="rRMPolicyMaxRatio", type=IntegerType)
RRMPolicyRatio_rRMPolicyMinRatio: Property = Property(name="rRMPolicyMinRatio", type=IntegerType)
RRMPolicyRatio.attributes={RRMPolicyRatio_RRMPolicyRatio, RRMPolicyRatio_rRMPolicyDedicatedRatio, RRMPolicyRatio_rRMPolicyMaxRatio, RRMPolicyRatio_rRMPolicyMinRatio}

RRMPolicy_ = Class(name="RRMPolicy_")

# RRMPolicy_ class attributes and methods
RRMPolicy__rRMPolicyMemberList: Property = Property(name="rRMPolicyMemberList", type=list)
RRMPolicy__resourceType: Property = Property(name="resourceType", type=StringType)
RRMPolicy_.attributes={RRMPolicy__rRMPolicyMemberList, RRMPolicy__resourceType}

rRMPolicyMember = Class(name="rRMPolicyMember")

# rRMPolicyMember class attributes and methods
# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-rrmpolicy",
    types={RRMPolicyRatio, RRMPolicy_, rRMPolicyMember},
    associations={},
    generalizations={}
)
