from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    StringType, IntegerType
)

# Basic types
DistinguishedName = StringType
DateTime = StringType

# Create domain model
domain_model = DomainModel(name="_3gpp_common_yang_types")
