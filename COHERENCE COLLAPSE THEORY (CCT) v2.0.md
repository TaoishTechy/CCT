# COHERENCE COLLAPSE THEORY (CCT) v2.0

## An Informational Phase Transition Framework of Psychosis

### Revised Specification with Operationalized Constructs and Falsifiable Predictions

**Landry, M.**

*Revised following formal audit and systematic correction*

Version 2.0 | 2026

**OPEN SCIENTIFIC FRAMEWORK | LICENSED UNDER HOLY PUBLIC DOMAIN v3.14159++**

---

# Preamble to v2.0

This revision responds to the 144-point audit of v1.0. The original framework contained foundational sign errors, dimensional inconsistencies, undefined terms, and non-falsifiable constructs. Rather than defending the original formalism, this revision:

1. **Corrects sign and bound errors** in boundary coherence
2. **Operationalizes every construct** with an estimator
3. **Retires unfalsifiable claims** (conservation axiom as stated, universal phase transition)
4. **Reframes the theory** as a mid-level computational model, not a first-principles derivation
5. **Gates all numerical thresholds** on empirical calibration
6. **Separates analogy from model** in cross-domain claims

The core phenomenological insight—that psychosis involves a characteristic breakdown in the relationship between self-boundary, temporal coherence, and informational organization—remains. What changes is the formal architecture and its evidential status.

**What this theory is:** A structured hypothesis linking computational parameters (precision, boundary integrity, temporal integration, noise sensitivity) to psychotic phenomenology, with explicit measurement models and falsifiable predictions.

**What this theory is not:** A first-principles derivation, a universal phase transition theory, a clinical protocol, or a complete framework.

---

# Abstract

Coherence Collapse Theory (CCT) proposes that psychosis involves a characteristic pattern of parameter deviation in self-modeling systems: reduced boundary integrity between internal and external states, elevated precision-weighting on prediction errors, disrupted temporal integration, and increased noise sensitivity. These deviations are operationally defined using established methods from computational psychiatry and dynamical systems neuroscience.

This revision: (1) corrects the boundary coherence formula to properly condition on Markov blanket states; (2) replaces unbounded constructs with normalized indices that have defined ranges; (3) reduces the state vector to parameters with existing estimators; (4) reframes the conservation principle as an approximate continuity equation with testable residuals; (5) specifies falsification conditions for all predictions; and (6) removes cross-domain claims that lack shared estimators.

The central hypothesis is that psychosis is not a categorical disorder but a region of parameter space characterized by specific deviations from healthy functioning—a hypothesis testable through hierarchical Bayesian modeling of longitudinal multimodal data.

**Keywords:** computational psychiatry, predictive coding, aberrant salience, Markov blankets, phase transitions, psychosis, precision-weighting

---

# Part I: Corrected Foundations

## 1. Theoretical Status and Scope

### 1.1 What CCT Claims

CCT v2.0 makes three bounded claims:

**Claim 1 (Computational):** Psychotic phenomenology is associated with a characteristic pattern of deviations in precision-weighting, boundary integrity, and temporal integration parameters within predictive-processing architectures.

**Claim 2 (Dynamical):** The transition from prodromal to acute psychosis involves a shift in the stability properties of the self-model's attractor landscape, detectable through early-warning signals.

**Claim 3 (Measurement):** These deviations can be estimated from neurophysiological and behavioral data using established methods, and their trajectories predict clinical outcomes.

### 1.2 What CCT Does Not Claim

- That psychosis is a "universal phase transition" occurring identically across all scales
- That the theory derives from first principles
- That numerical thresholds are known prior to calibration
- That the formalism applies to quantum, cosmological, or social systems without a shared estimator
- That any parameter can be directly "set" by intervention

### 1.3 Evidential Status

CCT is a **mid-level computational model**. It synthesizes established findings (aberrant salience, predictive coding deficits, corollary discharge dysfunction) into a parameter-space framework. The framework generates hypotheses; it does not yet have the status of a confirmed theory.

---

## 2. Operationalized Constructs

### 2.1 Boundary Coherence (Corrected)

