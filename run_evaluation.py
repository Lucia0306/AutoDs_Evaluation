from pathlib import Path
from evaluation import EvaluationAgent, EvaluationConfig

BASE_DIR = Path(__file__).resolve().parent

config = EvaluationConfig(
    modelling_output_dir=str(BASE_DIR / "input" / "modelling_outputs"),
    output_dir=str(BASE_DIR / "output" / "evaluation_outputs"),
    save_artifacts=True,
)

agent = EvaluationAgent(config)
summary = agent.run()

print("Evaluation completed.")
print(agent.get_minimal_summary())