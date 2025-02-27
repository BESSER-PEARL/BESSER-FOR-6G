# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
DMROFunction = Class(name="DMROFunction")

# DMROFunction class attributes and methods
DMROFunction_dmroControl: Property = Property(name="dmroControl", type=BooleanType)
DMROFunction_maximumDeviationHoTrigger: Property = Property(name="maximumDeviationHoTrigger", type=IntegerType)
DMROFunction_minimumTimeBetweenHoTriggerChange: Property = Property(name="minimumTimeBetweenHoTriggerChange", type=IntegerType)
DMROFunction_tstoreUEcntxt: Property = Property(name="tstoreUEcntxt", type=IntegerType)
DMROFunction.attributes={DMROFunction_dmroControl, DMROFunction_maximumDeviationHoTrigger, DMROFunction_minimumTimeBetweenHoTriggerChange, DMROFunction_tstoreUEcntxt}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-dmrofunction",
    types={DMROFunction},
    associations={},
    generalizations={}
)
