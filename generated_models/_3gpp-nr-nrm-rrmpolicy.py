# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
rRMPolicyMember = Class(name="rRMPolicyMember")

# rRMPolicyMember class attributes and methods
RRMPolicy_ = Class(name="RRMPolicy_")

# RRMPolicy_ class attributes and methods
RRMPolicy__resourceType: Property = Property(name="resourceType", type=StringType)
RRMPolicy__rRMPolicyMemberList: Property = Property(name="rRMPolicyMemberList", type=list)
RRMPolicy_.attributes={RRMPolicy__resourceType, RRMPolicy__rRMPolicyMemberList}

RRMPolicyRatio = Class(name="RRMPolicyRatio")

# RRMPolicyRatio class attributes and methods
RRMPolicyRatio_rRMPolicyMaxRatio: Property = Property(name="rRMPolicyMaxRatio", type=IntegerType)
RRMPolicyRatio_rRMPolicyMinRatio: Property = Property(name="rRMPolicyMinRatio", type=IntegerType)
RRMPolicyRatio_rRMPolicyDedicatedRatio: Property = Property(name="rRMPolicyDedicatedRatio", type=IntegerType)
RRMPolicyRatio_RRMPolicyRatio: Property = Property(name="RRMPolicyRatio", type=list)
RRMPolicyRatio.attributes={RRMPolicyRatio_rRMPolicyMaxRatio, RRMPolicyRatio_rRMPolicyMinRatio, RRMPolicyRatio_rRMPolicyDedicatedRatio, RRMPolicyRatio_RRMPolicyRatio}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-rrmpolicy",
    types={rRMPolicyMember, RRMPolicy_, RRMPolicyRatio},
    associations={},
    generalizations={}
)
