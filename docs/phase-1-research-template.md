# Phase 1 Research Template

Use this template to structure subject research before model implementation.

## 1. Research Goal

- What decision does this research support?
- What are we trying to prove or disprove?

## 2. Sources

Track references (papers, blog posts, docs, repos).

- Source 1:
  - Type:
  - Title:
  - Link:
  - Key takeaway:
- Source 2:
  - Type:
  - Title:
  - Link:
  - Key takeaway:
- Source 3:
  - Type:
  - Title:
  - Link:
  - Key takeaway:

## 3. Domain Rules Collected

Capture penalty shootout mechanics used by the environment.

- Kicker action constraints:
- Goalkeeper action constraints:
- Episode start conditions:
- Episode terminal conditions:
- Stochastic elements:

## 4. Candidate Algorithms

- IPPO:
  - Why consider it:
  - Pros:
  - Cons:
  - Decision:
- MAPPO:
  - Why consider it:
  - Pros:
  - Cons:
  - Decision:
- Other:
  - Why consider it:
  - Pros:
  - Cons:
  - Decision:

## 5. Observation and Action Design Notes

- Candidate observation variables per agent:
- Candidate action spaces per agent:
- Information asymmetry choices:
- Potential leakage risks:

## 6. Reward Design Notes

Keep reward logic independent from training code.

- Candidate reward terms:
- Risk of reward hacking:
- Sparse vs dense reward trade-off:
- Chosen reward draft:

## 7. Evaluation Protocol Draft

Define evaluation before training.

- Fixed seed list:
- Opponent pool definition:
- Metrics:
- Number of episodes per evaluation run:
- Statistical reporting method:

## 8. Decisions and Rationale

Document what is selected and why.

- First baseline algorithm:
  - Options considered:
  - Selected option:
  - Why:
- Observation design:
  - Options considered:
  - Selected option:
  - Why:
- Reward structure:
  - Options considered:
  - Selected option:
  - Why:

## 9. Open Questions

1.
2.
3.

## 10. Next Actions

- [ ] Finalize algorithm baseline selection.
- [ ] Finalize observation/action specification.
- [ ] Finalize reward draft for environment module.
- [ ] Prepare Phase 2 implementation tasks.
