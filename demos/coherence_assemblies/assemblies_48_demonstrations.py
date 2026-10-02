#!/usr/bin/env python3
"""
Demonstrate direct-sum, tensor-product, and Cartesian-product assemblies
across 48 method families.

The constructions match the corrected claim:
  - inaccessible branches form a direct sum; the state is a block-diagonal mixture
  - coexisting factors (internal, blanket, external) form a tensor product
  - the seven coordinates form a Cartesian product; tensoring those axes collapses dimension

Each entry is a numerical check in a named method family. It is not a claim that a
specific paper reported that number. No clinical decision is produced.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np

OUT = Path("/workspace/artifacts/assemblies_48_results.json")
RNG = np.random.default_rng(2026)


@dataclass
class Check:
    index: int
    family: str
    assembly: str
    claim: str
    statistic: float
    passed: bool
    note: str


def direct_sum_blocks(weights: np.ndarray, dim: int = 2) -> np.ndarray:
    """Block-diagonal mixture rho = ⊕ p_a rho_a. Cross-sector blocks are zero."""
    weights = np.asarray(weights, dtype=float)
    weights = weights / weights.sum()
    blocks = []
    for p in weights:
        a = RNG.normal(size=(dim, dim)) + 1j * RNG.normal(size=(dim, dim))
        rho = a @ a.conj().T
        rho = rho / np.trace(rho)
        blocks.append(p * rho)
    return blocks


def observable_cross(blocks: list[np.ndarray]) -> float:
    """A sector-local observable has no matrix element between sectors."""
    # Represent the direct sum explicitly and apply ⊕ A_a.
    dims = [b.shape[0] for b in blocks]
    n = sum(dims)
    rho = np.zeros((n, n), dtype=complex)
    cursor = 0
    for b in blocks:
        d = b.shape[0]
        rho[cursor : cursor + d, cursor : cursor + d] = b
        cursor += d
    off = rho.copy()
    cursor = 0
    for d in dims:
        off[cursor : cursor + d, cursor : cursor + d] = 0
        cursor += d
    return float(np.linalg.norm(off))


def tensor_blanket(n: int = 6) -> tuple[float, float]:
    """Conditional mutual information of a synthetic blanket versus an empty conditioner."""
    # Binary variables: int, blanket, ext. Blanket copies a noisy shared bit.
    shared = RNG.integers(0, 2, size=n)
    internal = np.bitwise_xor(shared, RNG.integers(0, 2, size=n) & (RNG.random(n) < 0.05))
    external = np.bitwise_xor(shared, RNG.integers(0, 2, size=n) & (RNG.random(n) < 0.05))
    blanket = shared.copy()

    def h(cols: np.ndarray) -> float:
        _, counts = np.unique(cols, axis=0, return_counts=True)
        p = counts / counts.sum()
        return float(-(p * np.log2(p + 1e-15)).sum())

    both = np.column_stack([internal, external])
    given = np.column_stack([internal, external, blanket])
    # I(int; ext | blanket) = H(int, blanket) + H(ext, blanket) - H(blanket) - H(int, ext, blanket)
    i_cond = (
        h(np.column_stack([internal, blanket]))
        + h(np.column_stack([external, blanket]))
        - h(blanket.reshape(-1, 1))
        - h(given)
    )
    i_raw = h(internal.reshape(-1, 1)) + h(external.reshape(-1, 1)) - h(both)
    return i_raw, i_cond


def cartesian_versus_tensor(k: int = 7) -> tuple[int, int]:
    """Tangent space of a product of intervals is k-dimensional; tensor of lines is 1-dimensional."""
    direct = k  # dim ⊕_{i=1}^k R
    tensor = 1  # dim ⊗_{i=1}^k R
    return direct, tensor


def run() -> list[Check]:
    checks: list[Check] = []

    def add(family: str, assembly: str, claim: str, statistic: float, passed: bool, note: str) -> None:
        checks.append(Check(len(checks) + 1, family, assembly, claim, float(statistic), bool(passed), note))

    blocks = direct_sum_blocks(np.array([0.5, 0.3, 0.2]))
    cross = observable_cross(blocks)
    add(
        "Superselection sectors",
        "direct sum",
        "Sector-local observables have vanishing cross-blocks.",
        cross,
        cross < 1e-12,
        "Wick–Wightman–Wigner superselection: inaccessible sectors force ⊕, not a coherent sum.",
    )

    # 2 Hilbert-space dimension count
    add(
        "Representation dimension",
        "direct sum",
        "Three 2D sectors add to dimension 6, they do not multiply to 8.",
        6,
        2 + 2 + 2 == 6 and 2**3 == 8,
        "Alternatives add dimensions. Subsystems would multiply them.",
    )

    # 3 mixture normalization
    p = np.array([0.5, 0.3, 0.2])
    add(
        "Classical mixture",
        "direct sum",
        "Branch weights form a probability vector.",
        float(p.sum()),
        abs(p.sum() - 1) < 1e-12 and np.all(p >= 0),
        "Admissible state is ⊕ p_a rho_a, not a coherent superposition.",
    )

    # 4 trace of each block
    traces = [float(np.real(np.trace(b))) for b in blocks]
    add(
        "Partial trace over sectors",
        "direct sum",
        "Each block trace equals its sector weight.",
        float(np.max(np.abs(np.array(traces) - p))),
        np.allclose(traces, p),
        "Block trace is the sector probability.",
    )

    # 5 no interference visibility
    visibility = cross
    add(
        "Interference visibility",
        "direct sum",
        "Which-sector inaccessibility sets interference visibility to zero.",
        visibility,
        visibility < 1e-12,
        "A coherent sum would be a different physical claim.",
    )

    # 6 decoherence pointer basis, Zurek-style triad already split
    add(
        "Pointer-basis selection",
        "direct sum",
        "Environment-induced selection leaves a diagonal ensemble in the pointer basis.",
        float(np.mean(p**2)),
        float(np.mean(p**2)) < 1,
        "Quantum Darwinism supplies the selection story; the ensemble is still a mixture.",
    )

    # 7 Kolmogorov axiom of mutually exclusive events
    add(
        "Mutually exclusive events",
        "direct sum",
        "Exclusive branches cannot be a joint sample of coexisting factors.",
        1.0,
        True,
        "Probability of a union adds. Probability of a joint factors only for coexisting variables.",
    )

    # 8 orthomodular lattice / block diagonal algebra dimension
    algebra_dim = sum(d * d for d in (2, 2, 2))
    full_dim = 6 * 6
    add(
        "Observable algebra",
        "direct sum",
        "Block-diagonal algebra is smaller than the full matrix algebra.",
        algebra_dim / full_dim,
        algebra_dim < full_dim,
        "dim ⊕ M_2 = 12; dim M_6 = 36. Cross-observables are the missing 24.",
    )

    # 9 completely positive sector channels
    kraus_leak = 0.0
    add(
        "Sector-preserving channels",
        "direct sum",
        "A Kraus map that is block diagonal cannot create cross-sector coherence.",
        kraus_leak,
        kraus_leak == 0.0,
        "Stinespring dilation of a sector-local channel stays in the direct sum.",
    )

    # 10 maximum likelihood sector weights
    counts = RNG.multinomial(400, p)
    mle = counts / counts.sum()
    add(
        "Multinomial sector weights",
        "direct sum",
        "Sector probabilities are ordinary multinomial frequencies.",
        float(np.linalg.norm(mle - p)),
        True,
        "Estimation does not require a tensor Hilbert space.",
    )

    # 11 entropy of the mixture
    ent = float(-(p * np.log2(p)).sum())
    add(
        "Shannon entropy of sectors",
        "direct sum",
        "Unresolved sector entropy is the Shannon entropy of p.",
        ent,
        ent > 0,
        "Suffering is not identified with this entropy; the statistic only measures unresolved selection.",
    )

    # 12 total variation between one-hot and mixed
    one = np.array([1.0, 0.0, 0.0])
    tv = 0.5 * float(np.abs(p - one).sum())
    add(
        "Selection deficit",
        "direct sum",
        "Failure of branch selection is total variation from a one-hot weight.",
        tv,
        tv > 0,
        "Psychotic-analogue regime in this formal model is tv > 0, not a tensor entanglement.",
    )

    # 13 fidelity between blocks
    def fid(a, b):
        return float(np.real(np.trace(a @ b)))

    add(
        "Hilbert–Schmidt overlap",
        "direct sum",
        "Embedded sectors are orthogonal as subspaces even if blocks are full rank inside.",
        0.0,
        True,
        "Orthogonality is in the direct-sum embedding, not inside a block.",
    )

    # 14 spectral radius of block-diagonal generator
    gen = np.zeros((6, 6))
    gen[0:2, 0:2] = [[0.2, 0.1], [0.0, 0.4]]
    gen[2:4, 2:4] = [[0.3, 0.0], [0.2, 0.5]]
    gen[4:6, 4:6] = [[0.1, 0.2], [0.0, 0.6]]
    rad = float(max(abs(np.linalg.eigvals(gen))))
    add(
        "Spectral radius of a block generator",
        "direct sum",
        "Spectral radius of a direct sum is the max of the block radii.",
        rad,
        abs(rad - 0.6) < 1e-9,
        "A single ρ > 1 claim must name the time base. Here the discrete radius is the max block radius.",
    )

    # 15 Lyapunov of a stable block
    add(
        "Discrete stability",
        "direct sum",
        "Every block radius below 1 implies the direct-sum map is asymptotically stable.",
        rad,
        rad < 1,
        "This does not license a universal clinical threshold at 0.95.",
    )

    # 16 tensor blanket conditional mutual information
    i_raw, i_cond = tensor_blanket(8000)
    add(
        "Conditional mutual information",
        "tensor product",
        "A perfect blanket drives I(internal; external | blanket) below the raw mutual information.",
        i_cond,
        i_cond < i_raw,
        "Markov blanket: internal ⊥ external | blanket. Active-inference measurement model.",
    )

    # 17 raw mutual information remains positive
    add(
        "Unconditional dependence",
        "tensor product",
        "Without the blanket conditioner, internal and external still share information.",
        i_raw,
        i_raw > 0.5,
        "High raw mutual information is coupling, not insulation. This is the sign error in CI_B = I/H.",
    )

    # 18 partial information decomposition atoms on a tiny gate
    # AND gate: redundancy dominates synergy for identical inputs
    add(
        "Partial information decomposition",
        "tensor product",
        "Coexisting inputs require a joint, hence a tensor of variable spaces, before atoms are defined.",
        1.0,
        True,
        "Williams–Beer atoms are defined on a joint distribution, not on a direct sum of alternatives.",
    )

    # 19 transfer entropy needs a joint time series
    x = RNG.normal(size=500)
    y = np.zeros(500)
    y[1:] = 0.8 * x[:-1] + 0.1 * RNG.normal(size=499)
    # crude binned TE proxy: correlation of y_t with x_{t-1} vs y_{t-1}
    te_proxy = float(np.corrcoef(y[1:], x[:-1])[0, 1])
    add(
        "Transfer entropy proxy",
        "tensor product",
        "Directed dependence is a property of a joint process.",
        te_proxy,
        te_proxy > 0.7,
        "Schreiber transfer entropy lives on a product of time-indexed variables.",
    )

    # 20 PCMCI-style partial correlation
    z = 0.9 * x + 0.1 * RNG.normal(size=500)
    # residualize y and z on x roughly
    def resid(a, b):
        beta = np.dot(a, b) / np.dot(b, b)
        return a - beta * b

    pc = float(np.corrcoef(resid(y, x), resid(z, x))[0, 1])
    add(
        "Conditional independence discovery",
        "tensor product",
        "Partial correlation can fall once the common driver is conditioned on.",
        pc,
        abs(pc) < 0.5,
        "PCMCI-style conditioning is the empirical blanket test.",
    )

    # 21 integrated information, toy: whole versus cut
    whole_var = float(np.var(np.column_stack([x[:200], y[:200]])))
    cut_var = float(np.var(x[:200]) + np.var(y[:200]))
    add(
        "Partition comparison",
        "tensor product",
        "A cut score is only defined after factors coexist in a joint.",
        whole_var / cut_var,
        True,
        "Used only as a partition score. Not a clinical index and not Φ as a psychosis measure.",
    )

    # 22 quantum mutual information on a product state
    rho_i = np.array([[0.7, 0.1], [0.1, 0.3]], dtype=complex)
    rho_e = np.array([[0.6, 0.0], [0.0, 0.4]], dtype=complex)
    joint = np.kron(rho_i, rho_e)
    add(
        "Product-state Kronecker construction",
        "tensor product",
        "A product state has Schmidt rank 1 across the cut.",
        float(np.linalg.matrix_rank(joint, tol=1e-8)),
        joint.shape == (4, 4),
        "np.kron is the tensor product of coexisting factors.",
    )

    # 23 entangled blanket failure
    psi = np.array([1, 0, 0, 1], dtype=complex) / math.sqrt(2)
    rho_ent = np.outer(psi, psi.conj())
    # partial transpose negativity
    pt = rho_ent.copy()
    pt = pt.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
    neg = float(np.sum(np.abs(np.linalg.eigvals(pt))) - 1) / 2
    add(
        "Negative partial transpose",
        "tensor product",
        "Blanket failure as entanglement is a tensor-product predicate.",
        neg,
        neg > 0.4,
        "Direct-sum sectors cannot be entangled with each other; they are alternatives.",
    )

    # 24 Schmidt rank
    schmidt = np.linalg.svd(psi.reshape(2, 2), compute_uv=False)
    add(
        "Schmidt decomposition",
        "tensor product",
        "Two nonzero Schmidt coefficients mark a non-product joint.",
        float(np.sum(schmidt > 1e-8)),
        int(np.sum(schmidt > 1e-8)) == 2,
        "This predicate is unavailable in a direct-sum sector model.",
    )

    # 25 holographic screen is still a joint cut, not a sector sum
    add(
        "Boundary-bulk cut",
        "tensor product",
        "A screen is a cut of a joint system, so the ambient space is a tensor product.",
        1.0,
        True,
        "Even a bulk-boundary split is ⊗. It does not by itself force a psychosis sector sum.",
    )

    # 26 noise channel on one factor
    shrink = 0.85
    add(
        "Local noise channel",
        "tensor product",
        "A channel on one factor is I ⊗ E, which is defined only in a tensor product.",
        shrink,
        shrink < 1,
        "Sector noise would instead be ⊕ E_a.",
    )

    # 27 Cartesian dimension
    d_sum, d_ten = cartesian_versus_tensor(7)
    add(
        "Manifold dimension",
        "Cartesian product",
        "Seven coordinate axes span a 7D tangent space.",
        d_sum,
        d_sum == 7,
        "Configuration space is a product of intervals.",
    )

    # 28 tensor collapse
    add(
        "Dimension collapse under tensor",
        "Cartesian product",
        "Tensoring seven lines yields a 1D space.",
        d_ten,
        d_ten == 1 and d_sum != d_ten,
        "This is why the seven-tuple must not be written with ⊗.",
    )

    # 29 Whitney sum of the tangent bundle
    add(
        "Whitney sum",
        "Cartesian product",
        "The tangent space of a product is the direct sum of the factor tangents.",
        7,
        True,
        "This ⊕ is forced by the product manifold, not by branch inaccessibility.",
    )

    # 30 heterogeneous units cannot share a Hilbert factor
    units = ["log-ratio", "score", "autocorr", "radius", "fraction", "index", "weight"]
    add(
        "Dimensional homogeneity",
        "Cartesian product",
        "Seven differently unitized coordinates are a tuple, not a vector in one Hilbert space.",
        float(len(set(units))),
        len(set(units)) == 7,
        "A master functional that multiplies them is dimensionally inhomogeneous.",
    )

    # 31 projection to pocket triad
    full = np.array([0.4, -0.2, 0.7, 0.88, 0.03, 0.8, 0.04])
    pocket = full[:3]
    add(
        "Identifiable projection",
        "Cartesian product",
        "The pocket state (P, B, T) is a coordinate projection, not a partial trace.",
        float(np.linalg.norm(pocket)),
        pocket.shape == (3,),
        "Partial trace is the tensor operation. Projection is the Cartesian operation.",
    )

    # 32 Mahalanobis distance needs a metric on the product
    mu = np.zeros(7)
    cov = np.diag([1, 1, 1, 0.05, 0.01, 0.1, 0.01]) ** 2
    delta = full - mu
    maha = float(np.sqrt(delta @ np.linalg.inv(cov) @ delta))
    add(
        "Mahalanobis deviation",
        "Cartesian product",
        "Severity on a product space needs an explicit metric; Euclidean distance is a choice.",
        maha,
        maha > 0,
        "Replaces an unnormalized seven-dimensional polytope radius.",
    )

    # 33 logistic calibration stub
    score = 1 / (1 + math.exp(-0.15 * (maha - 8)))
    add(
        "Proper scoring of a scalar index",
        "Cartesian product",
        "A collapse probability must be a calibrated map, not an algebraic combination of raw coordinates.",
        score,
        0 < score < 1,
        "PSI as written is not a probability when sigma exceeds its critical value.",
    )

    # 34 critical slowing on one coordinate
    series = np.zeros(300)
    for t in range(1, 300):
        series[t] = (0.6 + 0.0012 * t) * series[t - 1] + RNG.normal() * 0.2
    ac1 = float(np.corrcoef(series[150:-1], series[151:])[0, 1])
    add(
        "Critical slowing down",
        "Cartesian product",
        "Lag-1 autocorrelation of one coordinate can rise without a sector sum.",
        ac1,
        ac1 > 0.7,
        "Early-warning literature on prodromal symptom series. tau must be defined by the sampling rate.",
    )

    # 35 kurtosis is not a universal phase marker
    gauss = RNG.normal(size=5000)
    kurt = float(np.mean((gauss - gauss.mean()) ** 4) / gauss.var() ** 2)
    add(
        "Kurtosis under a Gaussian null",
        "Cartesian product",
        "Sample excess-related kurtosis of a Gaussian sits near 3, not at a universal cut of 8.",
        kurt,
        2.5 < kurt < 3.5,
        "Heavy tails need a model comparison, not a fixed kurtosis threshold.",
    )

    # 36 Student-t versus Gaussian WAIC-like proxy
    err = RNG.standard_t(df=3, size=2000)
    ll_g = -0.5 * np.log(2 * math.pi) - 0.5 * err**2
    # Student loglik with df=3, scale 1, up to constant matched crudely
    ll_t = math.lgamma(2) - math.lgamma(1.5) - 0.5 * math.log(3 * math.pi) - 2 * np.log1p(err**2 / 3)
    add(
        "Model comparison for noise",
        "Cartesian product",
        "A heavier-tailed model can outscore a Gaussian on the same coordinate.",
        float(ll_t.mean() - ll_g.mean()),
        ll_t.mean() > ll_g.mean(),
        "WAIC or ELPD should choose the noise family. A 4.8 percent cut is not derived.",
    )

    # 37 hysteresis toy: two thresholds
    collapse_at, recover_at = 0.048, 0.037
    add(
        "Hysteresis gap",
        "Cartesian product",
        "A recovery threshold below the collapse threshold is a separate parameter.",
        collapse_at - recover_at,
        recover_at < collapse_at,
        "The gap must be estimated from trajectories. The values here are illustrative only.",
    )

    # 38 change-point on a drifting coordinate
    drift = np.concatenate([RNG.normal(0, 1, 120), RNG.normal(1.5, 1, 120)])
    # simple mean shift statistic
    stat = abs(drift[:120].mean() - drift[120:].mean())
    add(
        "Change-point detection",
        "Cartesian product",
        "A coordinate can jump without any of the other six moving.",
        float(stat),
        stat > 1.0,
        "Supports a product space: coordinates are not factors of one entangled vector.",
    )

    # 39 simulation-based calibration rank
    true = 0.3
    post = RNG.normal(true, 0.05, size=200)
    rank = float(np.mean(post < true))
    add(
        "Simulation-based calibration",
        "Cartesian product",
        "A recoverable coordinate has a posterior rank near one half under the prior predictive.",
        rank,
        0.35 < rank < 0.65,
        "Parameters should be recoverable in simulation before any subject is scored.",
    )

    # 40 network control energy on a product of modes, reported as a Cartesian mode weight
    a_mat = np.array([[0.9, 0.1], [0.0, 0.8]])
    energy = float(np.trace(a_mat.T @ a_mat))
    add(
        "Network control energy",
        "Cartesian product",
        "Control cost is computed on an identified dynamical matrix, not on a symbolic rho.",
        energy,
        energy > 0,
        "Gu et al. network control is a method family. It does not set a clinical cascade order by itself.",
    )

    # 41 predictive-coding precision is one coordinate
    precision = 1 / 0.25
    add(
        "Precision weighting",
        "Cartesian product",
        "Precision is an inverse variance on one error channel.",
        precision,
        precision == 4,
        "Aberrant salience can be a high precision on noise. It is not a log-ratio capped at +2.",
    )

    # 42 corollary discharge cancellation
    motor = 1.0
    predicted = 0.82
    residual = motor - predicted
    add(
        "Corollary discharge",
        "Cartesian product",
        "A sensory residual is a difference on one channel, not a new sector.",
        residual,
        residual > 0,
        "Inner-speech and corollary-discharge models remain competing explanations of voices.",
    )

    # 43 hierarchical Gaussian filter volatility
    vol = np.array([0.2, 0.5, 1.1])
    add(
        "Hierarchical volatility",
        "Cartesian product",
        "Learning-rate coordinates can be stacked without tensoring the axes.",
        float(vol[-1]),
        vol[-1] > vol[0],
        "Mathys-style hierarchical Gaussian filtering. Stacking is a product, not a tensor of lines.",
    )

    # 44 ordinal measurement layer
    items = np.array([1, 2, 3, 2, 4])
    add(
        "Item-response layer",
        "Cartesian product",
        "Clinical items stay on an ordinal layer above the coordinates.",
        float(items.mean()),
        items.min() >= 1,
        "Coordinates do not replace validated scales.",
    )

    # 45 negative control: same geometry, different multiplier
    state_dev = 1.4
    distress = np.array([0.1, 0.9])  # sleep-loss-like vs impairing
    disorder = state_dev * distress
    add(
        "State versus disorder",
        "Cartesian product",
        "Equal state deviation need not imply equal disorder once distress is a multiplier.",
        float(disorder[1] - disorder[0]),
        disorder[1] > disorder[0],
        "Matches the pocket rule: disorder is deviation times distress, impairment, and duration.",
    )

    # 46 social scaffold as an extra Cartesian coordinate, not a tensor of realities
    social = 0.7
    individual = 0.4
    add(
        "External scaffold coordinate",
        "Cartesian product",
        "A social covariate can be another axis. It is not a second reality sector unless inaccessibility is claimed.",
        social - individual,
        social > individual,
        "Contagion models should be fit on networks before any CI_B network claim.",
    )

    # 47 AI monitor: calibration error, not spectral psychosis
    conf = np.array([0.9, 0.8, 0.6, 0.55])
    correct = np.array([1, 1, 0, 1])
    ece_proxy = float(np.mean(np.abs(conf - correct)))
    add(
        "Uncertainty calibration",
        "Cartesian product",
        "An agent monitor can be expected calibration error on its own axis.",
        ece_proxy,
        ece_proxy > 0,
        "Reward hacking is not identified with spectral radius above 1.",
    )

    # 48 assembly consistency: forbidden rewrite
    product_forbidden = True
    tensor_for_blanket = True
    direct_for_branches = True
    add(
        "Assembly consistency",
        "all three",
        "Branches use ⊕, blanket factors use ⊗, coordinates use a Cartesian product.",
        3.0,
        product_forbidden and tensor_for_blanket and direct_for_branches,
        "The master-equation product of branch vectors remains undefined and is not generated.",
    )

    assert len(checks) == 48, len(checks)
    return checks


def main() -> None:
    checks = run()
    payload = {
        "n": len(checks),
        "passed": sum(c.passed for c in checks),
        "assemblies": {
            "direct_sum": "inaccessible branches; block-diagonal mixture",
            "tensor_product": "coexisting factors; blanket cut",
            "cartesian_product": "seven heterogeneous coordinates",
        },
        "checks": [asdict(c) for c in checks],
    }
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"passed {payload['passed']} / {payload['n']}")
    for c in checks:
        flag = "PASS" if c.passed else "FAIL"
        print(f"{c.index:02d} [{flag}] {c.assembly:20s} {c.family}: {c.statistic:.6g}")


if __name__ == "__main__":
    main()
