# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
EUtranFreqRelation = Class(name="EUtranFreqRelation")

# EUtranFreqRelation class attributes and methods
EUtranFreqRelation_cellIndividualOffset: Property = Property(name="cellIndividualOffset", type=types3gpp:QOffsetRange)
EUtranFreqRelation_cellReselectionPriority: Property = Property(name="cellReselectionPriority", type=IntegerType)
EUtranFreqRelation_cellReselectionSubPriority: Property = Property(name="cellReselectionSubPriority", type=IntegerType)
EUtranFreqRelation_pMax: Property = Property(name="pMax", type=IntegerType)
EUtranFreqRelation_qOffsetFreq: Property = Property(name="qOffsetFreq", type=IntegerType)
EUtranFreqRelation_qQualMin: Property = Property(name="qQualMin", type=IntegerType)
EUtranFreqRelation_qRxLevMin: Property = Property(name="qRxLevMin", type=IntegerType)
EUtranFreqRelation_threshXHighP: Property = Property(name="threshXHighP", type=IntegerType)
EUtranFreqRelation_threshXHighQ: Property = Property(name="threshXHighQ", type=IntegerType)
EUtranFreqRelation_threshXLowP: Property = Property(name="threshXLowP", type=IntegerType)
EUtranFreqRelation_threshXLowQ: Property = Property(name="threshXLowQ", type=IntegerType)
EUtranFreqRelation_tReselectionEutra: Property = Property(name="tReselectionEutra", type=IntegerType)
EUtranFreqRelation_tReselectionEutraSfHigh: Property = Property(name="tReselectionEutraSfHigh", type=IntegerType)
EUtranFreqRelation_tReselectionEutraSfMedium: Property = Property(name="tReselectionEutraSfMedium", type=IntegerType)
EUtranFreqRelation_eUtranFrequencyRef: Property = Property(name="eUtranFrequencyRef", type=types3gpp:DistinguishedName)
EUtranFreqRelation.attributes={EUtranFreqRelation_cellIndividualOffset, EUtranFreqRelation_cellReselectionPriority, EUtranFreqRelation_cellReselectionSubPriority, EUtranFreqRelation_pMax, EUtranFreqRelation_qOffsetFreq, EUtranFreqRelation_qQualMin, EUtranFreqRelation_qRxLevMin, EUtranFreqRelation_threshXHighP, EUtranFreqRelation_threshXHighQ, EUtranFreqRelation_threshXLowP, EUtranFreqRelation_threshXLowQ, EUtranFreqRelation_tReselectionEutra, EUtranFreqRelation_tReselectionEutraSfHigh, EUtranFreqRelation_tReselectionEutraSfMedium, EUtranFreqRelation_eUtranFrequencyRef}

