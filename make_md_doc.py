#!/usr/bin/python3

import yaml

with open(r'combined_questions.yaml') as file:
    qs = yaml.load(file)

print("Read YAML questions")
    
modqs = [f"\n# Question {i+1}\n\n" + q['question'] for i, q in enumerate(qs)]
with open("combined_questions.md", 'w') as out_file:
    out_file.writelines(modqs)
    print("Wrote markdown document")
