# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ManagedElement = Class(name="ManagedElement", synonyms=["Represents telecommunications equipment or TMN entities within the telecommunications network providing support and/or service to the subscriber."])

# ManagedElement class attributes and methods
ManagedElement_ManagedElement: Property = Property(name="ManagedElement", type=list, synonyms=["Represents telecommunications equipment or TMN entities within the telecommunications network providing support and/or service to the subscriber. An ManagedElement IOC is used to represent a Network Element defined in TS 32.101 including virtualizeation or non-virtualization scenario. An ManagedElement instance is used for communicating with a manager (directly or indirectly) over one or more management interfaces for the purpose of being monitored and/or controlled. ManagedElement may or may not additionally perform element management functionality. An ManagedElement contains equipment that may or may not be geographically distributed. A telecommunication equipment has software and hardware components. The ManagedElement IOC described above represents following two case: - In the case when the software component is designed to run on dedicated hardware component, the ManagedElement IOC description includes both software and hardware components. - In the case when the software is designed to run on ETSI NFV defined NFVI [15], the ManagedElement IOC description would exclude the NFVI component supporting the above mentioned subject software. A ManagedElement may be contained in either a SubNetwork or in a MeContext instance. A single ManagedElement may also exist stand-alone with no parent at all. The relation of ManagedElement IOC and ManagedFunction IOC can be described as following: - A ManaagedElement instance may have 1..1 containment relationship to a ManagedFunction instance. In this case, the ManagedElement IOC may be used to represent a NE with single functionality. For example, a ManagedElement is used to represent the 3GPP defined RNC node; - A ManagedElement instance may have 1..N containment relationship to multiple ManagedFunction IOC instances. In this case, the ManagedElement IOC may be used to represent a NE with combined ManagedFunction funcationality (as indicated by the managedElementType attribute and the contained instances of different ManagedFunction IOCs).For example, a ManagedElement is used to represent the combined functionality of 3GPP defined gNBCUCPFuntion, gNBCUUPFunction and gNBDUFunction"])
ManagedElement_priorityLabel: Property = Property(name="priorityLabel", type=IntegerType)
ManagedElement_swVersion: Property = Property(name="swVersion", type=StringType)
ManagedElement_userDefinedState: Property = Property(name="userDefinedState", type=StringType, synonyms=["An operator defined state for operator specific usage"])
ManagedElement_vendorName: Property = Property(name="vendorName", type=StringType)
ManagedElement.attributes={ManagedElement_ManagedElement, ManagedElement_priorityLabel, ManagedElement_swVersion, ManagedElement_userDefinedState, ManagedElement_vendorName}

ManagedElement_ = Class(name="ManagedElement_", synonyms=["Abstract class representing telecommunications resources. An ME communicates with a manager (directly or indirectly) for the purpose of being monitored and/or controlled. MEs may perform element management functionality. An ME (and its contained Function_(s)) may or may not be geographically distributed. An ME (and its contained Function_(s)) is often referred to as a Network Element"])

# ManagedElement_ class attributes and methods
ManagedElement__dnPrefix: Property = Property(name="dnPrefix", type=StringType, synonyms=["Provides naming context that allows the Managed Elements to be partitioned into logical domains. A Distingushed Name(DN) is defined by 3GPP TS 32.300, which splits the DN into a DN Prefix and Local DN"])
ManagedElement__locationName: Property = Property(name="locationName", type=StringType, synonyms=["The physical location (e.g. an address) of an entity represented by a (derivative of) ManagedElement_. It may contain no information to support the case where the derivative of ManagedElement_ needs to represent a distributed multi-location NE."])
ManagedElement__userLabel: Property = Property(name="userLabel", type=StringType, synonyms=["A user-friendly (and user assignable) name of this object."])
ManagedElement_.attributes={ManagedElement__dnPrefix, ManagedElement__locationName, ManagedElement__userLabel}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-managed-element",
    types={ManagedElement, ManagedElement_},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines ManagedElement which will be augmented by other IOCs"]
