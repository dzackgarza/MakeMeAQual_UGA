#!/usr/bin/python3

import yaml

with open(r'Combined_Questions.yaml') as file:
    qs = yaml.load(file)

print("Read YAML questions")

Algebra_qs = [q for q in qs if q['exam'] == "Algebra"]
Real_qs = [q for q in qs if q['exam'] == "Real_Analysis"]
Complex_qs = [q for q in qs if q['exam'] == "Complex_Analysis"]
Topology_qs = [q for q in qs if q['exam'] == "Topology"]

out_str = """---
title: Combined Qual Questions
---

"""

out_str += f"# Algebra ({len(Algebra_qs)} Questions)\n"
out_str += "\n".join([f"\n**Question {i+1}**\n\n" + q['question'] for i, q in enumerate(Algebra_qs)])

out_str += f"\n# Real Analysis ({len(Real_qs)} Questions)\n"
out_str += "\n".join([f"\n**Question {i+1}**\n\n" + q['question'] for i, q in enumerate(Real_qs)])

out_str += f"\n# Complex Analysis ({len(Complex_qs)} Questions)\n"
out_str += "\n".join([f"\n**Question {i+1}**\n\n" + q['question'] for i, q in enumerate(Complex_qs)])

out_str += f"\n# Topology ({len(Topology_qs)} Questions)\n"
out_str += "\n".join([f"\n**Question {i+1}**\n\n" + q['question'] for i, q in enumerate(Topology_qs)])

with open("Combined_Questions.md", "w") as out_file:
    out_file.write(out_str)
    print("Wrote markdown document: Combined_Questions.md. Rendering PDF..")
 