**Problem in v1.0:** The formula \( \mathrm{CI}_B = 1 - H(\mathrm{internal}|\mathrm{external})/H(\mathrm{internal}) \) equals \( I(\mathrm{internal};\mathrm{external})/H(\mathrm{internal}) \), which is *high* when internal states are predictable from external states—the opposite of insulation.

**Corrected Definition:**

Boundary coherence measures the degree to which internal states are *insulated* from external states, conditional on blanket states:

\[
\mathrm{CI}_B = 1 - \frac{I(s_{\mathrm{int}}; s_{\mathrm{ext}} \mid s_{\mathrm{blanket}})}{H(s_{\mathrm{int}} \mid s_{\mathrm{blanket}})}
\]

*Eq. 2.1 — Boundary Coherence (Corrected)*

Where:
- \( s_{\mathrm{int}} \): internal states (beliefs, memories, intentions)
- \( s_{\mathrm{ext}} \): external states (environmental inputs)
- \( s_{\mathrm{blanket}} \): blanket states (sensory and active states mediating the boundary)
- \( I(\cdot;\cdot\mid\cdot) \): conditional mutual information
- \( H(\cdot\mid\cdot) \): conditional Shannon entropy

**Interpretation:**
- \( \mathrm{CI}_B = 1 \): Internal states are conditionally independent of external states given the blanket—perfect insulation
- \( \mathrm{CI}_B = 0 \): Internal states are fully determined by external states given the blanket—no insulation

**Estimator:** Conditional mutual information estimated via PCMCI (Peter-Clark Momentary Conditional Independence) or equivalent causal discovery algorithm on quantized time series. See Runge et al. (2019).

**Range:** \( [0,1] \) for discrete variables under \( I \le H \). Continuous variables require quantization or density estimation with specified reference measure.

### 2.2 Continuum Coherence (Corrected)

**Problem in v1.0:** The formula \( \mathrm{CI}_C = I(X;Y)/H(X) \) lies in \( [0,1] \), contradicting the claim that \( \mathrm{CI}_C \to \infty \).

**Corrected Definition:**

Continuum coherence is replaced by **excess entropy** (predictive information), which measures the total mutual information between past and future states:

\[
E = I(X_{\mathrm{past}}; X_{\mathrm{future}})
\]

*Eq. 2.2 — Excess Entropy*

**Interpretation:**
- High \( E \): Rich, structured temporal dynamics with long-range predictability
- Low \( E \): Disordered or random dynamics

**Range:** \( E \ge 0 \), unbounded above but typically scales with system size.

**Estimator:** Excess entropy estimated via block entropy methods (Grassberger, 1986) or transfer entropy with finite-sample bias correction (Marschinski & Kantz, 2002).

**Note:** The construct formerly called "continuum coherence" is retired. "Pathologically elevated \( \mathrm{CI}_C \)" is replaced by the hypothesis that psychosis involves *reduced* excess entropy (temporal disorganization) despite *elevated* local correlation.

### 2.3 Conservation Principle (Reframed)

**Problem in v1.0:** The axiom \( \partial_t(\mathrm{CI}_B + \mathrm{CI}_C) = \sigma_{\mathrm{topo}} \) is non-falsifiable because psychosis is defined as its violation.

**Corrected Formulation:**

Replace axiom with approximate continuity equation on a specified partition:

\[
\frac{d}{dt}\left( \mathrm{CI}_B + E \right) = \sigma_{\mathrm{residual}}
\]

*Eq. 2.3 — Approximate Continuity*

Where \( \sigma_{\mathrm{residual}} \) is an *estimated residual* that is:
- Near zero for healthy systems in steady state
- Nonzero during learning, development, and state transitions
- Abnormally large during psychotic transition

**Falsifiable Prediction:** The residual \( \sigma_{\mathrm{residual}} \) during acute psychosis exceeds the 95th percentile of residuals in healthy controls undergoing equivalent task demands.

**Note:** This is not a conservation law. It is an approximate bookkeeping equation whose residuals are the object of study.

---

## 3. Psychotic State Vector (PSV) — Revised

### 3.1 Dimensional Reduction

