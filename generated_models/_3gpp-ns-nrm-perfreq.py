# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
PerfReq = Class(name="PerfReq")

# PerfReq class attributes and methods
PerfReq_expDataRateDL: Property = Property(name="expDataRateDL", type=data-rate)
PerfReq_expDataRateUL: Property = Property(name="expDataRateUL", type=data-rate)
PerfReq_areaTrafficCapDL: Property = Property(name="areaTrafficCapDL", type=data-rate)
PerfReq_areaTrafficCapUL: Property = Property(name="areaTrafficCapUL", type=data-rate)
PerfReq_overallUserDensity: Property = Property(name="overallUserDensity", type=IntegerType)
PerfReq_activityFactor: Property = Property(name="activityFactor", type=integer-percentage)
PerfReq_cSAvailabilityTarget: Property = Property(name="cSAvailabilityTarget", type=FloatType)
PerfReq_cSReliabilityMeanTime: Property = Property(name="cSReliabilityMeanTime", type=reliability-string)
PerfReq_expDataRate: Property = Property(name="expDataRate", type=data-rate)
PerfReq_msgSizeByte: Property = Property(name="msgSizeByte", type=message-size-string)
PerfReq_transferIntervalTarget: Property = Property(name="transferIntervalTarget", type=transfer-interval-string)
PerfReq_survivalTime: Property = Property(name="survivalTime", type=survival-time-string)
PerfReq.attributes={PerfReq_expDataRateDL, PerfReq_expDataRateUL, PerfReq_areaTrafficCapDL, PerfReq_areaTrafficCapUL, PerfReq_overallUserDensity, PerfReq_activityFactor, PerfReq_cSAvailabilityTarget, PerfReq_cSReliabilityMeanTime, PerfReq_expDataRate, PerfReq_msgSizeByte, PerfReq_transferIntervalTarget, PerfReq_survivalTime}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-ns-nrm-perfreq",
    types={PerfReq},
    associations={},
    generalizations={}
)
