dpct64-anomaly-app

Discrete Coherence Entropy Phase Anomaly Detection
using Unified Coherence Encoding Theory (UCET-64)

Overview

dpct64-anomaly-app is a structural anomaly detection system built on Discrete Phase Coherence Theory (DPCT-64) and Unified Coherence Encoding Theory (UCET-64).

The app detects anomalies, regime shifts, and emerging instabilities in time-indexed systems by measuring loss or distortion of coherence in a fixed 64-state phase lattice.

This system does not rely on semantic interpretation, labels, or predictive heuristics.
All signals are treated as cyclic or quasi-cyclic oscillators and evaluated strictly through invariant relational structure.

Core Principles

Final state space is fixed and finite: 64 discrete phase states

All observables are dihedral-invariant

Coherence is defined as persistence of phase-differential structure

Anomalies emerge as entropy spikes, coherence decay, or structural divergence

Forecasting is nearest-neighbor structural recurrence, not extrapolation

No meanings are assigned.
No symbolic interpretations are embedded.
Only structure survives.

What the App Does

Encodes time-indexed signals into a 64-state phase lattice

Computes phase differentials between oscillators

Segments time into sliding windows

Measures coherence and entropy per window

Persists canonical structural charts

Compares current structure to historical memory

Flags anomalies when coherence deviates beyond admissible bounds

dpct64-anomaly-app/
│
├── encoding/
│   ├── phase_encoder.py        # UCET phase encoding
│   ├── oscillator_map.py       # Period definitions
│
├── dynamics/
│   ├── differentials.py        # δ(si, sj)
│   ├── windows.py              # Sliding window logic
│   ├── histograms.py           # Differential histograms
│
├── coherence/
│   ├── metrics.py              # Pairwise & global coherence
│   ├── entropy.py              # Structural entropy measures
│
├── charts/
│   ├── chart.py                # Chart object
│   ├── canonicalize.py         # Dihedral canonicalization
│
├── storage/
│   ├── persist.py              # Append-only history
│   ├── load.py                 # History retrieval
│
├── comparison/
│   ├── distance.py             # Chart distance metrics
│   ├── neighbors.py            # Structural similarity search
│
├── app/
│   ├── pipeline.py             # End-to-end execution
│   ├── detect.py               # Anomaly detection logic
│
└── README.md

Mathematical Foundation (Brief)

Phase lattice:

𝑍
64
=
{
0
,
1
,
…
,
63
}
Z
64
	​

={0,1,…,63}

Quantization:

𝜃
∈
[
0
,
2
𝜋
)
→
𝑠
=
⌊
𝜃
/
(
2
𝜋
/
64
)
⌋
θ∈[0,2π)→s=⌊θ/(2π/64)⌋

Phase differential:

𝛿
(
𝑎
,
𝑏
)
∈
[
−
32
,
32
]
δ(a,b)∈[−32,32]

Coherence:
Concentration of differential histograms within structurally privileged bands

Entropy:
Dispersion of phase-differential distributions across windows

Anomaly:
Statistically significant deviation from historical coherence baselines

What Counts as an Anomaly

An anomaly is not a rare value.

An anomaly is a structural event, such as:

Sudden collapse of resonance bands

Rapid entropy inflation

Loss of persistence across windows

Structural divergence from all historical neighbors

Regime boundary crossing

What This Is Not

Not astrology

Not prediction by belief

Not semantic AI

Not symbolic pattern matching

Not continuous embeddings

Any external labels are used only as historical indexing, never as causal variables.

Use Cases

Time-series regime detection

System instability monitoring

Market or signal anomaly detection

Behavioral or biological rhythm analysis

Structural forecasting engines

Research into coherence-based systems

Status

Active development
Core pipeline implemented
Persistence and comparison complete
Forecasting module pending (structural recurrence only)

Philosophy

Coherence precedes meaning.
Structure precedes interpretation.
Memory precedes foresight.