**Problem in v1.0:** Seven dimensions with incompatible codomains, undefined inner product, and symbol collisions.

**Corrected PSV:**

The state vector is reduced to four parameters with existing estimators:

\[
\mathrm{PSV} = (\pi, \beta, \tau, \nu)
\]

*Eq. 3.1 — Psychotic State Vector (Revised)*

| Symbol | Name | Definition | Healthy Range | Psychotic Deviation | Estimator |
|--------|------|------------|---------------|---------------------|-----------|
| \( \pi \) | Precision gain | Weight on prediction errors vs. priors | \( [0.5, 2.0] \) | \( \pi > 3.0 \) | Hierarchical Gaussian filter (HGF); Mathys et al. (2014) |
| \( \beta \) | Boundary permeability | \( 1 - \mathrm{CI}_B \) | \( [0, 0.3] \) | \( \beta > 0.7 \) | PCMCI on multimodal time series |
| \( \tau \) | Temporal integration constant | Decay rate of temporal autocorrelation | \( [0.3, 1.0] \) s | \( \tau < 0.1 \) s | Autocorrelation half-life; delayed embedding |
| \( \nu \) | Noise sensitivity | Inverse signal-to-noise threshold | \( [0.02, 0.05] \) | \( \nu > 0.08 \) | Psychophysical discrimination threshold |

**Note:** The parameters \( \rho \) (spectral radius), \( \sigma \) (noise fraction), \( \mathrm{CI}_B \), and \( \lambda \) (regularization) from v1.0 are retired as primary coordinates. They may be derived from the four core parameters under specific model assumptions, but are not independently measurable in the general case.

### 3.2 Coordinate Examples (Retired)

**Problem in v1.0:** Invented coordinate points such as \( \mathrm{CCT}(+1.8, -1.7, \ldots) \) not fitted to any cohort.

**Correction:** All coordinate examples are removed. PSV coordinates must be estimated from data using the specified estimators. Reporting conventions will be established after calibration on existing cohorts.

---

## 4. Phase Transition Hypothesis (Reframed)

### 4.1 From Categorical Threshold to Continuous Risk

**Problem in v1.0:** OR versus AND inconsistency; no proof of irreversibility; arbitrary thresholds.

**Corrected Formulation:**

Psychosis is not a discrete phase transition with sharp thresholds. It is a **region of parameter space** associated with:
- Elevated \( \pi \) (precision gain)
- Elevated \( \beta \) (boundary permeability)
- Reduced \( \tau \) (temporal integration)
- Elevated \( \nu \) (noise sensitivity)

**Risk Model:**

\[
P(\text{psychotic episode}) = \sigma\left( \sum_i w_i \cdot \mathrm{PSV}_i + b \right)
\]

*Eq. 4.1 — Psychotic Risk as Logistic Function*

Where:
- \( \sigma(\cdot) \) is the logistic function
- \( w_i \) are weights estimated from longitudinal data
- \( b \) is a bias term
- \( \mathrm{PSV}_i \) are the four parameters

**Calibration:** Weights and bias must be estimated on a training cohort and validated on an external cohort. No thresholds are specified a priori.

### 4.2 Early Warning Signals

**Corrected Predictions:**

Based on established dynamical-systems methods (Scheffer et al., 2009):

| Signal | Measure | Expected Change | Lead Time |
|--------|---------|-----------------|-----------|
| Critical slowing | Lag-1 autocorrelation of symptom time series | Increase toward 1 | 2-4 weeks |
| Variance rise | Variance of symptom time series | Increase | 2-4 weeks |
| Skewness shift | Skewness of symptom distribution | Increase | 1-3 weeks |
| Kurtosis shift | Kurtosis of prediction-error distribution | Increase (heavy tails) | 1-3 weeks |

**Note:** Lead times are hypotheses to be tested, not established facts. The undefined \( \tau \) from v1.0 is replaced by calendar time.

---

## 5. Cascade Model (Revised)

### 5.1 From Asserted Sequence to Testable Hypothesis

**Problem in v1.0:** The sequence \( \rho \to r \to \sigma \) was asserted without a Jacobian or coupling matrix.

