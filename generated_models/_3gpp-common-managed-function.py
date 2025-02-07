# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
Operation = Class(name="Operation")

# Operation class attributes and methods
Operation_name: Property = Property(name="name", type=StringType)
Operation_operationSemantics: Property = Property(name="operationSemantics", type=enumeration)
Operation.attributes={Operation_name, Operation_operationSemantics}

ManagedNFService = Class(name="ManagedNFService")

# ManagedNFService class attributes and methods
ManagedNFService_userLabel: Property = Property(name="userLabel", type=StringType)
ManagedNFService_nFServiceType: Property = Property(name="nFServiceType", type=StringType)
ManagedNFService_administrativeState: Property = Property(name="administrativeState", type=types3gpp:AdministrativeState)
ManagedNFService_operationalState: Property = Property(name="operationalState", type=types3gpp:OperationalState)
ManagedNFService_usageState: Property = Property(name="usageState", type=types3gpp:usageState)
ManagedNFService_registrationState: Property = Property(name="registrationState", type=enumeration)
ManagedNFService_sAP: Property = Property(name="sAP", type=list)
ManagedNFService_operations: Property = Property(name="operations", type=list)
ManagedNFService.attributes={ManagedNFService_userLabel, ManagedNFService_nFServiceType, ManagedNFService_administrativeState, ManagedNFService_operationalState, ManagedNFService_usageState, ManagedNFService_registrationState, ManagedNFService_sAP, ManagedNFService_operations}

Function_ = Class(name="Function_")

# Function_ class attributes and methods
Function__userLabel: Property = Property(name="userLabel", type=StringType)
Function_.attributes={Function__userLabel}

ManagedFunction = Class(name="ManagedFunction")

# ManagedFunction class attributes and methods
ManagedFunction_priorityLabel: Property = Property(name="priorityLabel", type=IntegerType)
ManagedFunction_vnfParametersList: Property = Property(name="vnfParametersList", type=list)
ManagedFunction_peeParametersList: Property = Property(name="peeParametersList", type=list)
ManagedFunction.attributes={ManagedFunction_priorityLabel, ManagedFunction_vnfParametersList, ManagedFunction_peeParametersList}

ManagedFunctionContainedClasses = Class(name="ManagedFunctionContainedClasses")

# ManagedFunctionContainedClasses class attributes and methods
ManagedFunctionContainedClasses_ManagedNFService: Property = Property(name="ManagedNFService", type=list)
ManagedFunctionContainedClasses.attributes={ManagedFunctionContainedClasses_ManagedNFService}

