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
Beam = Class(name="Beam")

# Beam class attributes and methods
Beam_beamAzimuth: Property = Property(name="beamAzimuth", type=IntegerType)
Beam_beamHorizWidth: Property = Property(name="beamHorizWidth", type=IntegerType)
Beam_beamIndex: Property = Property(name="beamIndex", type=IntegerType)
Beam_beamTilt: Property = Property(name="beamTilt", type=IntegerType)
Beam_beamType: Property = Property(name="beamType", type=StringType)
Beam_beamVertWidth: Property = Property(name="beamVertWidth", type=IntegerType)
Beam.attributes={Beam_beamAzimuth, Beam_beamHorizWidth, Beam_beamIndex, Beam_beamTilt, Beam_beamType, Beam_beamVertWidth}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-beam",
    types={Beam, BeamType},
    associations={},
    generalizations={}
)
