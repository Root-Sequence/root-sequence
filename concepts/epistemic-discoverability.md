# Epistemic Discoverability and Knowledge Routing

**Document role:** Working cross-domain design concept  
**Status:** Active / developing; AI-assisted synthesis for author review, 2026-09-24  
**Canonical scope:** Shared Root Sequence treatment of how people discover, navigate, evaluate, and build knowledge when they do not yet know the field's vocabulary or structure.  
**Evidence boundary:** The component ideas have established predecessors in information retrieval, information foraging, sensemaking, learning sciences, epistemic-agency research, libraries, HCI, and knowledge organization. This page proposes a Root Sequence synthesis and design vocabulary; it does not claim novelty for those components or establish one universal model of learning.

## Core idea

Knowledge can be public, searchable, and technically available while remaining **practically undiscoverable** to a person who does not yet know:

- the right term;
- the field that studies the question;
- which source type is trustworthy;
- which scholar/community uses different vocabulary;
- which adjacent concept would provide the next search term;
- whether they are interpreting the question at the right scale.

Root Sequence calls this problem **epistemic discoverability**:

> **Can a person move from the concepts and questions they currently possess toward relevant knowledge they do not yet know how to name?**

The companion concept is **knowledge routing**:

> **helping a question reach the field, method, community, source, or vocabulary best equipped to develop it—without forcing every question through one ontology or authority.**

This is related to, but distinct from:

- finding one known document;
- answering a factual query;
- teaching a fixed curriculum;
- ranking search results;
- recommending popular content;
- summarizing what an expert already knows.

The difficult case is:

> **I can feel the question, but I do not yet have the language required to search for it.**

---

## 1. Why vocabulary is infrastructure

Furnas, Landauer, Gomez, and Dumais's 1987 **Vocabulary Problem** demonstrated extreme variability in the words people spontaneously choose for the same objects/actions. Their study found that, across several domains, the probability that two people independently favored the same term was below 0.20.

Source:

- G. W. Furnas, T. K. Landauer, L. M. Gomez, S. T. Dumais, "The Vocabulary Problem in Human-System Communication," *Communications of the ACM* 30(11), 1987, 964–971. DOI: 10.1145/32206.32212

The immediate HCI lesson was that interfaces relying on one designer-selected vocabulary impose enormous first-try failure.

The broader Root Sequence lesson is:

> **Knowing the phenomenon is not the same as knowing the canonical name for it.**

A person can have a valid intuition while lacking:

- disciplinary terminology;
- historical names;
- alternate spellings;
- current preferred vocabulary;
- technical jargon;
- the name of a neighboring field.

Knowledge systems that require the user to supply the expert's exact phrase **before helping them discover the expert vocabulary** impose a hidden prerequisite.

That is an agency problem.

---

## 2. Search needs can change while searching

Marcia Bates's **berrypicking** model of information seeking rejects the assumption that a researcher starts with one stable query that merely needs a better result.

In real research:

- one source introduces a new term;
- that term reveals a field;
- the field changes the researcher's understanding of the question;
- the new understanding changes the query;
- useful fragments accumulate across many sources rather than in one final answer.

Source:

- Marcia J. Bates, "The Design of Browsing and Berrypicking Techniques for the Online Search Interface," *Online Review* 13(5), 1989. Author-hosted version: https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html

This is almost a perfect description of the September 24 Root Sequence research path.

The query did not merely become **better formulated**.

The researcher's **question-space changed**.

That means a good knowledge environment should preserve:

- evolving queries;
- concepts learned along the way;
- sources that triggered a change of direction;
- abandoned branches;
- useful partial answers;
- new unknowns produced by earlier answers.

---

## 3. Information foraging and “information scent”

Pirolli and Card's **Information Foraging Theory** analyzes how people seek valuable information in environments where information occurs in patches and where proximal cues help indicate whether a path is worth following.

Source:

- Peter Pirolli & Stuart Card, "Information Foraging," *Psychological Review* 106(4), 1999, 643–675. DOI: 10.1037/0033-295X.106.4.643

A knowledge interface therefore has a design problem analogous to navigation:

> What cues tell the person that this concept, source, citation, field, scholar, or community might lead somewhere useful?

Examples of **epistemic scent** may include:

