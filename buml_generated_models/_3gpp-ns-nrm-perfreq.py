# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
PerfReq = Class(name="PerfReq")

# PerfReq class attributes and methods
PerfReq_activityFactor: Property = Property(name="activityFactor", type=IntegerType)
PerfReq_areaTrafficCapDL: Property = Property(name="areaTrafficCapDL", type=StringType)
PerfReq_areaTrafficCapUL: Property = Property(name="areaTrafficCapUL", type=StringType)
PerfReq_cSAvailabilityTarget: Property = Property(name="cSAvailabilityTarget", type=FloatType)
PerfReq_cSReliabilityMeanTime: Property = Property(name="cSReliabilityMeanTime", type=StringType)
PerfReq_expDataRate: Property = Property(name="expDataRate", type=StringType)
PerfReq_expDataRateDL: Property = Property(name="expDataRateDL", type=StringType)
PerfReq_expDataRateUL: Property = Property(name="expDataRateUL", type=StringType)
PerfReq_msgSizeByte: Property = Property(name="msgSizeByte", type=StringType)
PerfReq_overallUserDensity: Property = Property(name="overallUserDensity", type=IntegerType)
PerfReq_survivalTime: Property = Property(name="survivalTime", type=StringType)
PerfReq_transferIntervalTarget: Property = Property(name="transferIntervalTarget", type=StringType)
PerfReq.attributes={PerfReq_activityFactor, PerfReq_areaTrafficCapDL, PerfReq_areaTrafficCapUL, PerfReq_cSAvailabilityTarget, PerfReq_cSReliabilityMeanTime, PerfReq_expDataRate, PerfReq_expDataRateDL, PerfReq_expDataRateUL, PerfReq_msgSizeByte, PerfReq_overallUserDensity, PerfReq_survivalTime, PerfReq_transferIntervalTarget}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-ns-nrm-perfreq",
    types={PerfReq},
    associations={},
    generalizations={}
)
