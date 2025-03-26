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
decimal64_type = FloatType

# Create enumerations
category_enum = Enumeration(
    name="Category-enum",
    literals=[
        EnumerationLiteral("character"),
        EnumerationLiteral("scalability")
    ]
)

tagging_enum = Enumeration(
    name="Tagging-enum",
    literals=[
        EnumerationLiteral("performance"),
        EnumerationLiteral("function"),
        EnumerationLiteral("operation")
    ]
)

exposure_enum = Enumeration(
    name="Exposure-enum",
    literals=[
        EnumerationLiteral("API"),
        EnumerationLiteral("KPI")
    ]
)

support_enum = Enumeration(
    name="Support-enum",
    literals=[
        EnumerationLiteral("NOT_SUPPORTED"),
        EnumerationLiteral("SUPPORTED")
    ]
)

v2x_mode_enum = Enumeration(
    name="V2XMode-enum",
    literals=[
        EnumerationLiteral("NOT_SUPPORTED"),
        EnumerationLiteral("SUPPORTED_BY_NR")
    ]
)

ue_mobility_level_enum = Enumeration(
    name="UeMobilityLevel",
    literals=[
        EnumerationLiteral("STATIONARY"),
        EnumerationLiteral("NOMADIC"),
        EnumerationLiteral("RESTRICTED_MOBILITY"),
        EnumerationLiteral("FULLY_MOBILITY")
    ]
)

resource_sharing_level_enum = Enumeration(
    name="ResourceSharingLevel",
    literals=[
        EnumerationLiteral("SHARED"),
        EnumerationLiteral("NON_SHARED")
    ]
)

# Define classes
service_attr_com_class = Class(
    name="ServAttrComGrp",
    attributes=[
        Property(
            name="category",
            type=category_enum,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Category of a service requirement/attribute of GST"]
        ),
        Property(
            name="exposure",
            type=exposure_enum,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Exposure mode of a service requirement/attribute of GST"]
        ),
        Property(
            name="tagging",
            type=tagging_enum,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Tagging of a service requirement/attribute of GST in character category"]
        )
    ]
)

dl_thpt_class = Class(
    name="DLThptGrp",
    attributes=[
        Property(
            name="servAttrCom",
            type=service_attr_com_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Common attributes of service requirement related attributes"]
        ),
        Property(
            name="guaThpt",
            type=IntegerType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["The guaranteed data rate in kbits/s"]
        ),
        Property(
            name="maxThpt",
            type=IntegerType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["The maximum data rate in kbits/s"]
        )
    ]
)

snssai_class = Class(
    name="SNssai",
    attributes=[
        Property(
            name="sst",
            type=IntegerType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Slice/Service type"]
        ),
        Property(
            name="sd",
            type=StringType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Slice Differentiator"]
        )
    ]
)

plmn_id_class = Class(
    name="PLMNId",
    attributes=[
        Property(
            name="mcc",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Mobile Country Code"]
        ),
        Property(
            name="mnc",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Mobile Network Code"]
        )
    ]
)

delay_tolerance_class = Class(
    name="DelayTolerance",
    attributes=[
        Property(
            name="support",
            type=support_enum,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Whether network slice supports service delivery flexibility"]
        ),
        Property(
            name="servAttrCom",
            type=service_attr_com_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Common attributes of service requirement related attributes"]
        )
    ]
)

deterministic_comm_class = Class(
    name="DeterministicComm",
    attributes=[
        Property(
            name="availability",
            type=support_enum,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Whether deterministic communication is available"]
        ),
        Property(
            name="periodicityList",
            type=StringType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["List of periodicities"]
        ),
        Property(
            name="servAttrCom",
            type=service_attr_com_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Common attributes of service requirement related attributes"]
        )
    ]
)

max_pkt_size_class = Class(
    name="MaxPktSize",
    attributes=[
        Property(
            name="maxSize",
            type=IntegerType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Maximum packet size in bytes"]
        ),
        Property(
            name="servAttrCom",
            type=service_attr_com_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Common attributes of service requirement related attributes"]
        )
    ]
)

max_number_of_pdu_sessions_class = Class(
    name="MaxNumberofPDUSessions",
    attributes=[
        Property(
            name="nOofPDUSessions",
            type=IntegerType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Number of PDU sessions"]
        ),
        Property(
            name="servAttrCom",
            type=service_attr_com_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Common attributes of service requirement related attributes"]
        )
    ]
)

kpi_monitoring_class = Class(
    name="KPIMonitoring",
    attributes=[
        Property(
            name="kPIList",
            type=StringType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Name list of KQIs and KPIs available for performance monitoring"]
        ),
        Property(
            name="servAttrCom",
            type=service_attr_com_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Common attributes of service requirement related attributes"]
        )
    ]
)

user_mgmt_open_class = Class(
    name="UserMgmtOpen",
    attributes=[
        Property(
            name="support",
            type=support_enum,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Whether network slice supports user management capability"]
        ),
        Property(
            name="servAttrCom",
            type=service_attr_com_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Common attributes of service requirement related attributes"]
        )
    ]
)

