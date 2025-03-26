# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Classes
PerfReq = Class(name="PerfReq")

# PerfReq class attributes and methods
PerfReq_activityFactor: Property = Property(name="activityFactor", type=IntegerType, synonyms=["Percentage value of the amount of simultaneous active UEs to the total number of UEs where active means the UEs are exchanging data with the network."])
PerfReq_areaTrafficCapDL: Property = Property(name="areaTrafficCapDL", type=StringType, synonyms=["Area traffic capacity over downlink"])
PerfReq_areaTrafficCapUL: Property = Property(name="areaTrafficCapUL", type=StringType, synonyms=["Area traffic capacity over uplink"])
PerfReq_cSAvailabilityTarget: Property = Property(name="cSAvailabilityTarget", type=FloatType, synonyms=["Reliability uptime target"])
PerfReq_cSReliabilityMeanTime: Property = Property(name="cSReliabilityMeanTime", type=StringType, synonyms=["Mean time between failures"])
PerfReq_expDataRate: Property = Property(name="expDataRate", type=StringType, synonyms=["User experienced data rate"])
PerfReq_expDataRateDL: Property = Property(name="expDataRateDL", type=StringType, synonyms=["User experienced data rate over downlink"])
PerfReq_expDataRateUL: Property = Property(name="expDataRateUL", type=StringType, synonyms=["User experienced data rate over uplink"])
PerfReq_msgSizeByte: Property = Property(name="msgSizeByte", type=StringType, synonyms=["PDU size"])
PerfReq_overallUserDensity: Property = Property(name="overallUserDensity", type=IntegerType, synonyms=["Overall user density"])
PerfReq_survivalTime: Property = Property(name="survivalTime", type=StringType, synonyms=["The time that an application consuming a communication service may continue without an anticipated message"])
PerfReq_transferIntervalTarget: Property = Property(name="transferIntervalTarget", type=StringType, synonyms=["Time difference between two consecutive transfers of application data from an application via the service interface to 3GPP system"])
PerfReq.attributes={PerfReq_activityFactor, PerfReq_areaTrafficCapDL, PerfReq_areaTrafficCapUL, PerfReq_cSAvailabilityTarget, PerfReq_cSReliabilityMeanTime, PerfReq_expDataRate, PerfReq_expDataRateDL, PerfReq_expDataRateUL, PerfReq_msgSizeByte, PerfReq_overallUserDensity, PerfReq_survivalTime, PerfReq_transferIntervalTarget}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-ns-nrm-perfreq",
    types={PerfReq},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["The performance requirements for the NSI in terms of the scenarios defined in the 3GPP TS 22.261, such as experienced data rate, area traffic capacity (density) information of UE density."]
