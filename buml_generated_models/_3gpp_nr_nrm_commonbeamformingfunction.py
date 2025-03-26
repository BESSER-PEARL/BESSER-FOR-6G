# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model

# Classes
CommonBeamformingFunction = Class(name="CommonBeamformingFunction", synonyms=["Represents the CommonBeamformingFunction IOC."])

# CommonBeamformingFunction class attributes and methods
CommonBeamformingFunction_CommonBeamformingFunction: Property = Property(name="CommonBeamformingFunction", type=DataType('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["Represents common beamforming functionality (eg: SSB beams) for the NRSectorCarrier."])
CommonBeamformingFunction_coverageShape: Property = Property(name="coverageShape", type=IntegerType, synonyms=["Identifies the sector carrier coverage shape described by the envelope of the contained SSB beams. The coverage shape is implementation dependent."])
CommonBeamformingFunction_digitalAzimuth: Property = Property(name="digitalAzimuth", type=IntegerType, synonyms=["Digitally-controlled azimuth through beamforming. It represents the horizontal pointing direction of the antenna relative to the antenna bore sight, representing the total non-mechanical horizontal pan of the selected coverageShape. Positive value gives azimuth to the right and negative value gives an azimuth to the left."])
CommonBeamformingFunction_digitalTilt: Property = Property(name="digitalTilt", type=IntegerType, synonyms=["Digitally-controlled tilt through beamforming. It represents the vertical pointing direction of the antenna relative to the antenna bore sight, representing the total non-mechanical vertical tilt of the selected coverageShape. Positive value gives downwards tilt and negative value gives upwards tilt."])
CommonBeamformingFunction.attributes={CommonBeamformingFunction_CommonBeamformingFunction, CommonBeamformingFunction_coverageShape, CommonBeamformingFunction_digitalAzimuth, CommonBeamformingFunction_digitalTilt}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-commonbeamformingfunction",
    types={CommonBeamformingFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the CommonBeamformingFuntion Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