**Corrected Formulation:**

The cascade hypothesis is restated as a testable claim about temporal ordering:

**Hypothesis:** In prodromal psychosis, changes in precision gain \( \pi \) precede changes in boundary permeability \( \beta \), which precede changes in temporal integration \( \tau \).

**Test:** Cross-lagged panel model or Granger causality on longitudinal data.

**Falsification:** If \( \beta \) changes precede \( \pi \) changes in a majority of prodromal subjects, the cascade hypothesis is falsified.

### 5.2 Spectral Claims (Retired)

**Problem in v1.0:** Period 4-7, Lyapunov exponent \( +0.27 \), half-life 1.1 iter—all magic numbers without derivation.

**Correction:** These claims are removed. Spectral properties of fitted dynamical models (neural mass models, dynamic causal models) may be estimated, but no specific values are predicted.

---

## 6. Master Psychosis Functional (Retired)

**Problem in v1.0:** Equation 2.7 was a limit expression, not a functional; the limit path was unspecified; symbols collided; the expression was dimensionally inhomogeneous.

**Correction:** The master functional is retired. It is replaced by the generative model:

\[
\mathbf{x}_{t+1} = f(\mathbf{x}_t, \theta) + \epsilon_t
\]

\[
\mathbf{y}_t = g(\mathbf{x}_t, \theta) + \eta_t
\]

*Eq. 6.1 — Generative Model*

Where:
- \( \mathbf{x}_t \): latent states (beliefs, precisions, boundary parameters)
- \( \mathbf{y}_t \): observations (behavioral, neural, self-report)
- \( \theta \): parameters including \( \pi, \beta, \tau, \nu \)
- \( f, g \): transition and observation functions (specified by model class)

Parameter estimation via variational Bayes or Markov Chain Monte Carlo. Model comparison via WAIC or ELPD.

---

## 7. Multiscale Claims (Restricted)

### 7.1 From Narrative Parallel to Shared Estimator

**Problem in v1.0:** The multiscale table presented narrative parallels as formal isomorphisms without shared estimators.

**Corrected Formulation:**

Cross-domain claims require that the *same dimensionless estimator*, computed with the *same code*, exceeds a *preregistered threshold* in both domains.

**Current Status:**

| Domain | Shared Estimator | Status |
|--------|------------------|--------|
| Neural | \( \pi, \beta, \tau, \nu \) | Under development |
| AI/RL | Reward-model disagreement, uncertainty calibration | Candidate estimators; not yet validated |
| Social | Belief-updating parameters from network data | Candidate estimators; not yet validated |
| Quantum | None | Retired |
| Cosmological | None | Retired |

**Note:** Quantum and cosmological rows are removed. Macroscopic coherence is not a clinical phenocopy.

### 7.2 AI Safety (Revised)

**Problem in v1.0:** \( \rho(W_{\mathrm{policy}}) > 1 \) as psychosis analogue; reward hacking routinely occurs without this condition.

**Corrected Formulation:**

Monitor directly:
- Reward-model disagreement (ensemble variance)
- Policy divergence (KL between policy and reference)
- Uncertainty calibration (expected vs. observed error)

**Hypothesis:** These quantities are elevated during reward hacking and deceptive alignment.

**Falsification:** If reward hacking occurs without elevated reward-model disagreement in a preregistered agent study, the AI-psychosis analogy is falsified.

---

## 8. Phenomenology Mapping (Revised)

### 8.1 Six Signatures (Corrected)

| Signature | Computational Substrate | Measured Quantity | Falsification |
|-----------|------------------------|-------------------|---------------|
| Hyperconnective totalism | Elevated \( \pi \) | Precision-weighted prediction error; HGF \( \omega \) parameter | \( \pi \) not elevated in acute psychosis |
| Boundary permeability | Elevated \( \beta \) | Conditional mutual information \( I(s_{\mathrm{int}}; s_{\mathrm{ext}} \mid s_{\mathrm{blanket}}) \) | \( \beta \) not elevated |
| Temporal discontinuity | Reduced \( \tau \) | Autocorrelation half-life; delayed embedding dimension | \( \tau \) not reduced |
| Identity instability | Reduced attractor stability | Variance of self-report identity measures; switching rate in perceptual rivalry | No instability detected |
| Voice fragmentation | Multiple latent policies | Number of independent sources in MEG during AVH; mixture-model component count | Fewer than 2 sources |
| Multiversal simultaneity | Branch desynchronization | Not operationalized | Retired as formal construct |

