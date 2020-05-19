# How to Contribute

For those that already know what this tool is, there are a number of ways you can help improve it:

- Contributing links to source material (e.g. school web pages containing old quals)

- Contributing Latex versions of questions , which is a **massive** help.
  - The easiest way is to [email me](mailto:dzackgarza@gmail.com) any `.tex` files containing typeset questions.
  - Additional information such as the source university, what year each question is from, and other metadata is all useful and can be incorporated into the tool.
  - You can also [submit a pull request](https://yangsu.github.io/pull-request-tutorial/), i.e. clone the repository to your computer, add or modify whatever files you'd like, then merge your changes back into the main project. 

- Contributing questions directly:
  - Using Algebra as an example subject, either modify or create a new folder for the university under the `Questions/Algebra` directory.
  - (Optional) Add original tex or markdown files to the folder.
  - Add a `Questions.yaml` file, and populate it in plain text with entries similar to this example.
    Note that the only *required* fields are year, exam, and question, and you can enter 0 for the year if it's not applicable.
```{yaml}
- year: 2019
  season: Spring 
  exam: Algebra
  number: 3
  tags:
    - Modules
    - Homomorphisms
  question: |
    Let $R$ be a ring and $M, M'$ be modules over...
    Then define
    $$
    \varphi: M \to M' \\
    x \mapsto \varphi(x)
    $$
    where ...
```
  
  - Submit a pull request with your additions!

# MakeMeAQual UGA
An adaptation of Jonathan Love's [Make Me a Qual](http://stanford.edu/~jonlove/qual/makeit.html) tool for the University of Georgia qualifying exams.

# Info

- Questions are first typeset in markdown/latex and used to generate a giant PDF containing all questions
- Latex for questions is then moved into yaml files, along with relevant metadata
- yaml files are converted to JSON for the frontend to read
  - To generate JSON: install the [yq](https://github.com/mikefarah/yq) tool and run  `cat QualQuestions.yaml | yq '.' > OutputExample.json`
- The frontend reads JSON file, sets up filters based on what it finds, and passes the tex'd questions to the backend
- The backend creates a markdown document and feeds it through pandoc to produce either a web page or a PDF containing a qualifying exam.
