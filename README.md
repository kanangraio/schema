# Kanangra I/O Schema Definitions

Meta data schemas are defined in the Avro Format https://avro.apache.org/. This format is widely used in event streaming and supports native storage.

To use a JSON Schema format this Avro converter can be used
https://json-schema-validator.herokuapp.com/avro.jsp

# Schema Standards

- All schemas are defined in lowercase.
- All schemas are singular. An alias can be used for plural cross references.
- All fields are defined in lowercase including widely accepted abbreviations.
- Schemas should try to follow a maximum two levels of nesting similar to the Star Schema concept

# core
- Country
- CountryState
- Category
- Link
- Location
- Position
