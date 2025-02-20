# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
Beam = Class(name="Beam")

# Beam class attributes and methods
Beam_beamIndex: Property = Property(name="beamIndex", type=IntegerType)
Beam_beamType: Property = Property(name="beamType", type=BeamType)
Beam_beamAzimuth: Property = Property(name="beamAzimuth", type=IntegerType)
Beam_beamTilt: Property = Property(name="beamTilt", type=IntegerType)
Beam_beamHorizWidth: Property = Property(name="beamHorizWidth", type=IntegerType)
Beam_beamVertWidth: Property = Property(name="beamVertWidth", type=IntegerType)
Beam.attributes={Beam_beamIndex, Beam_beamType, Beam_beamAzimuth, Beam_beamTilt, Beam_beamHorizWidth, Beam_beamVertWidth}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-beam",
    types={Beam},
    associations={},
    generalizations={}
)
