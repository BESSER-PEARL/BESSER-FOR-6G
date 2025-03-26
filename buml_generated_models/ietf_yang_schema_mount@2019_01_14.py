# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Create Namespace class for schema mounts
namespace_class = Class(
    name="Namespace",
    attributes=[
        Property(
            name="prefix",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Namespace prefix."]
        ),
        Property(
            name="uri",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Namespace URI reference."]
        )
    ]
)

# Create Inline Schema class
inline_schema_class = Class(
    name="InlineSchema",
    attributes=[
        Property(
            name="presence",
            type=BooleanType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["A complete self-contained schema is mounted at the mount point."]
        ),
        Property(
            name="description",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["This node indicates that the server has mounted at least the module 'ietf-yang-library' at the mount point, and its instantiation provides the information about the mounted schema. Different instances of the mount point may have different schemas mounted."]
        )
    ]
)

# Create Shared Schema class
shared_schema_class = Class(
    name="SharedSchema",
    attributes=[
        Property(
            name="presence",
            type=BooleanType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["The mounted schema together with the 'parent-reference' make up the schema for this mount point."]
        ),
        Property(
            name="description",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["This node indicates that the server has mounted at least the module 'ietf-yang-library' at the mount point, and its instantiation provides the information about the mounted schema. When XPath expressions in the mounted schema are evaluated, the 'parent-reference' leaf-list is taken into account. Different instances of the mount point MUST have the same schema mounted."]
        ),
        Property(
            name="parentReference",
            type=StringType,
            multiplicity=Multiplicity(0, 1),
            synonyms=["XPath 1.0 expressions that are evaluated in the parent data tree context."]
        )
    ]
)

# Create Mount Point class
mount_point_class = Class(
    name="MountPoint",
    attributes=[
        Property(
            name="module",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Name of a module containing the mount point."]
        ),
        Property(
            name="label",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Label of the mount point defined using the 'mount-point' extension."]
        ),
        Property(
            name="config",
            type=BooleanType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["If this leaf is set to 'false', then all data nodes in the mounted schema are read-only ('config false'), regardless of their 'config' property."]
        ),
        Property(
            name="schemaType",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Schema type, can be 'inline' or 'shared'"]
        ),
        Property(
            name="inlineSchema",
            type=inline_schema_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Contains information about an inline schema mount point."]
        ),
        Property(
            name="sharedSchema",
            type=shared_schema_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Contains information about a shared schema mount point."]
        )
    ]
)

# Create Schema Mounts class
schema_mounts_class = Class(
    name="SchemaMounts",
    attributes=[
        Property(
            name="namespace",
            type=namespace_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["This list provides a mapping of namespace prefixes that are used in XPath expressions of 'parent-reference' leafs to the corresponding namespace URI references."]
        ),
        Property(
            name="mountPoint",
            type=mount_point_class,
            multiplicity=Multiplicity(0, 1),
            synonyms=["Each entry of this list specifies a schema for a particular mount point."]
        )
    ]
)

# Extensions class for the mount-point extension
mount_point_extension_class = Class(
    name="MountPointExtension",
    attributes=[
        Property(
            name="label",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Label for the mount point."]
        ),
        Property(
            name="description",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["The mount-point statement defines a place in the node hierarchy where other data models may be attached."]
        )
    ]
)

# Domain Model with References
domain_model = DomainModel(
    name="ietf-yang-schema-mount",
    types={namespace_class, inline_schema_class, shared_schema_class, mount_point_class, schema_mounts_class, mount_point_extension_class},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This module defines a YANG extension statement that can be used to incorporate data models defined in other YANG modules in a module."]
