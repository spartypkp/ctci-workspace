# Suggested Study Plan

This workspace is optimized for spaced repetition and deliberate practice. The plan below is
opinionated by design—adapt it if your interview timeline requires a different cadence.

## Weekly Rhythm

1. **Foundations (2 sessions)** – Pick one data structure heavy problem and one algorithmic
   pattern problem. Use the journal template to capture your approach.
2. **Design / Theory (1 session)** – Rotate across system design, databases, concurrency, and
   object-oriented design chapters. Focus on sketching diagrams and rehearsing communication.
3. **Mixed Review (1 session)** – Revisit a solved problem from at least two weeks ago. Implement
   the solution again from scratch without peeking.
4. **Stretch Goal** – Attempt one Hard or Moderate question without time pressure. Treat it as a
   research session where you write down new patterns or helper utilities you want to build.

## Daily Loop

Each practice slot is 60–90 minutes and follows these checkpoints:

- **5 minutes** – Read the prompt, note clarifying questions, and list constraints.
- **20 minutes** – Brainstorm multiple approaches. Compare complexities and implementation risk.
- **30 minutes** – Implement the most promising solution. Commit your work locally even if
  incomplete so you can review history later.
- **10 minutes** – Write tests or articulate manual test cases. Capture bugs found during testing.
- **Remaining time** – Update your journal entry with insights, follow-up ideas, or alternate
  approaches you want to revisit.

## Rotation Guidance

Use the `make problems` command to print the full catalog. Track completed problems in your notes
and bias towards variety:

- Alternate between chapters instead of grinding one chapter at a time.
- Pair a conceptual/design exercise with an implementation-heavy one in the same week.
- Schedule a recurring review slot to revisit previously solved questions. Aim for a 2-1-1 split:
  two brand new problems, one redo, and one design drill every week.

## Retrospectives

At the end of each week, pick one solved problem and do a deep retrospective:

1. Write a short explanation as if you were teaching the concept to someone else.
2. Capture what signals would tell an interviewer that you have mastered the topic.
3. Identify tooling or utility functions you could build to make future problems faster.

Keep these retrospectives in the `notes/` directory so you can spot improvement trends over time.