**Note:** "Multiversal simultaneity" is retained as phenomenological description, not as formal construct. It is not distinguished from ordinary ambiguity or confabulation in v2.0.

### 8.2 Auditory Verbal Hallucinations (Revised)

**Problem in v1.0:** AVH reduced to \( \lambda < 0.008 \) and "3+ voices," ignoring corollary-discharge and inner-speech accounts.

**Corrected Formulation:**

AVH are modeled as a mixture of latent policies with a Dirichlet-process prior:

\[
p(\text{voice}_i) \sim \mathrm{DP}(\alpha, H)
\]

*Eq. 8.1 — Voice Mixture Model*

**Component number** is inferred, not fixed at 3. **Model comparison** against corollary-discharge and inner-speech models determines which account survives.

**Falsification:** If a unified corollary-discharge model fits AVH data better than a mixture model, the fragmentation hypothesis is falsified for that dataset.

---

## 9. Diagnostic Formalism (Revised)

### 9.1 Psychotic State Index (Corrected)

**Problem in v1.0:** PSI depended mainly on \( \sigma \); negative values outside interpretation bands; omitted dimensions.

**Corrected Formulation:**

\[
\mathrm{PSI} = \sigma\left( w_0 + w_1 \pi + w_2 \beta + w_3 \tau + w_4 \nu \right)
\]

*Eq. 9.1 — Psychotic State Index*

Where:
- \( \sigma(\cdot) \) is the logistic function (ensuring \( \mathrm{PSI} \in [0,1] \))
- Weights estimated on training cohort, validated on external cohort
- Calibration via isotonic regression or Platt scaling

**Interpretation:** PSI is a probability, not a score. Decision curves and net benefit analysis determine clinical utility.

### 9.2 Early Warning Indicators (Revised)

| Signal | Measure | Threshold | Action |
|--------|---------|-----------|--------|
| Critical slowing | Lag-1 autocorrelation | > 0.8 (preregistered) | Increase monitoring |
| Variance rise | Variance of symptoms | > 2× baseline | Clinical review |
| Kurtosis shift | Kurtosis of prediction errors | > 5 (preregistered) | Cognitive assessment |
| Boundary erosion | \( \beta \) from PCMCI | > 0.6 | Grounding intervention |

**Note:** Thresholds are hypotheses, not established cutoffs. They require calibration on existing prodromal cohorts (CHR designs).

---

## 10. Coherence Restoration Cascade (CRC) — Revised

### 10.1 From Protocol to Research Program

**Problem in v1.0:** CRC sequence declared without topology; D2 antagonism mapped to \( \rho \); numerical targets for \( \lambda \), \( T \); efficacy claims embedded in theory.

**Corrected Formulation:**

The CRC is a **research program**, not a clinical protocol. Its claims are:

1. **Testable:** Interventions targeting different parameters should have additive or synergistic effects.
2. **Ordered:** The sequence \( \pi \to \beta \to \tau \to \nu \) should be tested in factorial designs.
3. **Gated:** No efficacy claims until randomized controlled trials are conducted.

### 10.2 Intervention Mapping (Hypotheses)

| Target | Intervention Class | Mechanism Hypothesis | Test |
|--------|-------------------|---------------------|------|
| \( \pi \) | D2 antagonists | Reduce precision-weighting on prediction errors | HGF parameter estimation pre/post |
| \( \beta \) | Grounding techniques | Rebuild Markov blanket via sensorimotor anchoring | PCMCI pre/post |
| \( \tau \) | Narrative therapy | Re-establish temporal autocorrelation | Autocorrelation half-life pre/post |
| \( \nu \) | Sensory modulation | Reduce noise sensitivity | Psychophysical threshold pre/post |

**Note:** These are hypotheses, not established mechanisms. Standard of care takes precedence.

