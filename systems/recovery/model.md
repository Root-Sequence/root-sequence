# Recovery Model

Recovery is the process by which a system restores function, limits damage, reconstitutes itself, or continues in an acceptable form after failure.

## Core terms

A recovery path is a method by which a system regains function after failure.

Restoration is returning a system to a previous state.

Continuation is maintaining function without full restoration.

Rollback is reverting to a known good state.

Rebuild is reconstructing the system from components, backups, or documentation.

Redundancy is the presence of alternate components that can replace failed ones.

Fallback is an alternate mode of operation when primary systems fail.

Graceful degradation is reduced functionality without total failure.

Irrecoverable loss is damage that cannot be undone within the system.

## Patterns

Recovery often depends on:

- backups
- redundancy
- alternate paths
- distributed knowledge
- documentation
- system observability

## Key properties

Recovery may be:

- immediate or delayed
- partial or complete
- manual or automated
- local or distributed

## Guiding questions

What remains after failure?

What can be restored?

What can be rerouted?

What must be rebuilt?

What is permanently lost?

## Principle

Recovery determines whether failure ends the system or becomes part of its continuation.