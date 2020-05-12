# How to Contribute

For those that already know what this tool is, there are a number of ways you can help improve it:

- Contributing links to source material (e.g. school web pages containing old quals)
- Contributing Latex versions of questions , which is a **massive** help.
    - The easiest way is to email me `.tex` files containing typeset questions.
    Additional information such as the source university, what year each question is from, and any other metadata is all helpful and can be incorporated into the tool.
  - You can also [submit a pull request](https://yangsu.github.io/pull-request-tutorial/), i.e. clone the repository to your computer, add or modify whatever files you'd like, then merge your changes back into the main project. 
- Moving tex'd questions into `.yaml` data files
  - See e.g. [the Algebra yaml file](Algebra/QualQuestions.yaml)

# MakeMeAQual UGA
An adaptation of Jonathan Love's [Make Me a Qual](http://stanford.edu/~jonlove/qual/makeit.html) tool for the University of Georgia qualifying exams.

# Info

- Questions parsed from UGA exams contained in `ReviewDoc/UGA Questions/Quals.md`
- Metadata being moved to `QualQuestions.yaml`.
- To generate JSON: install the [yq](https://github.com/mikefarah/yq) tool and run  `cat QualQuestions.yaml | yq '.' > OutputExample.json`


# Syllabus

Todo.
