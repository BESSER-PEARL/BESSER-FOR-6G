# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
EUtranFreqRelation = Class(name="EUtranFreqRelation")

# EUtranFreqRelation class attributes and methods
EUtranFreqRelation_cellIndividualOffset: Property = Property(name="cellIndividualOffset", type=StringType)
EUtranFreqRelation_cellReselectionPriority: Property = Property(name="cellReselectionPriority", type=IntegerType)
EUtranFreqRelation_cellReselectionSubPriority: Property = Property(name="cellReselectionSubPriority", type=IntegerType)
EUtranFreqRelation_eUtranFrequencyRef: Property = Property(name="eUtranFrequencyRef", type=StringType)
EUtranFreqRelation_pMax: Property = Property(name="pMax", type=IntegerType)
EUtranFreqRelation_qOffsetFreq: Property = Property(name="qOffsetFreq", type=IntegerType)
EUtranFreqRelation_qQualMin: Property = Property(name="qQualMin", type=IntegerType)
EUtranFreqRelation_qRxLevMin: Property = Property(name="qRxLevMin", type=IntegerType)
EUtranFreqRelation_tReselectionEutra: Property = Property(name="tReselectionEutra", type=IntegerType)
EUtranFreqRelation_tReselectionEutraSfHigh: Property = Property(name="tReselectionEutraSfHigh", type=IntegerType)
EUtranFreqRelation_tReselectionEutraSfMedium: Property = Property(name="tReselectionEutraSfMedium", type=IntegerType)
EUtranFreqRelation_threshXHighP: Property = Property(name="threshXHighP", type=IntegerType)
EUtranFreqRelation_threshXHighQ: Property = Property(name="threshXHighQ", type=IntegerType)
EUtranFreqRelation_threshXLowP: Property = Property(name="threshXLowP", type=IntegerType)
EUtranFreqRelation_threshXLowQ: Property = Property(name="threshXLowQ", type=IntegerType)
EUtranFreqRelation.attributes={EUtranFreqRelation_cellIndividualOffset, EUtranFreqRelation_cellReselectionPriority, EUtranFreqRelation_cellReselectionSubPriority, EUtranFreqRelation_eUtranFrequencyRef, EUtranFreqRelation_pMax, EUtranFreqRelation_qOffsetFreq, EUtranFreqRelation_qQualMin, EUtranFreqRelation_qRxLevMin, EUtranFreqRelation_tReselectionEutra, EUtranFreqRelation_tReselectionEutraSfHigh, EUtranFreqRelation_tReselectionEutraSfMedium, EUtranFreqRelation_threshXHighP, EUtranFreqRelation_threshXHighQ, EUtranFreqRelation_threshXLowP, EUtranFreqRelation_threshXLowQ}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-eutranfreqrelation",
    types={EUtranFreqRelation},
    associations={},
    generalizations={}
)
