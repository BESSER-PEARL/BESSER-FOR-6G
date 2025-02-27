# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
Function_ = Class(name="Function_")

# Function_ class attributes and methods
Function__userLabel: Property = Property(name="userLabel", type=StringType)
Function_.attributes={Function__userLabel}

ManagedFunction = Class(name="ManagedFunction")

# ManagedFunction class attributes and methods
ManagedFunction_peeParametersList: Property = Property(name="peeParametersList", type=list)
ManagedFunction_priorityLabel: Property = Property(name="priorityLabel", type=IntegerType)
ManagedFunction_vnfParametersList: Property = Property(name="vnfParametersList", type=list)
ManagedFunction.attributes={ManagedFunction_peeParametersList, ManagedFunction_priorityLabel, ManagedFunction_vnfParametersList}

ManagedFunctionContainedClasses = Class(name="ManagedFunctionContainedClasses")

# ManagedFunctionContainedClasses class attributes and methods
ManagedFunctionContainedClasses_ManagedNFService: Property = Property(name="ManagedNFService", type=list)
ManagedFunctionContainedClasses.attributes={ManagedFunctionContainedClasses_ManagedNFService}

ManagedNFService = Class(name="ManagedNFService")

# ManagedNFService class attributes and methods
ManagedNFService_administrativeState: Property = Property(name="administrativeState", type=StringType)
ManagedNFService_nFServiceType: Property = Property(name="nFServiceType", type=StringType)
ManagedNFService_operationalState: Property = Property(name="operationalState", type=StringType)
ManagedNFService_operations: Property = Property(name="operations", type=list)
ManagedNFService_registrationState: Property = Property(name="registrationState", type=EnumerationType)
ManagedNFService_sAP: Property = Property(name="sAP", type=list)
ManagedNFService_usageState: Property = Property(name="usageState", type=StringType)
ManagedNFService_userLabel: Property = Property(name="userLabel", type=StringType)
ManagedNFService.attributes={ManagedNFService_administrativeState, ManagedNFService_nFServiceType, ManagedNFService_operationalState, ManagedNFService_operations, ManagedNFService_registrationState, ManagedNFService_sAP, ManagedNFService_usageState, ManagedNFService_userLabel}

Operation = Class(name="Operation")

# Operation class attributes and methods
Operation_name: Property = Property(name="name", type=StringType)
Operation_operationSemantics: Property = Property(name="operationSemantics", type=EnumerationType)
Operation.attributes={Operation_name, Operation_operationSemantics}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-managed-function",
    types={Function_, ManagedFunction, ManagedFunctionContainedClasses, ManagedNFService, Operation},
    associations={},
    generalizations={}
)
