# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Classes
DMROFunction = Class(name="DMROFunction", synonyms=["Represents the DMROFunction IOC."])

# DMROFunction class attributes and methods
DMROFunction_dmroControl: Property = Property(name="dmroControl", type=BooleanType, synonyms=["This attribute determines whether the MRO function is enabled or disabled."])
DMROFunction_maximumDeviationHoTrigger: Property = Property(name="maximumDeviationHoTrigger", type=IntegerType, synonyms=["This parameter defines the maximum allowed absolute deviation of the Handover Trigger, from the default point of operation."])
DMROFunction_minimumTimeBetweenHoTriggerChange: Property = Property(name="minimumTimeBetweenHoTriggerChange", type=IntegerType, synonyms=["This parameter defines the minimum allowed time interval between two Handover Trigger change performed by MRO. This is used to control the stability and convergence of the algorithm."])
DMROFunction_tstoreUEcntxt: Property = Property(name="tstoreUEcntxt", type=IntegerType, synonyms=["The timer used for detection of too early HO, too late HO and HO to wrong cell."])
DMROFunction.attributes={DMROFunction_dmroControl, DMROFunction_maximumDeviationHoTrigger, DMROFunction_minimumTimeBetweenHoTriggerChange, DMROFunction_tstoreUEcntxt}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-dmrofunction",
    types={DMROFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the DMROFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
