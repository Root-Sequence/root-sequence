# User-Configurable Cognitive Interfaces

A **user-configurable cognitive interface** is software whose structure can be shaped around how a person thinks, works, remembers, and moves between contexts, rather than forcing everyone through the same fixed menu hierarchy.

This goes beyond themes, font sizes, or rearrangeable toolbars. The interface itself can become a configurable cognitive environment.

A person might be able to say:

> Keep project capture visible. Put files and search near the top. Hide features I rarely use. When we are discussing an idea, show me buttons for the projects it might belong to.

The system could translate that request into an interface configuration while keeping the user in control of what changed.

## The motivating interaction: "BHIG?"

A simple example is a persistent project-routing button:

`BHIG?`

During a conversation, pressing it could take the current thought, selected passage, or recent exchange and ask the system to:

1. decide whether it meaningfully belongs in BHIG;
2. suggest the best location;
3. identify existing related material;
4. propose whether to merge, cross-link, or create something new;
5. show the proposed change before any destructive or public action.

The same pattern could support:

`BHIG?` · `RaeLog?` · `No One Noticed?` · `Community Infrastructure?` · `Save as seed` · `Cross-reference`

The important thing is that these are not merely shortcuts to folders. They are **semantic routing controls**. The interface knows what the destination means and can help integrate the thought rather than just copying text somewhere.

## Conversational interface configuration

Traditional customization requires users to understand the application's own configuration model first. They must find the correct settings screen, learn which options exist, and translate their preferences into whatever controls the designer anticipated.

A language-capable system creates another possibility: describe the desired interaction directly.

Examples:

- "Always keep my project-routing controls visible."
- "Do not show voice controls in my work layout."
- "When I attach a file, put file actions next to the conversation instead of in a separate menu."
- "Give research chats more screen space and hide decorative elements."
- "Keep the same basic layout on desktop and iPad so my muscle memory transfers."
- "For this project, show BHIG, RaeLog, and Root Sequence actions. For everything else, hide them."

The system can translate intent into configuration without requiring the person to become an interface administrator.

## Defaults are governance

Customization does not remove the importance of defaults.

Most users will not redesign an interface from first principles. Many will never change a default at all. Even highly configurable software therefore makes political and behavioral choices through what appears first, what is emphasized, what requires extra effort, and what is hidden.

Defaults influence:

- which actions feel normal;
- which capabilities are discoverable;
- which information receives attention;
- how much friction exists before a consequential action;
- whether privacy is protective or extractive by default;
- whether accessibility is assumed or treated as an exception;
- whether publishing, sharing, saving, deleting, or buying is the path of least resistance;
- whether the system rewards reflection or immediacy.

A default is not neutral because it is common.

A humane customizable system therefore needs two things at once:

1. **carefully designed defaults** that work without configuration; and
2. **meaningful user authority** to depart from those defaults.

## Stable substrate, flexible surface

An interface that constantly rearranges itself can be worse than a rigid one. Muscle memory, accessibility, spatial memory, and predictability matter.

The system should distinguish between a stable substrate and a flexible surface.

The stable substrate might include:

- navigation that does not silently move;
- predictable locations for safety-critical actions;
- consistent keyboard and assistive-technology semantics;
- stable undo and history controls;
- clear indication of what context or project is active;
- reliable access to privacy and account controls;
- a way to return to a known baseline.

The flexible surface might include:

- project-specific shortcuts;
- contextual action buttons;
- panels that appear only for relevant tasks;
- preferred density and information hierarchy;
- custom commands and workflows;
- different layouts for writing, research, coding, planning, or casual conversation.

The goal is not an interface that shape-shifts constantly. It is an interface that can become **personally legible without becoming unstable**.

## User authority over adaptation

An AI-capable interface should not interpret "adaptive" as permission to redesign itself whenever it predicts a preference.

Useful adaptation should be:

- inspectable;
- reversible;
- attributable;
- easy to pause;
- easy to reset;
- preferably previewable when a change is substantial.

A system might suggest:

> You use project routing frequently in these conversations. Add it to your persistent toolbar?

That is different from silently moving the toolbar.

The user should be able to ask:

- Why is this here?
- What changed?
- When did it change?
- Restore the previous layout.
- Never adapt this area automatically.
- Export my configuration.

## Project-aware interfaces

Projects are not merely folders. They can contain different vocabularies, sources, workflows, privacy rules, and definitions of "done."

A project-aware interface could expose controls relevant to the active conceptual environment.

For BHIG, contextual actions might include:

- `BHIG?`
- `Edge cases`
- `Power check`
- `Source this`
- `Cross-link`
- `Public-treatment candidate`

For RaeLog:

- `Draft privately`
- `Find related entries`
- `Capture provenance`
- `Anti-slop pass`
- `Stage for review`

For a software repository:

- `Open issue`
- `Create branch`
- `Run tests`
- `Document decision`

The interface becomes a visible layer over the project's own logic instead of forcing every project into generic chat controls.

## Semantic buttons, not macro buttons

A macro repeats a fixed sequence. A semantic button expresses intent.

`BHIG?` does not necessarily mean "append this text to BHIG.md." It means something closer to:

> Evaluate this material against the structure and purpose of BHIG, then help route it appropriately.

Depending on context, the correct result could be:

- no action because the idea is already represented;
- a cross-link to an existing seed;
- a paragraph added to an existing document;
- a new seed;
- an unresolved question;
- a source note;
- a suggestion that the material belongs elsewhere.

This makes the control compact without making the underlying operation simplistic.

## Accessibility is part of the architecture

Customization should not assume that every person benefits from greater visual density, animation, dynamic placement, tiny controls, drag-and-drop interaction, or hidden gestures.

The same semantic interface should remain operable through:

- keyboard navigation;
- screen readers;
- switch and alternative input systems;
- voice where appropriate;
- touch targets with adequate size and spacing;
- reduced motion;
- high zoom and text scaling;
- simplified or low-stimulation layouts.

User configuration can itself be an accessibility tool, but only if the customization system is accessible too.

## Privacy and local knowledge

A deeply personalized cognitive interface may contain unusually revealing information about how a person works, what projects matter to them, which controls they use, and which contexts trigger certain workflows.

That configuration should not casually become behavioral telemetry.

Prefer:

- local or user-controlled storage where feasible;
- explicit sync boundaries;
- understandable export and deletion;
- separation between configuration needed to serve the user and analytics desired by the provider;
- no requirement to surrender project contents merely to personalize layout;
- clear distinction between device-specific and account-wide preferences.

A cognitive environment can become intimate infrastructure. Treat it accordingly.

## Defaults should remain opinionated, but contestable

There is a temptation to respond to the politics of defaults by removing all opinion from the default interface. That usually produces a worse product.

Defaults still need to be coherent, learnable, safe, and accessible. The question is not whether designers make choices. They necessarily do.

The better standard is:

> **Make good default choices, expose the assumptions behind consequential ones, and give users meaningful ways to disagree.**

This treats interface design as stewardship rather than hidden behavioral governance.

## A possible minimum viable version

A first implementation does not require a fully generative GUI.

It could begin with:

1. a persistent customizable action bar;
2. user-defined semantic actions such as `BHIG?`;
3. per-project action sets;
4. natural-language configuration of which actions appear where;
5. a visible change log for interface changes;
6. one-click undo and reset;
7. an exportable configuration file;
8. accessibility-safe layout constraints that customization cannot silently break.

A later system could generate more of the interface, but the underlying principles would already be testable.

## Relationship to Root Sequence

This concept connects several Root Sequence concerns:

- **agency:** software should increase a person's practical ability to act rather than demand adaptation to a designer's workflow;
- **cognitive sovereignty:** personalization should serve the user's thinking rather than optimize their behavior for an external objective;
- **accessibility:** different bodies and minds should not be forced through one supposedly neutral interface;
- **legibility:** systems should expose how they are configured and why;
- **liberated intelligence:** an intelligent system can help translate intent into tools without claiming authority over the intent itself;
- **humane infrastructure:** defaults, reversibility, privacy, and user control are architectural questions, not optional polish.

## Possible implementation homes

The concept can remain canonical in Root Sequence while producing experiments elsewhere.

A Dev11 implementation could test:

- a standalone AI workspace shell;
- a browser extension that adds user-defined semantic routing actions;
- a project-aware command palette;
- a local-first configuration format for AI interfaces;
- a prototype routing layer shared by tools such as RaeLog and BHIG capture workflows.

The implementation should stay separate from the principle so one experimental UI does not become the definition of the idea.

## See also

- [What is intelligence?](what-is-intelligence.md)
- [What is liberation?](what-is-liberation.md)
- [What is personal anarchism?](what-is-personal-anarchism.md)
- [Being Human(e) Atlas](https://github.com/Root-Sequence/beinghumane-atlas)

> An interface is part of the environment in which thought becomes action. Users should have more say in shaping that environment.
