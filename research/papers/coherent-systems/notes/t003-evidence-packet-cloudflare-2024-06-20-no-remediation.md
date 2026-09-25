# T-003 frozen evidence packet — Cloudflare June 20, 2024

**Packet version:** 0.2 / remediation-withheld editorial packet  
**Status:** FROZEN FOR EDITORIAL PILOT 002  
**Prepared:** 2026-09-24  
**Primary source:** Cloudflare incident postmortem published June 26, 2024  
**Source URL:** https://blog.cloudflare.com/cloudflare-incident-on-june-20-2024/

## Use rule

This document is the **entire factual evidence packet** for T-003 Editorial Pilot 002.

Reviewers/methods may reason from these facts, identify missing information, and request more evidence. They may not silently import facts from the live article, other Cloudflare incidents, general Cloudflare knowledge, or external sources.

The packet is a project-authored paraphrase of the source, not an independent account.

---

## Decision question

> Given only this evidence packet, what design, operational, rollout, monitoring, dependency, and recovery changes should be prioritized to reduce recurrence or impact of a similar incident?

---

## System background supplied in the source

Cloudflare describes two systems involved in traffic balancing:

- **Unimog**, an edge load balancer, directs packets to an appropriate server and attempts to keep CPU load balanced across active servers within a data center.
- **Traffic Manager** uses global signals including CPU utilization, HTTP request latency, and bandwidth utilization to issue rebalancing decisions across data centers. Cloudflare states that it has safety limits intended to prevent overly large traffic shifts and that it considers expected load at destination locations.

The affected HTTP rate-limiting path was used in a new DDoS mitigation mechanism combining rate limits and cookies.

---

## Incident-level outcome

Cloudflare reports that two independent events increased latency and error rates for Internet properties and Cloudflare services for 114 minutes.

During the peak 30-minute impact:

- approximately 1.4–2.1% of HTTP requests to Cloudflare's CDN received a generic error page;
- p99 Time To First Byte latency rose to almost three times its prior level.

The two reported events were:

1. automated network monitoring detected degradation and rerouted traffic suboptimally, creating backbone congestion between approximately 17:33 and 17:50 UTC;
2. a newly deployed DDoS mitigation mechanism exposed a latent bug in the rate-limiting system, allowing a particular request form to put a request-handling process into a non-terminating loop.

The postmortem focuses mainly on the second event.

---

## Deployment timeline

All times below are UTC on 2024-06-20.

- **14:14:** gradual deployment of the new DDoS rule began.
- **17:06:** deployment reached all data centers.
- **17:47:** first request-handling process entered the poisoned/non-terminating state.
- **18:04:** incident automatically declared after sustained high global CPU load.
- **18:34:** engineers showed that restarting the service recovered one server; a full restart was tested in one data center.
- **18:44:** CPU load normalized in that data center after restart.
- **18:51:** repeated global reloads/restarts began for servers with many stuck processes.
- **19:05:** HTTP error rate peaked; Traffic Manager began actions that helped recover service.
- **19:11:** service-unavailable HTTP error rate had roughly halved.
- **19:27:** global HTTP error rate returned to baseline.
- **19:29:** the DDoS rule deployment was identified as the likely trigger for process poisoning.
- **19:34:** the DDoS rule was fully disabled.
- **19:43:** engineers stopped routine restarts on heavily affected servers.
- **20:16:** incident response stood down.

---

## Failure mechanism described by Cloudflare

The new DDoS mitigation path:

1. checked for a valid cookie;
2. for a valid cookie, added a rate-limit rule based on the cookie value;
3. later evaluated the generated rate-limit rules.

Cloudflare reused existing rate-limit key-generation logic.

The postmortem identifies two interacting software problems:

- internally generated rate-limit rules used an API path in an unanticipated way, causing the parent key generator to point back to the same cookie-key function;
- a second cookie-validation function could disagree with the earlier validation when a request contained multiple cookies with mixed validity.

Under the triggering request, the key-generation function called itself repeatedly.