- "This is the field that studies the pattern you're describing";
- related terms and aliases;
- why a source is relevant;
- disagreement between fields;
- what prerequisite concept unlocks the next source;
- "start here" routes;
- citation trails;
- examples that connect unfamiliar terminology to the person's existing model.

A link dump has low epistemic scent.

A good Reading Trail explains **why you might want to click**.

---

## 4. Sensemaking is representation-building

Russell, Stefik, Pirolli, and Card describe sensemaking as the process of searching for a useful representation and encoding information within it to answer task-specific questions.

Source:

- Daniel M. Russell, Mark J. Stefik, Peter Pirolli, Stuart K. Card, "The Cost Structure of Sensemaking," INTERCHI '93. DOI: 10.1145/169059.169209

That matters because information access is not sufficient.

A researcher may have:

- the papers;
- the data;
- the vocabulary;

and still lack a representation that makes the relationships intelligible.

Root Sequence frequently supplies:

- concept maps;
- distinction tables;
- timelines;
- state/transition models;
- Idea Trails;
- project maps;
- provenance graphs;
- Reading Trails.

These are not merely prettier summaries.

They can be **sensemaking infrastructure**.

The danger is equally important:

> A compelling representation can make a weak theory feel finished.

So every map should preserve:

- uncertainty;
- contested relationships;
- source boundaries;
- analogy versus mechanism;
- missing evidence;
- alternatives.

---

## 5. Epistemic agency already exists as a research concept

**Epistemic agency** is established terminology in learning-sciences and education research.

Different formulations emphasize learners' ability and responsibility to:

- shape knowledge-building;
- decide what questions matter;
- evaluate evidence;
- construct or transform knowledge;
- participate as producers rather than passive recipients of knowledge.

Examples:

- Nieminen & Ketonen (2024), "Epistemic agency: a link between assessment, knowledge and society," *Higher Education* 88, 777–794. DOI: 10.1007/s10734-023-01142-5
- Odden et al. (2023), work on disciplinary epistemic agency in undergraduate science.
- science-education traditions drawing on Scardamalia, Bereiter, Stroupe, and others.

Root Sequence therefore should **not** claim coinage of epistemic agency.

Its local question is narrower and infrastructural:

> **What properties of a knowledge environment expand or suppress people's ability to exercise epistemic agency?**

That includes discoverability.

---

## 6. From unknown unknown to navigable question

One useful trajectory is:

    felt pattern / curiosity
            ↓
    ordinary-language question
            ↓
    candidate concepts
            ↓
    terminology / aliases
            ↓
    fields / communities
            ↓
    overview sources
            ↓
    primary literature
            ↓
    competing theories
            ↓
    methods / evidence
            ↓
    revised question
            ↺

A failure can occur at every transition.

Examples:

### Vocabulary failure

The user searches "system keeps doing what used to work" but never learns **path dependence**, **maladaptation**, **lock-in**, **double-loop learning**, or **adaptive trap**.

### Field-routing failure

The user finds generic productivity writing instead of resilience engineering or organizational learning.

### Authority failure

Popular SEO material outranks the primary scholar/archive.

### Representation failure

The person finds fifty papers but no map showing which questions they answer.

### Gatekeeping failure

The introductory source assumes vocabulary learned only after taking several courses.

### Interface failure

A system answers the current query so completely that it hides the surrounding field and terminates exploration.

### Recommendation capture

An algorithm repeatedly serves material similar to what the user already consumes, reducing encounter with genuinely different intellectual traditions.

---

## 7. Epistemic discoverability is not maximum exposure

More information is not automatically better.

A system that exposes every possible related concept can destroy discoverability through overload.

Good epistemic routing must balance:

- novelty;
- relevance;
- cognitive load;
- uncertainty;
- serendipity;
- depth;
- accessibility;
- provenance.

The goal is not:

> show everything.

It is:

> **make the next useful intellectual moves visible without pretending there is only one path.**

---

## 8. Progressive epistemic legibility

This concept extends [Legible Systems](legible-systems.md).

A progressively legible knowledge environment can support movement such as:

    intuition
       ↓
    ordinary explanation
       ↓
    canonical terminology
       ↓
    field map
       ↓
    overview
       ↓
    original sources
       ↓
    methods
       ↓
    disagreements
       ↓
    technical depth
       ↓
    contribution

