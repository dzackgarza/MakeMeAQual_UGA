
let parseQuestions = jsonQuestions => {
  let years = new Set(jsonQuestions.Problems.map(a => a.year));
  years.forEach(j => {
    $("#selectYears").append($("<option selected></option>").val(j).html(j));
  });

  let topics = new Set([].concat(...jsonQuestions.Problems.map(a => a.tags)))
  topics.forEach(j => {
    $("#selectTopics").append($("<option selected></option>").val(j).html(j));
  });

}

fetch("/questions.json")
  .then(response => response.json())
  .then(json => parseQuestions(json));