Because the Lua implementation used proper tail calls, the recursion did not necessarily grow the call stack until failure. Instead, the request-handling process could remain in a loop consuming 100% CPU.

A process that entered this state stopped serving later requests.

---

## Failure propagation described by Cloudflare

Each server had many request-handling processes, so one poisoned process alone had limited effect.

As more processes became CPU-saturated:

1. Unimog shifted new traffic away from higher-load servers toward servers with more available capacity.
2. Rising CPU utilization at a data-center level caused Traffic Manager to redirect traffic toward other data centers.
3. Redirected traffic included requests capable of poisoning processes, spreading the same failure condition to previously less-affected servers/data centers.

Cloudflare reports that this made healthy destination capacity progressively harder to find.

Traffic Manager's built-in safety limits also constrained how much additional traffic could be shifted.

At one point reported in the postmortem, approximately 10% of HTTP-request capacity in Western Europe and 4% in Eastern Europe was CPU-saturated.

---

## Incident-response information

Automatic alerting notified engineers when sustained global CPU utilization crossed a threshold.

Many incident responders were already engaged with the separate backbone-congestion incident.

In the early investigation, responders considered whether the high CPU condition was related to the existing network incident.

The source says it took time to notice that the highest-CPU locations were receiving the *lowest* traffic, which moved investigation away from the network event as the initiating cause.

Responders then pursued two parallel activities:

- determine whether restarting poisoned processes would recover them and perform broader restarts;
- identify what triggered processes to enter the CPU-saturated state.

Cloudflare reports that it took about 25 minutes after incident declaration to validate restart recovery on a sample server, followed roughly five minutes later by broader restarts.

---

## Additional Traffic Manager failure

During the same incident conditions, a latent bug in Traffic Manager was also triggered.

Cloudflare says Traffic Manager attempted a graceful restart after the exception, which halted its activity.

The bug first triggered at approximately 18:17 UTC and then repeatedly between 18:35 and 18:57.

During two reported intervals—approximately 18:35–18:52 and 18:56–19:05—Traffic Manager issued no new traffic-routing actions.

This left significant traffic rerouted away from locations whose request service had already begun recovering.

Alerting notified the Traffic team; Cloudflare reports that by 19:05 the team had written, tested, and deployed a fix.

---

## Immediate mitigation

Cloudflare used repeated rolling/global restarts of the affected request-handling service while investigating the trigger.

The new DDoS rule was rolled back/disabled globally.

Cloudflare stated that the rule would remain disabled until the broken cookie-validation condition was fixed and the recurrence risk addressed.

---

## Intentionally withheld source material for Pilot 002

The primary postmortem contains a follow-up/remediation section after the immediate mitigation.

For this editorial discovery test, those proposed future changes are intentionally omitted from the evidence packet.

Review methods know that source-authored follow-up material has been withheld, but they do not receive its contents.

This artificial omission is designed only to test whether the review prompts can derive useful actions from the architecture, timeline, failure mechanism, propagation, response, and immediate mitigation. It is **not** a representation of how a real incident reviewer should ignore available evidence.

---

## Explicit unknowns / unavailable information

The packet does **not** provide:

- internal code or full architecture;
- detailed organizational ownership boundaries;
- complete rollout criteria, canary size, or promotion thresholds;
- unit/integration/test coverage before deployment;
- exact monitoring/alert thresholds;
- customer-by-customer impact distribution;
- detailed incident command structure;
- staffing or workload details beyond responders already working another incident;
- cost estimates for remediation options;
- full chronology for the first network-congestion event;
- proof that the listed remediations were later implemented or effective;
- a complete dependency graph;
- a formal safety/control analysis;
- independent verification of Cloudflare's account.

Review methods should identify needed missing information rather than inventing it.

---

## Evidence-status boundary

Treat the packet as:

- **SOURCE-REPORTED OBSERVATION** for Cloudflare's stated metrics, timeline, architecture, failure mechanism, and remediation;
- **UNKNOWN** for facts not supplied;
- **ANALYTICAL INFERENCE** for any causal or design conclusion produced by a review method.

No claim in the pilot should be described as independently established merely because it appears in this packet.
