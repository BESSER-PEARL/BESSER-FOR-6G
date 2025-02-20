# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Enumerations
SEPPType = Enumeration(name="SEPPType")
SEPPType_CSEPP = EnumerationLiteral(name="CSEPP", owner=SEPPType)
SEPPType_PSEPP = EnumerationLiteral(name="PSEPP", owner=SEPPType)
SEPPType.literals = {SEPPType_CSEPP, SEPPType_PSEPP}

# Classes
SEPPFunction = Class(name="SEPPFunction")

# SEPPFunction class attributes and methods
SEPPFunction_fqdn: Property = Property(name="fqdn", type=StringType)
SEPPFunction_sEPPId: Property = Property(name="sEPPId", type=IntegerType)
SEPPFunction_sEPPType: Property = Property(name="sEPPType", type=StringType)
SEPPFunction.attributes={SEPPFunction_fqdn, SEPPFunction_sEPPId, SEPPFunction_sEPPType}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-seppfunction",
    types={SEPPFunction, SEPPType},
    associations={},
    generalizations={}
)
