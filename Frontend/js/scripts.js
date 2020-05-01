

let parseQuestions = jsonQuestions => {
  let years = Array.from(new Set(jsonQuestions.Problems.map(a => a.year)));
  //years.forEach(j => {
    //$("#selectYears").append($("<option selected></option>").val(j).html(j));
  //});

  let topics = Array.from(new Set([].concat(...jsonQuestions.Problems.map(a => a.tags))));
  //topics.forEach(j => {
    //$("#selectTopics").append($("<option selected></option>").val(j).html(j));
  //});


  $('#selectYears').selectize({
    options: years.reduce((o, j) => { o[j] = j; return o;}, {})
  })
  $('#selectTopics').selectize({
    options: topics.reduce((o, j) => { o[j] = j; return o;}, {})
  })
}

fetch("/questions.json")
  .then(response => response.json())
  .then(json => parseQuestions(json));

