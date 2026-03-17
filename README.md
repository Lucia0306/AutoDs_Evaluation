# AutoDs_Evaluation
This repository contains the Evaluation Agent for the AutoDS multi-agent workflow.

The Evaluation Agent consumes modelling artifacts produced by the Modelling Agent, performs benchmark comparison across candidate models, and generates structured technical evaluation outputs for downstream reporting.

# Responsibility
The Evaluation Agent is responsible for:
- benchmarking candidate models
- summarising model comparison results
- providing best-model selection evidence
- generating structured technical evaluation outputs

# Input
The Evaluation Agent expects modelling artifacts under:
input/modelling_outputs/

Required input files:
- leaderboard.csv
- best_model_metrics.json
- best_model_predictions.csv
- diagnostics.json
- modelling_summary.json

# Output
The Evaluation Agent generates evaluation outputs under:
output/evaluation_outputs/

Generated files:
- evaluation_summary.json
- evaluation_comparison_table.csv

# Run

Run the Evaluation Agent with:
python run_evaluation.py

# Curremt Features
- Reads modelling artifacts exported by the Modelling Agent
- Builds benchmark comparison across candidate models
- Extracts best-model selection evidence
- Summarises technical evaluation results
- Saves structured outputs for downstream reporting

# Benchmark Logic
The Evaluation Agent uses the leaderboard exported by the Modelling Agent to compare candidate models under a unified benchmark view.

It reports:
- candidate model count
- primary metric
- top-ranked model
- selected best model
- best-model selection evidence
