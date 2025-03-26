# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Classes
# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-yang-extensions",
    types={},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["The module defines YANG extensions needed 3GPP YANG modeling. Copyright (c) 2019 3GPP. All rights reserved. Extensions MUST be defined with the following structure in the description statement: - What is this statement. - Newline, - This statement can be a substatement of the xxx statements with cardinality x..y. - This statement can have the following substatements with cardinality x..y. - Newline - Is changing this statement an editorial, BC(backwards compatible) or NBC(non-BC) change? - Newline. - The argument its meaning and type. Preferably use YANG types and constraints to define the argument's type. Any extension statement can be added with a deviation/deviate add statement. In this case the restriction about the parent statement of the extension SHALL be evaluated based on the target of the deviation statement. Support for this module does not mean that a YANG server implements support for each of these extensions. Implementers of each specific module using an extensions MUST check if the server implements support for the used extension. Note: modules use many extensions which individual implementations MAY or MAY NOT support. If support for an extension is missing the extension statement needs individual handling or it SHOULD be removed from the module using the extension e.g. with a deviation."]
