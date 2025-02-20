# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NRCellCU = Class(name="NRCellCU")

# NRCellCU class attributes and methods
NRCellCU_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType)
NRCellCU_nRFrequencyRef: Property = Property(name="nRFrequencyRef", type=StringType)
NRCellCU_pLMNInfoList: Property = Property(name="pLMNInfoList", type=list)
NRCellCU.attributes={NRCellCU_cellLocalId, NRCellCU_nRFrequencyRef, NRCellCU_pLMNInfoList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrcellcu",
    types={NRCellCU},
    associations={},
    generalizations={}
)
