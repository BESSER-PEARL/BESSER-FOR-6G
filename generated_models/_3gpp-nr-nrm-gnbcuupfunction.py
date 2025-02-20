# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
TAI = Class(name="TAI")

# TAI class attributes and methods
TAI_nRTAC: Property = Property(name="nRTAC", type=IntegerType)
TAI_pLMNId: Property = Property(name="pLMNId", type=list)
TAI.attributes={TAI_nRTAC, TAI_pLMNId}

BackhaulAddress = Class(name="BackhaulAddress")

# BackhaulAddress class attributes and methods
BackhaulAddress_gNBId: Property = Property(name="gNBId", type=IntegerType)
BackhaulAddress_tAI: Property = Property(name="tAI", type=list)
BackhaulAddress.attributes={BackhaulAddress_gNBId, BackhaulAddress_tAI}

MappingSetIDBackhaulAddress = Class(name="MappingSetIDBackhaulAddress")

# MappingSetIDBackhaulAddress class attributes and methods
MappingSetIDBackhaulAddress_idx: Property = Property(name="idx", type=IntegerType)
MappingSetIDBackhaulAddress_setID: Property = Property(name="setID", type=IntegerType)
MappingSetIDBackhaulAddress_backhaulAddress: Property = Property(name="backhaulAddress", type=list)
MappingSetIDBackhaulAddress.attributes={MappingSetIDBackhaulAddress_idx, MappingSetIDBackhaulAddress_setID, MappingSetIDBackhaulAddress_backhaulAddress}

GNBCUUPFunction = Class(name="GNBCUUPFunction")

# GNBCUUPFunction class attributes and methods
GNBCUUPFunction_gNBCUUPId: Property = Property(name="gNBCUUPId", type=IntegerType)
GNBCUUPFunction_gNBId: Property = Property(name="gNBId", type=IntegerType)
GNBCUUPFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType)
GNBCUUPFunction_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=StringType)
GNBCUUPFunction_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=StringType)
GNBCUUPFunction_pLMNInfoList: Property = Property(name="pLMNInfoList", type=list)
GNBCUUPFunction_mappingSetIDBackhaulAddressList: Property = Property(name="mappingSetIDBackhaulAddressList", type=list)
GNBCUUPFunction.attributes={GNBCUUPFunction_gNBCUUPId, GNBCUUPFunction_gNBId, GNBCUUPFunction_gNBIdLength, GNBCUUPFunction_configurable5QISetRef, GNBCUUPFunction_dynamic5QISetRef, GNBCUUPFunction_pLMNInfoList, GNBCUUPFunction_mappingSetIDBackhaulAddressList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-gnbcuupfunction",
    types={TAI, BackhaulAddress, MappingSetIDBackhaulAddress, GNBCUUPFunction},
    associations={},
    generalizations={}
)
