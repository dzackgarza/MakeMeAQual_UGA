Set.prototype.intersect = s2 => {
  new Set( [...this].filter(x => s2.has(x)) );
}

let parseQuestions = jsonQuestions => {
  years = Array.from(new Set(jsonQuestions.Problems.map(a => a.year))).sort();
  //years.forEach(j => {
    //$("#selectYears").append($("<option selected></option>").val(j).html(j));
  //});

  let topics = Array.from(new Set([].concat(...jsonQuestions.Problems.map(a => a.tags)))).sort();
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
  window.selectedQuestions = jsonQuestions.Problems;
}

let updateSelectedQuestions = () => {
  let selectedTopics = $('#selectTopics').val();
  let selectedYears = $('#selectYears').val();
  window.selectedQuestions = window.questions
  debugger;
}

$('#makeQual').on('click', function(event) {
  event.preventDefault(); 
  updateSelectedQuestions();
});

fetch("/questions.json")
  .then(response => response.json())
  .then(json => parseQuestions(json));

