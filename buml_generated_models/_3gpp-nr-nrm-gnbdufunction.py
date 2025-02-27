# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
GNBDUFunction = Class(name="GNBDUFunction")

# GNBDUFunction class attributes and methods
GNBDUFunction_aggressorSetID: Property = Property(name="aggressorSetID", type=IntegerType)
GNBDUFunction_gNBDUId: Property = Property(name="gNBDUId", type=IntegerType)
GNBDUFunction_gNBDUName: Property = Property(name="gNBDUName", type=StringType)
GNBDUFunction_gNBId: Property = Property(name="gNBId", type=IntegerType)
GNBDUFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType)
GNBDUFunction_victimSetID: Property = Property(name="victimSetID", type=IntegerType)
GNBDUFunction.attributes={GNBDUFunction_aggressorSetID, GNBDUFunction_gNBDUId, GNBDUFunction_gNBDUName, GNBDUFunction_gNBId, GNBDUFunction_gNBIdLength, GNBDUFunction_victimSetID}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-gnbdufunction",
    types={GNBDUFunction},
    associations={},
    generalizations={}
)
