# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NRFreqRelation = Class(name="NRFreqRelation")

# NRFreqRelation class attributes and methods
NRFreqRelation_cellReselectionPriority: Property = Property(name="cellReselectionPriority", type=IntegerType)
NRFreqRelation_cellReselectionSubPriority: Property = Property(name="cellReselectionSubPriority", type=IntegerType)
NRFreqRelation_nRFrequencyRef: Property = Property(name="nRFrequencyRef", type=StringType)
NRFreqRelation_pMax: Property = Property(name="pMax", type=IntegerType)
NRFreqRelation_qOffsetFreq: Property = Property(name="qOffsetFreq", type=StringType)
NRFreqRelation_qQualMin: Property = Property(name="qQualMin", type=IntegerType)
NRFreqRelation_qRxLevMin: Property = Property(name="qRxLevMin", type=IntegerType)
NRFreqRelation_tReselectionNR: Property = Property(name="tReselectionNR", type=IntegerType)
NRFreqRelation_tReselectionNRSfHigh: Property = Property(name="tReselectionNRSfHigh", type=IntegerType)
NRFreqRelation_tReselectionNRSfMedium: Property = Property(name="tReselectionNRSfMedium", type=IntegerType)
NRFreqRelation_threshXHighP: Property = Property(name="threshXHighP", type=IntegerType)
NRFreqRelation_threshXHighQ: Property = Property(name="threshXHighQ", type=IntegerType)
NRFreqRelation_threshXLowP: Property = Property(name="threshXLowP", type=IntegerType)
NRFreqRelation_threshXLowQ: Property = Property(name="threshXLowQ", type=IntegerType)
NRFreqRelation.attributes={NRFreqRelation_cellReselectionPriority, NRFreqRelation_cellReselectionSubPriority, NRFreqRelation_nRFrequencyRef, NRFreqRelation_pMax, NRFreqRelation_qOffsetFreq, NRFreqRelation_qQualMin, NRFreqRelation_qRxLevMin, NRFreqRelation_tReselectionNR, NRFreqRelation_tReselectionNRSfHigh, NRFreqRelation_tReselectionNRSfMedium, NRFreqRelation_threshXHighP, NRFreqRelation_threshXHighQ, NRFreqRelation_threshXLowP, NRFreqRelation_threshXLowQ}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrfreqrelation",
    types={NRFreqRelation},
    associations={},
    generalizations={}
)
