# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
CommonBeamformingFunction = Class(name="CommonBeamformingFunction")

# CommonBeamformingFunction class attributes and methods
CommonBeamformingFunction_coverageShape: Property = Property(name="coverageShape", type=IntegerType)
CommonBeamformingFunction_digitalAzimuth: Property = Property(name="digitalAzimuth", type=IntegerType)
CommonBeamformingFunction_digitalTilt: Property = Property(name="digitalTilt", type=IntegerType)
CommonBeamformingFunction.attributes={CommonBeamformingFunction_coverageShape, CommonBeamformingFunction_digitalAzimuth, CommonBeamformingFunction_digitalTilt}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-commonbeamformingfunction",
    types={CommonBeamformingFunction},
    associations={},
    generalizations={}
)
