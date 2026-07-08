<!-- markdownlint-disable MD049 -->

# RL And MARL Mathematics Basics

This document is a compact math primer for RL first, then MARL.
It is designed to be read before implementation work.

## 1) RL mathematics basics

### 1.1 Markov Decision Process (MDP)

An MDP is defined by:

- State space: \(\mathcal{S}\)
- Action space: \(\mathcal{A}\)
- Transition model: \(P(s'\mid s,a)\)
- Reward: \(r(s,a)\)
- Discount factor: \(\gamma \in [0,1)\)

A policy is \(\pi(a\mid s)\).

### 1.2 Return

The discounted return from time \(t\) is:

\[
G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k+1}
\]

### 1.3 Value functions

State value:

\[
V^{\pi}(s) = \mathbb{E}_{\pi}[G_t \mid s_t=s]
\]

Action value:

\[
Q^{\pi}(s,a) = \mathbb{E}_{\pi}[G_t \mid s_t=s, a_t=a]
\]

### 1.4 Bellman expectation equations

\[
V^{\pi}(s) = \sum_a \pi(a\mid s) \sum_{s'} P(s'\mid s,a) \left[r(s,a,s') + \gamma V^{\pi}(s')\right]
\]

\[
Q^{\pi}(s,a) = \sum_{s'} P(s'\mid s,a) \left[r(s,a,s') + \gamma \sum_{a'} \pi(a'\mid s')Q^{\pi}(s',a')\right]
\]

### 1.5 Bellman optimality equations

\[
V^*(s) = \max_a \sum_{s'} P(s'\mid s,a) \left[r(s,a,s') + \gamma V^*(s')\right]
\]

\[
Q^*(s,a) = \sum_{s'} P(s'\mid s,a) \left[r(s,a,s') + \gamma \max_{a'} Q^*(s',a')\right]
\]

### 1.6 RL optimization targets

- Value-based methods approximate \(Q^*\).
- Policy-based methods maximize \(J(\theta)=\mathbb{E}_{\pi_\theta}[G_0]\).
- Actor-critic combines policy optimization with value estimation.

Policy gradient identity (high-level form):

\[
\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta}\left[\nabla_\theta \log \pi_\theta(a\mid s) \cdot A^{\pi}(s,a)\right]
\]

## 2) MARL mathematics basics

### 2.1 From MDP to Markov game

For \(n\) agents, define:

- Agents: \(\mathcal{N}=\{1,\dots,n\}\)
- State space: \(\mathcal{S}\)
- Joint action space: \(\mathcal{A}=\mathcal{A}_1\times\cdots\times\mathcal{A}_n\)
- Transition: \(P(s'\mid s, a_1,\dots,a_n)\)
- Rewards: \(r_i(s,a_1,\dots,a_n)\) for each agent \(i\)

Joint policy:

\[
\pi(a_1,\dots,a_n\mid s)=\prod_{i=1}^{n}\pi_i(a_i\mid o_i)
\]

### 2.2 MARL values

Agent-\(i\) state value under joint policy \(\pi\):

\[
V_i^{\pi}(s)=\mathbb{E}_{\pi}\left[\sum_{t=0}^{\infty}\gamma^t r_i^{(t)}\mid s_0=s\right]
\]

Agent-\(i\) joint-action value:

\[
Q_i^{\pi}(s,a_1,\dots,a_n)=\mathbb{E}_{\pi}\left[\sum_{t=0}^{\infty}\gamma^t r_i^{(t)}\mid s_0=s, a_0=(a_1,\dots,a_n)\right]
\]

### 2.3 Why MARL is mathematically harder

- Non-stationarity: opponent policies change during training.
- Credit assignment: hard to isolate one agent's contribution.
- Equilibrium selection: multiple stable solutions can exist.

### 2.4 Nash equilibrium

A joint policy \(\pi^*\) is Nash if no agent improves by unilateral deviation:

\[
V_i(\pi_i^*,\pi_{-i}^*) \ge V_i(\pi_i,\pi_{-i}^*) \quad \forall i, \forall \pi_i
\]

### 2.5 Two-player zero-sum minimax

For payoff \(V\) to player 1:

\[
\max_{\pi_1}\min_{\pi_2}V(\pi_1,\pi_2)=\min_{\pi_2}\max_{\pi_1}V(\pi_1,\pi_2)
\]

This gives a robust-game objective against strongest opponents.

### 2.6 CTDE objective intuition

Centralized Training, Decentralized Execution:

- Training critic can use global state and joint actions.
- Execution policy uses local observation only.

Typical policy gradient for agent \(i\):

\[
\nabla_{\theta_i}J_i=\mathbb{E}\left[\nabla_{\theta_i}\log\pi_i(a_i\mid o_i)\cdot A_i\right]
\]

### 2.7 Self-play and regret notions

- Self-play approximates adaptive opponents.
- Exploitability measures distance from equilibrium robustness.
- Regret minimization methods connect to equilibrium convergence in many settings.

## 3) What this means for your project

### 3.1 Environment math requirements

- Explicit per-agent state, action, reward definitions.
- Deterministic transitions under fixed seeds.
- Verified terminal and truncation logic.

### 3.2 Training math requirements

- Start with stable baseline objective (IPPO-like setup).
- Keep train and eval distributions separated.
- Track entropy, value targets, and variance for stability diagnosis.

### 3.3 Evaluation math requirements

- Evaluate against fixed and historical opponent pools.
- Report averages with dispersion (not only best run).
- Monitor regression and exploitability proxy trends.

## 4) Quick formula reference

- Return: \(G_t=\sum_{k=0}^{\infty}\gamma^k r_{t+k+1}\)
- RL value: \(V^{\pi}(s)\), \(Q^{\pi}(s,a)\)
- MARL value: \(V_i^{\pi}(s)\), \(Q_i^{\pi}(s,a_1,\dots,a_n)\)
- Nash condition: no profitable unilateral deviation
- Minimax identity in two-player zero-sum games
- Policy gradient score-function form
