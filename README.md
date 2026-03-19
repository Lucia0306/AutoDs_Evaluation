# AutoDs_Evaluation
This repository contains the Evaluation Agent for the AutoDS multi-agent workflow.

The Evaluation Agent consumes modelling artifacts produced by the Modelling Agent, benchmarks candidate models under a common evaluation framework, validates model-selection consistency across exported artifacts and performs prediction-level error analysis for the selected best model.

# Responsibility
The Evaluation Agent is responsible for:
- benchmarking candidate models
- comparing model performance under a unified benchmark
- validating best-model selection consistency
- providing technical evidence for best-model selection
- performing prediction-level error analysis
- generating structured technical evaluation outputs

# Input
The Evaluation Agent expects modelling artifacts under:
input/modelling_outputs/

# Required input files:
- leaderboard.csv
- best_model_metrics.json
- diagnostics.json
- modelling_summary.json

# Optional input files
- best_model_predictions.csv
- best_model_feature_importance.csv
- modelling_metadata.json
Note: best_model_predictions.csv is optional, but it is required if prediction-level error analysis is needed.

# Output
The Evaluation Agent generates evaluation outputs under:
output/evaluation_outputs/

# Generated files
- evaluation_summary.json
- evaluation_comparison_table.csv

# Run
Run the Evaluation Agent with:
python run_evaluation.py

# Curremt Features
- Reads modelling artifacts exported by the Modelling Agent
- Benchmarks candidate models under a unified comparison view
- Validates consistency across leaderboard, metrics, diagnostics, and modelling summary
- Extracts technical evidence for best-model selection
- Performs prediction-level error analysis using y_true and y_pred when prediction outputs are available
- Saves structured outputs for downstream reporting

# Benchmark Logic
The Evaluation Agent uses the leaderboard exported by the Modelling Agent to compare candidate models under a unified benchmark view.

It reports:
- candidate model count
- primary metric
- top-ranked model
- selected best model
- performance margin between the top two models
- selected best model
- best-model selection evidence

# Evaluation Logic
In addition to benchmark comparison, the Evaluation Agent also validates whether exported modelling artifacts are internally consistent.

It checks whether:
- the selected best model matches the leaderboard rank-1 model
- the selected best model matches the top-ranked model under the primary metric
- best-model metrics align with the modelling summary
- diagnostics align with the selected best model

If prediction outputs are available, the agent also performs prediction-level error analysis, including:
- confusion matrix statistics
- accuracy
- precision
- recall
- f1 score
- dominant error type
