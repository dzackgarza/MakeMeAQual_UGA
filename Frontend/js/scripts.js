
let parseQuestions = jsonQuestions => {
  years = Array.from(new Set(jsonQuestions.Problems.map(a => a.year)));
  //years.forEach(j => {
    //$("#selectYears").append($("<option selected></option>").val(j).html(j));
  //});

  let topics = Array.from(new Set([].concat(...jsonQuestions.Problems.map(a => a.tags))));
  //topics.forEach(j => {
    //$("#selectTopics").append($("<option selected></option>").val(j).html(j));
  //});


  $('#selectYears').selectize({
    options: years.map(a => ({"text": a, "value": a})),
    items: years
  })
  $('#selectTopics').selectize({
    options: topics.map(a => ({"text": a, "value": a})),
    items: topics
  })
  window.questions = jsonQuestions.Problems;
}

$('#makeQual').on('click', function(event) {
  debugger;
  event.preventDefault(); 
});

fetch("/questions.json")
  .then(response => response.json())
  .then(json => parseQuestions(json));

