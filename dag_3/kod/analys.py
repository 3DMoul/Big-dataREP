import json

with open("Big-dataREP/dag_3/kod/output/model_metrics.json") as file:
    result = json.load(file)

print(result["model"])
print(result["baseline"])