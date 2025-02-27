# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
Function_ = Class(name="Function_", synonyms=["A base grouping for 3GPP functions."])

# Function_ class attributes and methods
Function__userLabel: Property = Property(name="userLabel", type=StringType, synonyms=["A user-friendly (and user assignable) name of this object."])
Function_.attributes={Function__userLabel}

ManagedFunction = Class(name="ManagedFunction", synonyms=["Abstract root class to be inherited/reused by classes representing 3GPP functions. Anywhere this grouping is used by classes inheriting from ManagedFunction the list representing the inheriting class needs to include all contained classes of ManagedFunction too. Contained classes are either - augmented into the Function class or - shall be included in the list representing the inheriting class using the grouping ManagedFunctionContainedClasses: 1) EP_RP solved using augment 2) uses mf3gpp:ManagedFunctionContainedClasses;"])

# ManagedFunction class attributes and methods
ManagedFunction_peeParametersList: Property = Property(name="peeParametersList", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Contains the parameter set for the control and monitoring of power, energy and environmental parameters of ManagedFunction instance(s)."])
ManagedFunction_priorityLabel: Property = Property(name="priorityLabel", type=IntegerType)
ManagedFunction_vnfParametersList: Property = Property(name="vnfParametersList", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Contains the parameter set of the VNF instance(s) corresponding to an NE. The presence of this list indicates that the ManagedFunction represented is realized by one or more VNF instance(s). Otherwise it shall be absent. The presence of a vnfParametersList entry, whose vnfInstanceId with a string length of zero, in createMO operation can trigger the instantiation of the related VNF/VNFC instances."])
ManagedFunction.attributes={ManagedFunction_peeParametersList, ManagedFunction_priorityLabel, ManagedFunction_vnfParametersList}

ManagedFunctionContainedClasses = Class(name="ManagedFunctionContainedClasses", synonyms=["A grouping used to containe classes (lists) contained by the abstract IOC ManagedFunction"])

# ManagedFunctionContainedClasses class attributes and methods
ManagedFunctionContainedClasses_ManagedNFService: Property = Property(name="ManagedNFService", type=top3gpp_model.get_type_by_name('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["Represents a Network Function (NF)"])
ManagedFunctionContainedClasses.attributes={ManagedFunctionContainedClasses_ManagedNFService}

ManagedNFService = Class(name="ManagedNFService", synonyms=["A ManagedNFService represents a Network Function (NF) service."])

# ManagedNFService class attributes and methods
ManagedNFService_administrativeState: Property = Property(name="administrativeState", type=types3gpp_model.get_type_by_name('AdministrativeState'), synonyms=["Permission to use or prohibition against using the instance"])
ManagedNFService_nFServiceType: Property = Property(name="nFServiceType", type=StringType, synonyms=["The type of the managed NF service instance The specifc values allowed are described in clause 7.2 of TS 23.501"])
ManagedNFService_operationalState: Property = Property(name="operationalState", type=types3gpp_model.get_type_by_name('OperationalState'), synonyms=["Describes whether the resource is installed and working"])
ManagedNFService_operations: Property = Property(name="operations", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["Set of operations supported by the managed NF service instance"])
ManagedNFService_registrationState: Property = Property(name="registrationState", type=EnumerationType)
ManagedNFService_sAP: Property = Property(name="sAP", type=types3gpp_model.get_type_by_name('SAP'), multiplicity=Multiplicity(1, "*"), synonyms=["The service access point of the managed NF service instance"])
ManagedNFService_usageState: Property = Property(name="usageState", type=types3gpp_model.get_type_by_name('usageState'), synonyms=["Describes whether the resource is actively in use at a specific instant, and if so, whether or not it has spare capacity for additional users."])
ManagedNFService_userLabel: Property = Property(name="userLabel", type=StringType, synonyms=["A user-friendly (and user assignable) name of this object."])
ManagedNFService.attributes={ManagedNFService_administrativeState, ManagedNFService_nFServiceType, ManagedNFService_operationalState, ManagedNFService_operations, ManagedNFService_registrationState, ManagedNFService_sAP, ManagedNFService_usageState, ManagedNFService_userLabel}

Operation = Class(name="Operation", synonyms=["This data type represents an Operation."])

# Operation class attributes and methods
Operation_name: Property = Property(name="name", type=StringType)
Operation_operationSemantics: Property = Property(name="operationSemantics", type=EnumerationType, synonyms=["Semantics type of the operation."])
Operation.attributes={Operation_name, Operation_operationSemantics}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-managed-function",
    types={Function_, ManagedFunction, ManagedFunctionContainedClasses, ManagedNFService, Operation},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["The module defines a base class/grouping for major 3GPP functions."]
