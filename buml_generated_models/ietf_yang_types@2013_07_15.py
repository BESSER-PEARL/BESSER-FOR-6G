# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Create custom IETF YANG types
counter32_type = Class(
    name="Counter32",
    attributes=[
        Property(
            name="value",
            type=IntegerType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["A non-negative integer that monotonically increases until it reaches a maximum value of 2^32-1, when it wraps around and starts increasing again from zero."]
        )
    ]
)

counter64_type = Class(
    name="Counter64",
    attributes=[
        Property(
            name="value",
            type=IntegerType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["A non-negative integer that monotonically increases until it reaches a maximum value of 2^64-1, when it wraps around and starts increasing again from zero."]
        )
    ]
)

gauge32_type = Class(
    name="Gauge32",
    attributes=[
        Property(
            name="value",
            type=IntegerType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["A non-negative integer that may increase or decrease, but shall never exceed 2^32-1 or fall below 0."]
        )
    ]
)

gauge64_type = Class(
    name="Gauge64",
    attributes=[
        Property(
            name="value",
            type=IntegerType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["A non-negative integer that may increase or decrease, but shall never exceed 2^64-1 or fall below 0."]
        )
    ]
)

object_identifier_type = Class(
    name="ObjectIdentifier",
    attributes=[
        Property(
            name="value",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Represents administratively assigned names in a registration-hierarchical-name tree."]
        )
    ]
)

yang_identifier_type = Class(
    name="YangIdentifier",
    attributes=[
        Property(
            name="value",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["A YANG identifier string as defined by the 'identifier' rule in Section 12 of RFC 6020."]
        )
    ]
)

date_and_time_type = Class(
    name="DateAndTime",
    attributes=[
        Property(
            name="value",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["The date-and-time type is a profile of the ISO 8601 standard for representation of dates and times using the Gregorian calendar."]
        )
    ]
)

timeticks_type = Class(
    name="TimeTicks",
    attributes=[
        Property(
            name="value",
            type=IntegerType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Represents a non-negative integer that represents the time, modulo 2^32, in hundredths of a second between two epochs."]
        )
    ]
)

timestamp_type = Class(
    name="Timestamp",
    attributes=[
        Property(
            name="value",
            type=IntegerType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Represents the value of an associated timeticks schema node at which a specific occurrence happened."]
        )
    ]
)

phys_address_type = Class(
    name="PhysAddress",
    attributes=[
        Property(
            name="value",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Represents media- or physical-level addresses represented as a sequence octets, each octet represented by two hexadecimal numbers."]
        )
    ]
)

mac_address_type = Class(
    name="MacAddress",
    attributes=[
        Property(
            name="value",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["The mac-address type represents an IEEE 802 MAC address."]
        )
    ]
)

xpath_type = Class(
    name="XPath1.0",
    attributes=[
        Property(
            name="expression",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Represents an XPATH 1.0 expression."]
        )
    ]
)

hex_string_type = Class(
    name="HexString",
    attributes=[
        Property(
            name="value",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["A hexadecimal string with octets represented as hex digits separated by colons."]
        )
    ]
)

uuid_type = Class(
    name="UUID",
    attributes=[
        Property(
            name="value",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["A Universally Unique IDentifier in the string representation defined in RFC 4122."]
        )
    ]
)

dotted_quad_type = Class(
    name="DottedQuad",
    attributes=[
        Property(
            name="value",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["An unsigned 32-bit number expressed in the dotted-quad notation."]
        )
    ]
)

# Domain Model with References
domain_model = DomainModel(
    name="ietf-yang-types",
    types={
        counter32_type, counter64_type, gauge32_type, gauge64_type, object_identifier_type,
        yang_identifier_type, date_and_time_type, timeticks_type, timestamp_type,
        phys_address_type, mac_address_type, xpath_type, hex_string_type, uuid_type, dotted_quad_type
    },
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This module contains a collection of generally useful derived YANG data types."]