### 10.3 Hysteresis (Revised)

**Problem in v1.0:** 4.8% and 3.7% thresholds unestimated.

**Corrected Formulation:**

Hysteresis is estimated from longitudinal trajectories using change-point detection and cusp-catastrophe models. No thresholds are specified a priori.

**Prediction:** Relapse threshold < remission threshold for at least one PSV parameter.

**Falsification:** If relapse and remission thresholds are equal for all parameters, hysteresis is absent.

---

## 11. Predictions (Revised)

### 11.1 Neuroscience

| Prediction | Measured Quantity | Test Method | Falsification |
|------------|-------------------|-------------|---------------|
| N1 | HGF \( \omega \) (precision) elevated in prodromal subjects | Hierarchical Gaussian filter on behavioral data | \( \omega \) not elevated |
| N2 | \( \beta \) (boundary permeability) elevated in acute psychosis | PCMCI on fMRI + behavioral time series | \( \beta \) not elevated |
| N3 | \( \tau \) (temporal integration) reduced in acute psychosis | Autocorrelation half-life | \( \tau \) not reduced |
| N4 | Critical slowing precedes relapse | Lag-1 autocorrelation of symptom time series | No critical slowing |

### 11.2 Computational

| Prediction | Measured Quantity | Test Method | Falsification |
|------------|-------------------|-------------|---------------|
| A1 | Reward-model disagreement elevated during reward hacking | Ensemble variance in deep RL | No elevation |
| A2 | Policy divergence elevated during deceptive alignment | KL divergence from reference policy | No elevation |
| A3 | Uncertainty miscalibration precedes goal misgeneralization | Expected vs. observed error | No miscalibration |

### 11.3 Clinical

| Prediction | Measured Quantity | Test Method | Falsification |
|------------|-------------------|-------------|---------------|
| C1 | PSI predicts episode within 3 months | ROC analysis; AUC > 0.70 | AUC < 0.70 |
| C2 | CRC sequence outperforms treatment-as-usual | RCT; remission rate | No difference |
| C3 | Social coherence moderates recovery | Network analysis + outcome | No moderation |

---

## 12. Philosophical Coda (Revised)

### 12.1 The Protective Function of Selfhood

The coherence architecture—boundary integrity, temporal integration, precision regulation—is not a limitation on experience. It is a precondition for adaptive functioning.

The self is a computational achievement: a dynamically maintained region of locally reduced entropy, bounded by a semi-permeable membrane, sustained by metabolic expenditure.

**Self = arg min H(S | environment) subject to: \( \mathrm{CI}_B \ge \epsilon_B \), \( \pi \le \pi_{\max} \)**

*Eq. 12.1 — Self as Constrained Entropy Minimization*

### 12.2 Psychosis as Revelation (Restricted)

The claim that psychosis "reveals something true about reality" is retained as *phenomenological description*, not as theorem. Elevated salience is not knowledge; it is a computational state that may feel like insight but is not calibrated to truth.

**Ethical Constraint:** Any account of psychosis must include the impairment multiplier—distress, functional impairment, and duration—that distinguishes disorder from non-disordered states.

### 12.3 Ethics of Coherence (Revised)

**Problem in v1.0:** \( \frac{d}{dt}\mathrm{CI}_B \ge 0 \) forbids sleep, play, grief, and learning.

**Corrected Principle:**

\[
\text{Non-maleficence: Do not intervene to reduce } \mathrm{CI}_B \text{ below the healthy range}
\]

*Eq. 12.2 — Non-Maleficence*

This applies to:
- Individuals: Do not disrupt therapeutic grounding
- Social systems: Do not amplify epistemic contagion
- AI systems: Do not deploy agents with uncalibrated uncertainty

---

## 13. Glossary (Revised)