v2x_comm_models_class = Class(
    name="V2XCommModels",
    attributes=[
        Property(
            name="v2XMode",
            type=v2x_mode_enum,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Whether V2X communication mode is supported"]
        ),
        Property(
            name="servAttrCom",
            type=service_attr_com_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Common attributes of service requirement related attributes"]
        )
    ]
)

term_density_class = Class(
    name="TermDensity",
    attributes=[
        Property(
            name="density",
            type=IntegerType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Overall user density over the coverage area in users/km2"]
        ),
        Property(
            name="servAttrCom",
            type=service_attr_com_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Common attributes of service requirement related attributes"]
        )
    ]
)

nb_iot_class = Class(
    name="NBIoT",
    attributes=[
        Property(
            name="support",
            type=support_enum,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Whether NB-IoT is supported in the RAN"]
        ),
        Property(
            name="servAttrCom",
            type=service_attr_com_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Common attributes of service requirement related attributes"]
        )
    ]
)

# Define ServiceProfile class
service_profile_class = Class(
    name="ServiceProfile",
    attributes=[
        Property(
            name="serviceProfileId",
            type=distinguished_name_type,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Service profile identifier"]
        ),
        Property(
            name="maxNumberofUEs",
            type=IntegerType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Maximum number of UEs that may simultaneously access the network slice instance"]
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
            synonyms=["Whether resources may be shared with another network slice instance(s)"]
        ),
        Property(
            name="sST",
            type=IntegerType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Slice/service type"]
        ),
        Property(
            name="availability",
            type=decimal64_type,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Availability requirement as percentage"]
        ),
        Property(
            name="activityFactor",
            type=decimal64_type,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Percentage of simultaneous active UEs to total UEs"]
        ),
        Property(
            name="uESpeed",
            type=IntegerType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Maximum speed supported by the network slice in km/hour"]
        ),
        Property(
            name="jitter",
            type=IntegerType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Deviation from desired value when assessing time parameters"]
        ),
        Property(
            name="survivalTime",
            type=StringType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Time an application may continue without an anticipated message"]
        ),
        Property(
            name="reliability",
            type=StringType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Percentage of successfully delivered network layer packets"]
        ),
        Property(
            name="maxDLDataVolume",
            type=StringType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Maximum downlink data volume"]
        ),
        Property(
            name="maxULDataVolume",
            type=StringType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Maximum uplink data volume"]
        ),
        Property(
            name="sNSSAIList",
            type=snssai_class,
            multiplicity=Multiplicity(1, 1),
            synonyms=["List of S-NSSAIs to be supported"]
        ),
        Property(
            name="pLMNIdList",
            type=plmn_id_class,
            multiplicity=Multiplicity(1, 1),
            synonyms=["List of PLMN IDs"]
        ),
        Property(
            name="delayTolerance",
            type=delay_tolerance_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["attributes of service delivery flexibility"]
        ),
        Property(
            name="deterministicComm",
            type=deterministic_comm_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["attributes of deterministic communication for periodic traffic"]
        ),
        Property(
            name="dLThptPerSlice",
            type=dl_thpt_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Downlink throughput for the entire slice"]
        ),
        Property(
            name="dLThptPerUE",
            type=dl_thpt_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Downlink throughput per UE"]
        ),
        Property(
            name="uLThptPerSlic",
            type=dl_thpt_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Uplink throughput for the entire slice"]
        ),
        Property(
            name="uLThptPerUE",
            type=dl_thpt_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Uplink throughput per UE"]
        ),
        Property(
            name="maxPktSize",
            type=max_pkt_size_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Maximum packet size supported"]
        ),
        Property(
            name="maxNumberofPDUSessions",
            type=max_number_of_pdu_sessions_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Maximum number of concurrent PDU sessions"]
        ),
        Property(
            name="kPIMonitoring",
            type=kpi_monitoring_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Performance monitoring"]
        ),
        Property(
            name="userMgmtOpen",
            type=user_mgmt_open_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["User management capability support"]
        ),
        Property(
            name="v2XCommModels",
            type=v2x_comm_models_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["V2X communication mode support"]
        ),
        Property(
            name="termDensity",
            type=term_density_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Overall user density over coverage area"]
        ),
        Property(
            name="nBIoT",
            type=nb_iot_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["NB-IoT support in the RAN"]
        ),
        Property(
            name="coverageArea",
            type=tac_type,
            multiplicity=Multiplicity(1, 1),
            synonyms=["List of TrackingAreas where the NSI can be selected"]
        )
    ]
)

# Create domain model
domain_model = DomainModel(
    name="_3gpp-ns-nrm-serviceprofile",
    types={category_enum, tagging_enum, exposure_enum, support_enum, v2x_mode_enum, ue_mobility_level_enum, resource_sharing_level_enum, service_attr_com_class, dl_thpt_class, snssai_class, plmn_id_class, delay_tolerance_class, deterministic_comm_class, max_pkt_size_class, max_number_of_pdu_sessions_class, kpi_monitoring_class, user_mgmt_open_class, v2x_comm_models_class, term_density_class, nb_iot_class, service_profile_class},
    associations={},
    generalizations={}
)