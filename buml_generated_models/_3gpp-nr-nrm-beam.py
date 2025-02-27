# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Enumerations
BeamType = Enumeration(name="BeamType")
BeamType_SSB-BEAM = EnumerationLiteral(name="SSB-BEAM", owner=BeamType)
BeamType.literals = {BeamType_SSB-BEAM}

# Classes
Beam = Class(name="Beam", synonyms=["Represents the per-Beam information required for, e.g. beam performance management utilizing measurements generated in the RAN. Can have spatial attributes of horizontal/azimuth (ie: Phi ?-axis) and vertical/tilt (ie: Theta ?-axis) beam pointing direction and beam width attributes."])

# Beam class attributes and methods
Beam_beamAzimuth: Property = Property(name="beamAzimuth", type=IntegerType, synonyms=["The azimuth of a beam transmission, which means the horizontal beamforming pointing angle (beam peak direction) in the (Phi) ?-axis in 1/10th degree resolution. The pointing angle is the direction equal to the geometric centre of the half-power contour of the beam relative to the reference plane. Zero degree implies explicit antenna bearing (boresight). Positive angle implies clockwise from the antenna bearing."])
Beam_beamHorizWidth: Property = Property(name="beamHorizWidth", type=IntegerType, synonyms=["The Horizontal beamWidth of a beam transmission, which means the horizontal beamforming half-power (3dB down) beamwidth in the (Phi) ?-axis in 1/10th degree resolution."])
Beam_beamIndex: Property = Property(name="beamIndex", type=IntegerType, synonyms=["Index of the beam."])
Beam_beamTilt: Property = Property(name="beamTilt", type=IntegerType, synonyms=["The tilt of a beam transmission, which means the vertical beamforming pointing angle (beam peak direction) in the (Theta) ?-axis in 1/10th degree resolution. The pointing angle is the direction equal to the geometric centre of the half-power contour of the beam relative to the reference plane. Positive value implies downtilt."])
Beam_beamType: Property = Property(name="beamType", type=StringType, synonyms=["The type of the beam."])
Beam_beamVertWidth: Property = Property(name="beamVertWidth", type=IntegerType, synonyms=["The Vertical beamWidth of a beam transmission, which means the vertical beamforming half-power (3dB down) beamwidth in the (Theta) ?-axis in 1/10th degree resolution."])
Beam.attributes={Beam_beamAzimuth, Beam_beamHorizWidth, Beam_beamIndex, Beam_beamTilt, Beam_beamType, Beam_beamVertWidth}

BeamGrp = Class(name="BeamGrp", synonyms=["Represents the Beam IOC."])

# BeamGrp class attributes and methods
BeamGrp_beamAzimuth: Property = Property(name="beamAzimuth", type=IntegerType, synonyms=["The azimuth of a beam transmission, which means the horizontal beamforming pointing angle (beam peak direction) in the (Phi) ?-axis in 1/10th degree resolution. The pointing angle is the direction equal to the geometric centre of the half-power contour of the beam relative to the reference plane. Zero degree implies explicit antenna bearing (boresight). Positive angle implies clockwise from the antenna bearing."])
BeamGrp_beamHorizWidth: Property = Property(name="beamHorizWidth", type=IntegerType, synonyms=["The Horizontal beamWidth of a beam transmission, which means the horizontal beamforming half-power (3dB down) beamwidth in the (Phi) ?-axis in 1/10th degree resolution."])
BeamGrp_beamIndex: Property = Property(name="beamIndex", type=IntegerType, synonyms=["Index of the beam."])
BeamGrp_beamTilt: Property = Property(name="beamTilt", type=IntegerType, synonyms=["The tilt of a beam transmission, which means the vertical beamforming pointing angle (beam peak direction) in the (Theta) ?-axis in 1/10th degree resolution. The pointing angle is the direction equal to the geometric centre of the half-power contour of the beam relative to the reference plane. Positive value implies downtilt."])
BeamGrp_beamType: Property = Property(name="beamType", type=StringType, synonyms=["The type of the beam."])
BeamGrp_beamVertWidth: Property = Property(name="beamVertWidth", type=IntegerType, synonyms=["The Vertical beamWidth of a beam transmission, which means the vertical beamforming half-power (3dB down) beamwidth in the (Theta) ?-axis in 1/10th degree resolution."])
BeamGrp.attributes={BeamGrp_beamAzimuth, BeamGrp_beamHorizWidth, BeamGrp_beamIndex, BeamGrp_beamTilt, BeamGrp_beamType, BeamGrp_beamVertWidth}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-beam",
    types={Beam, BeamGrp, BeamType},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the Beam Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