A newcomer should not need expert vocabulary before they can discover the vocabulary.

An expert should not be trapped behind simplified explanations that hide primary evidence.

> **Concept first; term second; source third; mechanism underneath.**

Not always literally in that sequence—but all should remain reachable.

---

## 9. Design principles

### 1. Accept the language the person has

Do not require canonical terminology as the admission ticket.

Map:

- ordinary phrases;
- aliases;
- historical names;
- technical terms;
- neighboring-field vocabulary.

### 2. Explain why a route is relevant

"This field studies X because..." is more useful than a bare link.

### 3. Preserve query evolution

Let the research question change visibly rather than pretending the first formulation was final.

### 4. Show neighboring disciplines

A phenomenon may have:

- biological;
- technical;
- social;
- philosophical;
- historical;
- political;
- design;

treatments that should not be collapsed.

### 5. Route to native methods

Once the mechanism is identified, point to the discipline that actually studies it.

### 6. Preserve primary-source paths

A summary should not sever the route to:

- papers;
- books;
- datasets;
- archives;
- standards;
- original authors;
- code.

### 7. Surface disagreement

Do not make the knowledge graph falsely smooth.

Show:

- competing definitions;
- rival theories;
- controversy;
- different disciplinary assumptions.

### 8. Preserve serendipity without surrendering to engagement optimization

Recommendation should support useful surprise, not endless retention.

### 9. Make provenance visible

Why is this source here?

Who produced it?

What role is it playing?

### 10. Support stopping

Epistemic agency includes deciding:

> I know enough for this purpose.

The interface should not turn curiosity into compulsory infinite consumption.

---

## 10. Reading Trails as epistemic infrastructure

[Reading Trails](../research/reading-trails/README.md) began as a way to preserve interesting resources encountered during research.

This concept gives them a deeper function.

A Reading Trail can act as a **bridge between vocabulary states**.

Instead of:

    list of links

it can preserve:

    question
      ↓
    concept
      ↓
    why it matters
      ↓
    field
      ↓
    approachable entry point
      ↓
    deeper sources
      ↓
    adjacent rabbit holes

That is epistemic infrastructure.

Reading Trails are not intended to replace:

- libraries;
- search engines;
- bibliographies;
- academic databases;
- textbooks.

They complement them by preserving the **route into the field**.

---

## 11. Root Sequence as a knowledge router

The maintained [Why Root Sequence?](root-sequence.md) page now describes RS as a conceptual commons and routing/synthesis layer.

Epistemic discoverability makes one aspect of that role explicit.

Given a question such as:

> Why does a system keep doing something that used to work?

Root Sequence might route:

- **path dependence** — historical/institutional analysis;
- **maladaptation** — biological/ecological/psychological contexts;
- **double-loop learning** — organizational learning;
- **ultrastability** — cybernetics;
- **allostasis** — biological stress regulation;
- **lock-in** — economics/institutions/technology;
- **adaptive trap** — domain-specific use;
- **resilience engineering** — socio-technical systems.

The output should not be:

> They are secretly all the same phenomenon.

It should be:

> **You are noticing a family resemblance. Here are the fields that study different mechanisms inside that resemblance.**

That is knowledge routing.

---

## 12. AI and epistemic agency

AI can lower the vocabulary barrier dramatically.

A person can describe:

> "the thing where an organization keeps repeating a strategy that used to work but conditions changed"

and receive possible routes such as:

- path dependence;
- organizational inertia;
- double-loop learning;
- maladaptation;
- lock-in;
- competency traps.

That is powerful.

But AI can also destroy epistemic agency by:

- presenting synthesis without sources;
- selecting one interpretation too early;
- hiding alternatives;
- using authoritative language for uncertain mappings;
- summarizing away disagreement;
- answering instead of teaching how to continue inquiry;
- making the user dependent on the model as the only route to knowledge.

The design objective should therefore be:

> **AI that expands the user's ability to navigate knowledge without making itself the permanent gatekeeper of that navigation.**

This strongly connects to:

- Legible Systems;
- Wingbot;
- liberated intelligence;
- user-configurable cognitive interfaces;
- Reading Trails;
- agency vs automation.

---

## 13. Discoverability has politics

Knowledge access is shaped by:

- paywalls;
- language;
- academic prestige;
- search ranking;
- recommendation systems;
- institutional credentials;
- publication norms;
- library access;
- disability/accessibility;
- censorship;
- platform ownership;
- disciplinary siloing;
- who receives funding and preservation.

So epistemic discoverability is not only an interface problem.

Ask:

- Which knowledge becomes easy to encounter?
- Which requires insider vocabulary?
- Which is systematically buried?
- Whose classifications become canonical?
- Who controls indexing?
- Which archives disappear?
- Who can participate in producing knowledge?
- Which communities are treated as sources versus subjects?

A knowledge router must not pretend these conditions are neutral.

---

## 14. Design test

When evaluating a knowledge environment, ask:

1. Can someone begin from ordinary language?
2. Can they discover the field's preferred terminology?
3. Does the system recognize multiple plausible terms for the same target?
4. Can the query evolve as understanding changes?
5. Are neighboring disciplines visible without being falsely unified?
6. Can the user see why a suggested source/path is relevant?
7. Are primary sources reachable?
8. Is source role/provenance clear?
9. Are competing interpretations visible?
10. Are prerequisites explained or bridged?
11. Does the system support exploration without overwhelming the person?
12. Does it preserve unexpected but relevant discovery?
13. Can the user leave the AI/recommender and continue independently?
14. Does the environment help people create/evaluate knowledge, not merely consume answers?
15. Who or what controls the ranking/routing layer?
16. Which people or traditions become effectively undiscoverable under the current vocabulary/index?
17. Can someone stop with a useful partial understanding and return later without reconstructing the entire inquiry?

---

## 15. Relationship to other Root Sequence concepts

### Legible Systems

Legibility asks whether a system helps affected people understand and work with it.

Epistemic discoverability asks whether a **knowledge environment helps people find the concepts required to understand it in the first place**.

### Dynamic Coherence / Adaptive Continuity

New knowledge changes future search behavior.

A concept can alter the researcher's transition dynamics by making previously unavailable questions and resources reachable.

This is an epistemic example of history changing later possibility.

### Agency

Knowledge changes what actions can be perceived, evaluated, and enacted.

But knowledge alone does not erase material, institutional, bodily, or authority constraints.

### User-Configurable Cognitive Interfaces

Different people may need different routes through the same knowledge space.

### Legible AI-Assisted Expression

AI should make its synthesis, sources, transformations, and uncertainty inspectable.

### Reading Trails

Reading Trails are the first lightweight RS implementation of this concept.

---

## 16. Candidate future artifact: Conceptual Router

A possible future Root Sequence tool could accept a question in ordinary language and return a **routing graph**, not merely an answer.

Example:

    "Why does a system keep doing something that used to work?"
                  │
          ┌───────┴────────┐
          ↓                ↓
    historical lock-in    adaptive response
          │                │
    path dependence       maladaptation
    increasing returns    allostasis (biological)
    institutionalism      resilience
          │                │
          └───────┬────────┘
                  ↓
       organizational learning
                  │
          double-loop learning

For every route:

- what the term means;
- what field owns it;
- why it might fit;
- why it might **not** fit;
- best entry resource;
- deeper source;
- related RS material.

This would be closer to an **intellectual transit map** than a chatbot answer.

Do not build it until the Reading Trails and routing method have enough real use to justify the structure.

---

## 17. Research anchors

These sources support components of the model, not the whole Root Sequence synthesis.

- Furnas, Landauer, Gomez & Dumais (1987), "The Vocabulary Problem in Human-System Communication." DOI: 10.1145/32206.32212
- Bates (1989), "The Design of Browsing and Berrypicking Techniques for the Online Search Interface." https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html
- Pirolli & Card (1999), "Information Foraging." DOI: 10.1037/0033-295X.106.4.643
- Russell, Stefik, Pirolli & Card (1993), "The Cost Structure of Sensemaking." DOI: 10.1145/169059.169209
- Nieminen & Ketonen (2024), "Epistemic agency: a link between assessment, knowledge and society." DOI: 10.1007/s10734-023-01142-5

---

## Working principle

> **A knowledge system should not require someone to already possess the vocabulary, map, or institutional access that the system is supposed to help them acquire.**

And:

> **A good answer should increase the person's capacity to discover the next good question.**
