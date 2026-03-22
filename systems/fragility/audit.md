# Fragility Audit

This method is used to examine how a system responds to stress, failure, compromise, or disruption.

The aim is not to prove that a system is bad. The aim is to understand where weight accumulates, where dependencies hide, how failure propagates, and what recovery paths exist.

## Step 1: Define the system

What system is being analyzed?

What is inside scope?
What is outside scope?

What is the system supposed to do?
What does it rely on to do that?

## Step 2: Identify nodes

List the important nodes in the system.

These may include people, devices, accounts, services, storage layers, policies, routines, procedures, locations, documents, trust relationships, or informal roles.

Ask:
What components carry function, value, access, responsibility, or memory?

## Step 3: Identify edges

Map the dependencies between nodes.

Ask:
What connects to what?
What grants access to what?
What relies on what?
What is upstream from what?
What is trusted by what?

## Step 4: Find root nodes

Identify the nodes that hold disproportionate weight.

These may include:
- master accounts
- central machines
- storage layers
- recovery channels
- key people
- undocumented procedures
- hidden assumptions
- social gatekeepers

A root node is any point whose failure would have outsized consequences.

## Step 5: Simulate failure

For each root node, ask:

What happens if this breaks?
What becomes inaccessible?
What becomes exposed?
What stops functioning?
What silently degrades?
What propagates outward?

## Step 6: Evaluate propagation

Does failure:
- stay local
- spread immediately
- spread quietly
- trigger secondary failures
- create irreversible damage
- damage trust, legitimacy, or coordination

Describe the likely failure paths.

## Step 7: Evaluate recovery

Can the system recover?

Ask:
Is there backup?
Is there rollback?
Is there redundancy?
Is there documentation?
Is there another trusted path?
Can recovery happen quickly enough to matter?
Who knows how to restore function?

## Step 8: Record weak points

For each weak point, note:

- impact
- likelihood
- visibility
- recoverability

A weak point with high impact, low visibility, and poor recovery is usually a serious fragility point.

## Step 9: Design improvements

Reduce fragility by:

- removing single points of failure
- decoupling systems
- improving observability
- strengthening recovery paths
- reducing trust assumptions
- distributing responsibility
- making hidden dependencies visible
- documenting restoration steps

## Output template

System:
Scope:
Purpose:
Key nodes:
Key dependencies:
Root nodes:
Likely failure paths:
Propagation risks:
Recovery gaps:
Recommended changes:
Notes: