// Empty JS for your own code to be here

let parseQuestions = jsonQuestions => {
  debugger;
}

fetch("/questions.json")
  .then(response => response.json())
  .then(json => parseQuestions(json));

