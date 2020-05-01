
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
    items: years,
    onChange: updateSelectedQuestions
  })
  $('#selectTopics').selectize({
    options: topics.map(a => ({"text": a, "value": a})),
    items: topics,
    onChange: updateSelectedQuestions
  })
  window.questions = jsonQuestions.Problems;
}

let updateSelectedQuestions = () => {
  debugger;
}

$('#makeQual').on('click', function(event) {
  event.preventDefault(); 
  updateSelectedQuestions();
});

fetch("/questions.json")
  .then(response => response.json())
  .then(json => parseQuestions(json));

