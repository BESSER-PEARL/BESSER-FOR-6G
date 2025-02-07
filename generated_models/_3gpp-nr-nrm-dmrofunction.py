# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
DMROFunction = Class(name="DMROFunction")

# DMROFunction class attributes and methods
DMROFunction_maximumDeviationHoTrigger: Property = Property(name="maximumDeviationHoTrigger", type=IntegerType)
DMROFunction_minimumTimeBetweenHoTriggerChange: Property = Property(name="minimumTimeBetweenHoTriggerChange", type=IntegerType)
DMROFunction_tstoreUEcntxt: Property = Property(name="tstoreUEcntxt", type=IntegerType)
DMROFunction_dmroControl: Property = Property(name="dmroControl", type=BooleanType)
DMROFunction.attributes={DMROFunction_maximumDeviationHoTrigger, DMROFunction_minimumTimeBetweenHoTriggerChange, DMROFunction_tstoreUEcntxt, DMROFunction_dmroControl}

