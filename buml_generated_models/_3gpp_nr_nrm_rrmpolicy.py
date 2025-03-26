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
RRMPolicyRatio = Class(name="RRMPolicyRatio", synonyms=["Represents the RRMPolicyRatio concrete IOC."])

# RRMPolicyRatio class attributes and methods
RRMPolicyRatio_RRMPolicyRatio: Property = Property(name="RRMPolicyRatio", type=DataType('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["The RRMPolicyRatio IOC is one realization of a RRMPolicy_ IOC, see the inheritance in Figure 4.2.1.2-1. This RRM framework allows adding new policies, both standardized (like RRMPolicyRatio) or as vendor specific, by inheriting from the abstract RRMPolicy_ IOC. For details see subclause 4.3.36."])
RRMPolicyRatio_rRMPolicyDedicatedRatio: Property = Property(name="rRMPolicyDedicatedRatio", type=IntegerType, synonyms=["This attribute specifies the percentage of radio resource that dedicatedly used by the associated rRMPolicyMemberList. The sum of the rRMPolicyDeidctaedRatio values assigned to all RRMPolicyRatio(s) name-contained by same ManagedEntity shall be less or equal 100."])
RRMPolicyRatio_rRMPolicyMaxRatio: Property = Property(name="rRMPolicyMaxRatio", type=IntegerType, synonyms=["This attribute specifies the maximum percentage of radio resource that can be used by the associated rRMPolicyMemberList. The maximum percentage of radio resource include at least one of the shared resources, prioritized resources and dedicated resources. The sum of the rRMPolicyMaxRatio values assigned to all RRMPolicyRatio(s) name-contained by same ManagedEntity can be greater that 100."])
RRMPolicyRatio_rRMPolicyMinRatio: Property = Property(name="rRMPolicyMinRatio", type=IntegerType, synonyms=["This attribute specifies the minimum percentage of radio resources that can be used by the associated rRMPolicyMemberList. The minimum percentage of radio resources including at least one of prioritized resources and dedicated resources. The sum of the rRMPolicyMinRatio values assigned to all RRM PolicyRatio(s) name-contained by same ManagedEntity shall be less or equal 100."])
RRMPolicyRatio.attributes={RRMPolicyRatio_RRMPolicyRatio, RRMPolicyRatio_rRMPolicyDedicatedRatio, RRMPolicyRatio_rRMPolicyMaxRatio, RRMPolicyRatio_rRMPolicyMinRatio}

RRMPolicy_ = Class(name="RRMPolicy_", synonyms=["This IOC represents the properties of an abstract RRMPolicy . The RRMPolicy_ IOC needs to be subclassed to be instantiated. It defines two attributes apart from those inherited from Top IOC, the resourceType attribute defines type of resource (PRB, RRC connected users, DRB usage etc.) and the rRMPolicyMemberList attribute defines the RRMPolicyMember(s)that are subject to this policy. An RRM resource (defined in resourceType attribute) is located in NRCellDU, NRCellCU, GNBDUFunction, GNBCUCPFunction or in GNBCUUPFunction. The RRMPolicyRatio IOC is one realization of a RRMPolicy_ IOC. This RRM framework allows adding new policies, both standardized (like RRMPolicyRatio) or as vendor specific, by inheriting from the abstract RRMPolicy_ IOC."])

# RRMPolicy_ class attributes and methods
RRMPolicy__rRMPolicyMemberList: Property = Property(name="rRMPolicyMemberList", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["It represents the list of RRMPolicyMember (s) that the managed object is supporting. A RRMPolicyMember <<dataType>> include the PLMNId <<dataType>> and S-NSSAI <<dataType>>."])
RRMPolicy__resourceType: Property = Property(name="resourceType", type=StringType, synonyms=["The resourceType attribute defines type of resource (PRB, RRC connected users, DRB usage etc.) that is subject to policy. Valid values are 'PRB', 'RRC' or 'DRB'"])
RRMPolicy_.attributes={RRMPolicy__rRMPolicyMemberList, RRMPolicy__resourceType}

rRMPolicyMember = Class(name="rRMPolicyMember", synonyms=["This data type represents an RRM Policy member that will be part of a rRMPolicyMemberList. A RRMPolicyMember is defined by its pLMNId and sNSSAI (S-NSSAI). The members in a rRMPolicyMemberList are assigned a specific amount of RRM resources based on settings in RRMPolicy."])

# rRMPolicyMember class attributes and methods
# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-rrmpolicy",
    types={RRMPolicyRatio, RRMPolicy_, rRMPolicyMember},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the RRMPolicy abstract class that is part of the NR Network Resource Model (NRM)."]
