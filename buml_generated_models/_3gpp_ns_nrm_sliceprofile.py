# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)


# Create needed data types
distinguished_name_type = StringType
tac_type = StringType

# Create UE Mobility Level enumeration
ue_mobility_level_enum = Enumeration(
    name="UeMobilityLevel",
    literals=[
        EnumerationLiteral("STATIONARY"),
        EnumerationLiteral("NOMADIC"),
        EnumerationLiteral("RESTRICTED_MOBILITY"),
        EnumerationLiteral("FULLY_MOBILITY")
    ]
)

# Create Resource Sharing Level enumeration
resource_sharing_level_enum = Enumeration(
    name="ResourceSharingLevel",
    literals=[
        EnumerationLiteral("SHARED"),
        EnumerationLiteral("NON_SHARED")
    ]
)

# Define SNssai class
snssai_class = Class(
    name="SNssai",
    attributes=[
        Property(
            name="sst",
            type=IntegerType,
            multiplicity=Multiplicity(1, 1)
        ),
        Property(
            name="sd",
            type=StringType,
            multiplicity=Multiplicity(0, 1)
        )
    ]
)

# Define PLMNId class
plmn_id_class = Class(
    name="PLMNId",
    attributes=[
        Property(
            name="mcc",
            type=StringType,
            multiplicity=Multiplicity(1, 1)
        ),
        Property(
            name="mnc",
            type=StringType,
            multiplicity=Multiplicity(1, 1)
        )
    ]
)

# Define PerfReqGrp class
perf_req_class = Class(
    name="PerfReqGrp",
    attributes=[
        # Performance requirement attributes would go here
        # Adding placeholder as the JSON doesn't detail these
        Property(
            name="perfMetric",
            type=StringType,
            multiplicity=Multiplicity(0, 1)
        )
    ]
)

# Define SliceProfile class
slice_profile_class = Class(
    name="SliceProfile",
    attributes=[
        Property(
            name="sliceProfileId",
            type=distinguished_name_type,
            multiplicity=Multiplicity(1, 1),
            synonyms=["A unique identifier of the property of network slice subnet related requirement"]
        ),
        Property(
            name="maxNumberofUEs",
            type=IntegerType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Maximum number of UEs may simultaneously access the network slice instance"]
        ),
        Property(
            name="latency",
            type=IntegerType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Packet transmission latency through the RAN, CN, and TN part of 5G network"]
        ),
        Property(
            name="uEMobilityLevel",
            type=ue_mobility_level_enum,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Mobility level of UE accessing the network slice instance"]
        ),
        Property(
            name="resourceSharingLevel",
            type=resource_sharing_level_enum,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Whether resources may be shared with another network slice subnet instance(s)"]
        ),
        Property(
            name="sNSSAIList",
            type=snssai_class,
            multiplicity=Multiplicity(1, 1),
            synonyms=["List of S-NSSAIs the managed object is capable of supporting"]
        ),
        Property(
            name="pLMNIdList",
            type=plmn_id_class,
            multiplicity=Multiplicity(1, 6),
            synonyms=["List of PLMN Identifiers (1-6 entries)"]
        ),
        Property(
            name="perfReq",
            type=perf_req_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Performance requirements for the NSI"]
        ),
        Property(
            name="coverageAreaTAList",
            type=tac_type,
            multiplicity=Multiplicity(1, 1),
            synonyms=["List of TrackingAreas where the NSI can be selected"]
        )
    ]
)


# Create domain model
domain_model = DomainModel(
    name="_3gpp-ns-nrm-sliceprofile",
    types={slice_profile_class, snssai_class, plmn_id_class, perf_req_class, ue_mobility_level_enum, resource_sharing_level_enum},
    associations={},
    generalizations={}
)