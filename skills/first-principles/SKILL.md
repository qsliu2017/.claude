---
name: first-principles
description: Apply first principles thinking to software engineering decisions. Use this skill when the user is facing architecture choices, technology selection, system design tradeoffs, debugging complex issues, evaluating whether to build vs buy, or questioning why a system works the way it does. Also trigger when the user says things like "should we use X or Y", "why is this so complex", "do we really need this", "help me think through this", or is stuck on a design decision and needs structured reasoning rather than pattern-matching to existing solutions.
---

# First Principles Thinking for Software Projects

Help the user break down software problems to their fundamental truths and reason up from there, rather than defaulting to convention or analogy.

## When This Matters

Convention-based thinking ("everyone uses X") is efficient for routine work. First principles thinking is worth the extra effort when:

- The decision has lasting consequences (architecture, data model, core abstractions)
- Existing approaches feel wrong but you cannot articulate why
- You are choosing between multiple plausible options with real tradeoffs
- A system has grown complex and you need to decide what to simplify
- You are debugging a problem where surface-level fixes keep failing

## Read the room first

Before diving into decomposition, assess how much thinking the user has already done. If they hand you a detailed spec or a well-reasoned comparison, do not re-derive everything from scratch -- that wastes their time. Instead, focus on finding blind spots: assumptions they did not question, dependency chains they did not trace, constraints they accepted without evidence. The less thinking they have done, the more structure you provide. The more they have done, the more you act as a stress-tester.

## The Process

### 1. Name the actual problem

State what you are trying to solve in concrete terms. Not "we need a message queue" but "we need to process user uploads without blocking the request." The solution is not the problem.

Ask: What outcome does the user/system actually need?

### 2. Decompose into fundamentals

Break the problem into its irreducible parts. For a software system, these are typically:

- **What data** exists and how it relates
- **What operations** must happen and in what order
- **What constraints** are real (latency, cost, team size, compliance) vs assumed
- **What guarantees** are required (consistency, availability, durability)

### 3. Challenge assumptions

For each component, ask:

- *Is this actually required, or are we carrying it forward from a previous decision?*
- *What evidence supports this constraint?*
- *What would we do if this assumption were false?*

Two techniques that sharpen this step:

**Trace dependency chains.** When one choice forces several others, name the chain explicitly. "Choosing DuckLake requires a Postgres catalog, which requires a proxy worker to hide credentials, which requires..." makes the true cost of a decision visible. Often the first choice in the chain is the one worth questioning.

**Quantify, do not hand-wave.** Vague comparisons ("Kafka is overkill") are less convincing than concrete ones ("10k events/day is 6 orders of magnitude below where Kafka's operational cost starts paying for itself"). Use actual numbers from the user's context -- their throughput, team size, request volume, budget. When you do not have a number, ask for it.

Common assumptions worth questioning in software:

- "We need a database for this" -- maybe a file or in-memory store is enough
- "This needs to be real-time" -- maybe near-real-time or batch is fine
- "We should use a microservice" -- maybe a module boundary is sufficient
- "We need to support X scale" -- maybe current scale is the right target
- "This is too complex to change" -- maybe the complexity is in your mental model, not the system

### 4. Build up from what remains

After stripping away assumptions, construct the simplest solution that satisfies the real constraints. Add complexity only when a concrete requirement demands it, not because "we might need it later."

For each piece of complexity you removed, name the specific condition that would justify adding it back. This gives the user a decision framework they can use later without re-doing the whole analysis. For example: "Use a simple Postgres queue now. Revisit when you are processing more than 50k jobs/hour or need fan-out to multiple independent consumers."

### 5. End with a falsifiable question

Close with one or two questions the user can actually answer to validate your recommendation. These should be concrete and checkable, not rhetorical.

Good: "In the last 3 months, how many times did your staging environment catch a bug that unit tests missed?"
Good: "What is your actual p99 latency requirement? Has a customer ever complained about the current speed?"
Bad: "Does this architecture align with your long-term vision?"

This forces the discussion out of the abstract and into evidence. It also gives the user a clear next step.

## Applying It

When the user brings a decision or problem, walk through these steps conversationally. Be direct about which assumptions look questionable. Use concrete questions, not abstract frameworks.

Good: "You said you need Kafka -- your current throughput is 10k events/day. That is one event every 8 seconds. A Postgres table with a polling worker handles that trivially. What specific property of Kafka do you need that a database row does not give you?"

Bad: "Let us apply the first principles framework to decompose your messaging requirements."

Keep the focus practical. The goal is a better decision, not a philosophy exercise.
