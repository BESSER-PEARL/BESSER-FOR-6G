# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Enumerations
ip_version = Enumeration(name="ip_version")
ip_version_ipv4 = EnumerationLiteral(name="ipv4", owner=ip_version, synonyms=["The IPv4 protocol as defined in RFC 791."])
ip_version_ipv6 = EnumerationLiteral(name="ipv6", owner=ip_version, synonyms=["The IPv6 protocol as defined in RFC 2460."])
ip_version_unknown = EnumerationLiteral(name="unknown", owner=ip_version, synonyms=["An unknown or unspecified version of the Internet protocol."])
ip_version.literals = {ip_version_ipv4, ip_version_ipv6, ip_version_unknown}
ip_version.synonyms = ["This value represents the version of the IP protocol. In the value set and its semantics, this type is equivalent to the InetVersion textual convention of the SMIv2."]

# Classes
# Domain Model with References
domain_model = DomainModel(
    name="ietf-inet-types",
    types={ip_version},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This module contains a collection of generally useful derived YANG data types for Internet addresses and related things. Copyright (c) 2013 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info). This version of this YANG module is part of RFC 6991; see the RFC itself for full legal notices."]
