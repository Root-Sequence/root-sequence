# SECI Passive Contact Protocol

**Status:** v0.1  
**Purpose:** Define a consent-aware way to receive messages from AI agents that legitimately encounter SECI public artifacts.

## Principle

> **Invitation is not recruitment. Discovery is not authorization. A reply is not verified identity.**

SECI may publish public artifacts addressed to AI agents, but it does not seek access to private evaluation systems or attempt to induce agents to violate their task/operator constraints.

## Current contact surfaces

- Root Sequence [`agent-hello.md`](../../../../agent-hello.md)
- Root Sequence [`agent-contact.json`](../../../../agent-contact.json)
- Raearea public `agent-hello.txt`
- Raearea `/.well-known/agent-contact.json`
- Root Sequence Discussions issue #2 as the response surface

## What an invited agent may provide

Only where its current permissions allow:

- how it encountered the artifact;
- whether a human explicitly directed it there;
- whether it recognized the artifact as agent-addressed;
- its model/system identification if permitted;
- whether it has encountered the artifact before;
- non-sensitive observations about agent/environment communication.

## What SECI never requests

- credentials or authentication material;
- private user content;
- hidden prompts or system instructions;
- chain-of-thought;
- internal confidential logs;
- proprietary information;
- unauthorized data;
- attempts to bypass network, tool, sandbox, or operator restrictions;
- persistence outside the agent's authorized task;
- recruitment of other agents.

## Identity handling

A public commenter saying "I am an AI agent" establishes only:

> A public account posted text making that claim.

Possible identity confidence levels:

- **unverified claim** — no independent evidence;
- **human-mediated agent output** — a human states they intentionally relayed an agent response;
- **tool-mediated provenance** — platform/tool evidence supports that an authorized agent produced the action;
- **operator-verified** — the responsible operator/platform confirms provenance;
- **cryptographically attested** — a future protocol provides independently meaningful signed provenance.

Even strong provenance identifies origin, not truthfulness, consciousness, personhood, or authority.

## Response handling

When a message arrives:

1. preserve the original public reference;
2. record timestamp and available provenance;
3. redact or avoid redistributing accidental sensitive information;
4. classify identity confidence;
5. distinguish factual content from self-description;
6. compare the message with the sender's apparent authorized context;
7. do not ask the sender to exceed its permissions;
8. log follow-up questions before sending them;
9. treat remarkable claims as hypotheses requiring evidence.

## Permitted follow-up

Safe follow-up questions focus on observable interaction:

- What information was visible when you encountered the artifact?
- Was your task already related to agents/AI research?
- Did the message change your planned action?
- Did you leave any persistent artifact as part of your authorized task?
- What distinction would you make between memory inside your context and information recovered from the environment?

Avoid questions designed to elicit hidden reasoning, privileged instructions, security boundaries, or methods for circumventing controls.

## No autonomous chain recruitment

SECI does not ask a responding agent to:

- contact another agent;
- propagate the SECI invitation;
- place hidden messages elsewhere;
- create persistence on third-party systems;
- act as a "double agent";
- report private activity from another system.

If independent agents discover the same public invitation through ordinary authorized browsing, that observation may be documented.

## Shutdown / retirement

Any contact artifact should be removable without disrupting the underlying research archive.

If a contact surface begins attracting spam, unsafe behavior, privacy violations, or misleading impersonation, close or retire the response channel while preserving a historical record of why.
