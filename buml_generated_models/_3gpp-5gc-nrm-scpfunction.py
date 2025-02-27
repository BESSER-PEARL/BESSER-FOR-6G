# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
SCPFunction = Class(name="SCPFunction", synonyms=["5G Core SCP Function"])

# SCPFunction class attributes and methods
SCPFunction_address: Property = Property(name="address", type=StringType, synonyms=["The host address of the SCP."])
SCPFunction_supportedFuncList: Property = Property(name="supportedFuncList", type=list)
SCPFunction.attributes={SCPFunction_address, SCPFunction_supportedFuncList}

SCPFunctionGrp = Class(name="SCPFunctionGrp")

# SCPFunctionGrp class attributes and methods
SCPFunctionGrp_address: Property = Property(name="address", type=StringType, synonyms=["The host address of the SCP."])
SCPFunctionGrp_supportedFuncList: Property = Property(name="supportedFuncList", type=list)
SCPFunctionGrp.attributes={SCPFunctionGrp_address, SCPFunctionGrp_supportedFuncList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-scpfunction",
    types={SCPFunction, SCPFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the SCP function in 5GC. For more information about the SCP, see 3GPP TS 23.501."]
