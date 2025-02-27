# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalSEPPFunction = Class(name="ExternalSEPPFunction")

# ExternalSEPPFunction class attributes and methods
ExternalSEPPFunction_fqdn: Property = Property(name="fqdn", type=StringType)
ExternalSEPPFunction_sEPPId: Property = Property(name="sEPPId", type=IntegerType)
ExternalSEPPFunction.attributes={ExternalSEPPFunction_fqdn, ExternalSEPPFunction_sEPPId}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-externalseppfunction",
    types={ExternalSEPPFunction},
    associations={},
    generalizations={}
)
