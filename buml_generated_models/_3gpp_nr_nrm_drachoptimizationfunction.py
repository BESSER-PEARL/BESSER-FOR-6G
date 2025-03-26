# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Enumerations
TargetProbability = Enumeration(name="TargetProbability")
TargetProbability_25 = EnumerationLiteral(name="25", owner=TargetProbability)
TargetProbability_50 = EnumerationLiteral(name="50", owner=TargetProbability)
TargetProbability_75 = EnumerationLiteral(name="75", owner=TargetProbability)
TargetProbability_90 = EnumerationLiteral(name="90", owner=TargetProbability)
TargetProbability.literals = {TargetProbability_25, TargetProbability_50, TargetProbability_75, TargetProbability_90}

# Classes
DRACHOptimizationFunction = Class(name="DRACHOptimizationFunction", synonyms=["Represents the DRACHOptimizationFunction IOC."])

# DRACHOptimizationFunction class attributes and methods
DRACHOptimizationFunction_drachOptimizationControl: Property = Property(name="drachOptimizationControl", type=BooleanType, synonyms=["This attribute determines whether the RACH Optimization function is enabled or disabled."])
DRACHOptimizationFunction_ueAccDelayProbilityDist: Property = Property(name="ueAccDelayProbilityDist", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["This is a list of target Access Delay probability (ADP) for the RACH optimization function."])
DRACHOptimizationFunction_ueAccProbilityDist: Property = Property(name="ueAccProbilityDist", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["This is a list of target Access Probability (APn) for the RACH optimization function."])
DRACHOptimizationFunction.attributes={DRACHOptimizationFunction_drachOptimizationControl, DRACHOptimizationFunction_ueAccDelayProbilityDist, DRACHOptimizationFunction_ueAccProbilityDist}

UeAccDelayProbilityDist = Class(name="UeAccDelayProbilityDist", synonyms=["Represents the target Access Delay probability (ADP) for the RACH optimization function."])

# UeAccDelayProbilityDist class attributes and methods
UeAccDelayProbilityDist_accessdelay: Property = Property(name="accessdelay", type=StringType, synonyms=["This attribute determines the access delay."])
UeAccDelayProbilityDist_targetProbability: Property = Property(name="targetProbability", type=StringType, synonyms=["This attribute determines the target Probability."])
UeAccDelayProbilityDist.attributes={UeAccDelayProbilityDist_accessdelay, UeAccDelayProbilityDist_targetProbability}

UeAccProbilityDist = Class(name="UeAccProbilityDist", synonyms=["Represents the target Access Probability (APn) for the RACH optimization function."])

# UeAccProbilityDist class attributes and methods
UeAccProbilityDist_numberofpreamblessent: Property = Property(name="numberofpreamblessent", type=StringType, synonyms=["This attribute determines the number of preambles sent."])
UeAccProbilityDist_targetProbability: Property = Property(name="targetProbability", type=StringType, synonyms=["This attribute determines the target Probability."])
UeAccProbilityDist.attributes={UeAccProbilityDist_numberofpreamblessent, UeAccProbilityDist_targetProbability}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-drachoptimizationfunction",
    types={DRACHOptimizationFunction, TargetProbability, UeAccDelayProbilityDist, UeAccProbilityDist},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the DRACHOptimizationFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
