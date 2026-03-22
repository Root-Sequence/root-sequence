# Cascade Mapping

This method is used to trace how failure propagates through a system.

## Step 1: Identify origin points

Where can failure start?

Examples:
- compromised account
- failed machine
- broken assumption
- conflict event

## Step 2: Trace immediate dependencies

What directly depends on the origin?

What breaks first?

## Step 3: Expand outward

For each affected node:

What depends on this?

Continue tracing outward.

## Step 4: Identify branching

Where does one failure affect multiple nodes?

These are amplification points.

## Step 5: Identify choke points

Where could the cascade be slowed or stopped?

Examples:
- isolation
- redundancy
- validation
- boundaries

## Step 6: Identify hidden paths

What connections are not obvious?

What might fail later or indirectly?

## Step 7: Evaluate outcome

Does the cascade:
- remain contained
- spread widely
- create irreversible damage

## Output

Origin:
Primary path:
Secondary paths:
Branch points:
Choke points:
Final impact: