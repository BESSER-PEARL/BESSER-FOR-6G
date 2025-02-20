# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Enumerations
TargetProbability = Enumeration(name="TargetProbability")
TargetProbability_25 = EnumerationLiteral(name="25", owner=TargetProbability)
TargetProbability_50 = EnumerationLiteral(name="50", owner=TargetProbability)
TargetProbability_75 = EnumerationLiteral(name="75", owner=TargetProbability)
TargetProbability_90 = EnumerationLiteral(name="90", owner=TargetProbability)
TargetProbability.literals = {TargetProbability_25, TargetProbability_50, TargetProbability_75, TargetProbability_90}

# Classes
DRACHOptimizationFunction = Class(name="DRACHOptimizationFunction")

# DRACHOptimizationFunction class attributes and methods
DRACHOptimizationFunction_drachOptimizationControl: Property = Property(name="drachOptimizationControl", type=BooleanType)
DRACHOptimizationFunction_ueAccDelayProbilityDist: Property = Property(name="ueAccDelayProbilityDist", type=list)
DRACHOptimizationFunction_ueAccProbilityDist: Property = Property(name="ueAccProbilityDist", type=list)
DRACHOptimizationFunction.attributes={DRACHOptimizationFunction_drachOptimizationControl, DRACHOptimizationFunction_ueAccDelayProbilityDist, DRACHOptimizationFunction_ueAccProbilityDist}

UeAccDelayProbilityDist = Class(name="UeAccDelayProbilityDist")

# UeAccDelayProbilityDist class attributes and methods
UeAccDelayProbilityDist_accessdelay: Property = Property(name="accessdelay", type=StringType)
UeAccDelayProbilityDist_targetProbability: Property = Property(name="targetProbability", type=StringType)
UeAccDelayProbilityDist.attributes={UeAccDelayProbilityDist_accessdelay, UeAccDelayProbilityDist_targetProbability}

UeAccProbilityDist = Class(name="UeAccProbilityDist")

# UeAccProbilityDist class attributes and methods
UeAccProbilityDist_numberofpreamblessent: Property = Property(name="numberofpreamblessent", type=StringType)
UeAccProbilityDist_targetProbability: Property = Property(name="targetProbability", type=StringType)
UeAccProbilityDist.attributes={UeAccProbilityDist_numberofpreamblessent, UeAccProbilityDist_targetProbability}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-drachoptimizationfunction",
    types={DRACHOptimizationFunction, TargetProbability, UeAccDelayProbilityDist, UeAccProbilityDist},
    associations={},
    generalizations={}
)