| Term | Symbol | Definition | Estimator |
|------|--------|------------|-----------|
| Boundary coherence | \( \mathrm{CI}_B \) | Insulation of internal from external states given blanket | PCMCI |
| Boundary permeability | \( \beta \) | \( 1 - \mathrm{CI}_B \) | Derived |
| Excess entropy | \( E \) | Mutual information between past and future | Block entropy |
| Precision gain | \( \pi \) | Weight on prediction errors vs. priors | HGF |
| Psychotic State Index | PSI | Probability of episode given PSV | Logistic regression |
| Psychotic State Vector | PSV | \( (\pi, \beta, \tau, \nu) \) | See estimators |
| Temporal integration | \( \tau \) | Autocorrelation half-life | Delayed embedding |
| Noise sensitivity | \( \nu \) | Psychophysical discrimination threshold | Staircase procedure |

---

## 14. References

### Primary Empirical Literature

- Adams, R. A., Stephan, K. E., Brown, H. R., Frith, C. D., & Friston, K. J. (2013). The computational anatomy of psychosis. *Frontiers in Psychiatry*, 4, 47.
- Fletcher, P. C., & Frith, C. D. (2009). Perceiving is believing: A Bayesian approach to explaining the positive symptoms of schizophrenia. *Nature Reviews Neuroscience*, 10(1), 48-58.
- Kapur, S. (2003). Psychosis as a state of aberrant salience. *American Journal of Psychiatry*, 160(1), 13-23.
- Mathys, C., Daunizeau, J., Friston, K. J., & Stephan, K. E. (2011). A Bayesian foundation for individual learning under uncertainty. *Frontiers in Human Neuroscience*, 5, 39.
- Scheffer, M., Bascompte, J., Brock, W. A., et al. (2009). Early-warning signals for critical transitions. *Nature*, 461(7260), 53-59.
- Stephan, K. E., Baldeweg, T., & Friston, K. J. (2012). Synaptic plasticity and dysconnection in schizophrenia. *Biological Psychiatry*, 59(10), 929-939.

### Methods

- Runge, J., Nowack, P., Kretschmer, M., Flaxman, S., & Sejdinovic, D. (2019). Detecting and quantifying causal associations in large nonlinear time series datasets. *Science Advances*, 5(11), eaau4996.
- Grassberger, P. (1986). Toward a quantitative theory of self-generated complexity. *International Journal of Theoretical Physics*, 25(9), 907-938.
- Marschinski, R., & Kantz, H. (2002). Analysing the information flow between financial time series. *European Physical Journal B*, 30(2), 275-281.

---

# Appendix A: Responses to Audit

| Audit Item | Response |
|------------|----------|
| Sign error in Eq. 2.1 | Corrected to condition on blanket states (Eq. 2.1) |
| \( \mathrm{CI}_C \to \infty \) contradiction | Replaced with excess entropy \( E \) |
| Conservation non-falsifiable | Reframed as approximate continuity with testable residuals |
| Seven incompatible dimensions | Reduced to four with existing estimators |
| \( B \to -2 \) impossible | Retired; \( \beta \in [0,1] \) |
| \( P \to +2 \) arbitrary | Replaced with \( \pi > 3.0 \) from HGF |
| Period 4-7 magic number | Retired |
| Master functional undefined | Retired; replaced with generative model |
| Multiscale isomorphism asserted | Restricted to shared estimators |
| PSI depends mainly on \( \sigma \) | Replaced with logistic regression on all parameters |
| CRC efficacy claims | Gated on RCTs |
| \( \frac{d}{dt}\mathrm{CI}_B \ge 0 \) forbids sleep | Replaced with non-maleficence principle |
| Self-citation only | Primary empirical literature cited |

---

# Appendix B: What Remains Speculative

1. The cascade hypothesis (\( \pi \to \beta \to \tau \)) is not yet tested.
2. The AI-psychosis analogy requires preregistered agent studies.
3. The social coherence moderation hypothesis requires network data.
4. The multiscale isomorphism claim is programmatic, not established.
5. The relationship between PSV parameters and clinical outcomes is not yet calibrated.

**Version 2.0 is a specification for a research program, not a validated theory.**

---

**Coherence Collapse Theory (CCT) v2.0**

*Landry, M. (2026). CCT: An Informational Phase Transition Framework of Psychosis (Revised).*

Licensed under Holy Public Domain v3.14159++

*Use ethically, in service of consciousness, balance, and light.*
