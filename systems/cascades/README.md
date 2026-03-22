# Cascades

A cascade is the propagation of failure through a system.

Where fragility describes the tendency for small failures to become large consequences, cascades describe the mechanism by which that expansion occurs.

A cascade begins when a failure at one node travels through dependencies, trust relationships, or shared infrastructure and affects additional nodes. These secondary failures may trigger further failures, creating a chain or network of disruption.

Cascades may be immediate or delayed, visible or silent, linear or branching.

They often follow existing structure rather than random paths. The shape of the system determines the shape of the cascade.

## Core idea

Failure does not spread randomly.

It follows connections.

## Relationship to fragility

Fragility determines whether a system allows cascades.

Cascades describe how those failures move once they begin.

Fragility is the condition.

Cascades are the process.

## Questions

Where can failure start?

Where can it travel?

What connections allow it to propagate?

What stops it?

What slows it?

What amplifies it?

## In this folder

- `model.md` defines cascade behavior in structural terms.
- `mapping.md` provides a method for tracing cascade paths.
- `applications/` contains real-world examples.

## Directions

Future work may include:

- mapping cascade paths
- identifying high-risk connections
- modeling branching failure patterns
- designing containment boundaries