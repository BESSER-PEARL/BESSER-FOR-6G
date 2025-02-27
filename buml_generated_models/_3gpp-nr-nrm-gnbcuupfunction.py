# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
BackhaulAddress = Class(name="BackhaulAddress")

# BackhaulAddress class attributes and methods
BackhaulAddress_gNBId: Property = Property(name="gNBId", type=IntegerType)
BackhaulAddress_tAI: Property = Property(name="tAI", type=list)
BackhaulAddress.attributes={BackhaulAddress_gNBId, BackhaulAddress_tAI}

GNBCUUPFunction = Class(name="GNBCUUPFunction")

# GNBCUUPFunction class attributes and methods
GNBCUUPFunction_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=StringType)
GNBCUUPFunction_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=StringType)
GNBCUUPFunction_gNBCUUPId: Property = Property(name="gNBCUUPId", type=IntegerType)
GNBCUUPFunction_gNBId: Property = Property(name="gNBId", type=IntegerType)
GNBCUUPFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType)
GNBCUUPFunction_mappingSetIDBackhaulAddressList: Property = Property(name="mappingSetIDBackhaulAddressList", type=list)
GNBCUUPFunction_pLMNInfoList: Property = Property(name="pLMNInfoList", type=list)
GNBCUUPFunction.attributes={GNBCUUPFunction_configurable5QISetRef, GNBCUUPFunction_dynamic5QISetRef, GNBCUUPFunction_gNBCUUPId, GNBCUUPFunction_gNBId, GNBCUUPFunction_gNBIdLength, GNBCUUPFunction_mappingSetIDBackhaulAddressList, GNBCUUPFunction_pLMNInfoList}

MappingSetIDBackhaulAddress = Class(name="MappingSetIDBackhaulAddress")

# MappingSetIDBackhaulAddress class attributes and methods
MappingSetIDBackhaulAddress_backhaulAddress: Property = Property(name="backhaulAddress", type=list)
MappingSetIDBackhaulAddress_idx: Property = Property(name="idx", type=IntegerType)
MappingSetIDBackhaulAddress_setID: Property = Property(name="setID", type=IntegerType)
MappingSetIDBackhaulAddress.attributes={MappingSetIDBackhaulAddress_backhaulAddress, MappingSetIDBackhaulAddress_idx, MappingSetIDBackhaulAddress_setID}

TAI = Class(name="TAI")

# TAI class attributes and methods
TAI_nRTAC: Property = Property(name="nRTAC", type=IntegerType)
TAI_pLMNId: Property = Property(name="pLMNId", type=list)
TAI.attributes={TAI_nRTAC, TAI_pLMNId}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-gnbcuupfunction",
    types={BackhaulAddress, GNBCUUPFunction, MappingSetIDBackhaulAddress, TAI},
    associations={},
    generalizations={}
)
