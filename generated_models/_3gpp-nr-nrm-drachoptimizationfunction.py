# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
DRACHOptimizationFunction = Class(name="DRACHOptimizationFunction")

# DRACHOptimizationFunction class attributes and methods
DRACHOptimizationFunction_drachOptimizationControl: Property = Property(name="drachOptimizationControl", type=BooleanType)
DRACHOptimizationFunction_ueAccProbilityDist: Property = Property(name="ueAccProbilityDist", type=list)
DRACHOptimizationFunction_ueAccDelayProbilityDist: Property = Property(name="ueAccDelayProbilityDist", type=list)
DRACHOptimizationFunction.attributes={DRACHOptimizationFunction_drachOptimizationControl, DRACHOptimizationFunction_ueAccProbilityDist, DRACHOptimizationFunction_ueAccDelayProbilityDist}

UeAccProbilityDist = Class(name="UeAccProbilityDist")

# UeAccProbilityDist class attributes and methods
UeAccProbilityDist_targetProbability: Property = Property(name="targetProbability", type=TargetProbability)
UeAccProbilityDist_numberofpreamblessent: Property = Property(name="numberofpreamblessent", type=Numberofpreamblessent)
UeAccProbilityDist.attributes={UeAccProbilityDist_targetProbability, UeAccProbilityDist_numberofpreamblessent}

UeAccDelayProbilityDist = Class(name="UeAccDelayProbilityDist")

# UeAccDelayProbilityDist class attributes and methods
UeAccDelayProbilityDist_targetProbability: Property = Property(name="targetProbability", type=TargetProbability)
UeAccDelayProbilityDist_accessdelay: Property = Property(name="accessdelay", type=Accessdelay)
UeAccDelayProbilityDist.attributes={UeAccDelayProbilityDist_targetProbability, UeAccDelayProbilityDist_accessdelay}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-drachoptimizationfunction",
    types={DRACHOptimizationFunction, UeAccProbilityDist, UeAccDelayProbilityDist},
    associations={},
    generalizations={}
)
