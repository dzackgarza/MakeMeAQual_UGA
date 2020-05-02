let intersect = (s1, s2) => {
  let s = new Set( [...s1].filter(x => s2.has(x)) );
  return s;
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
  let selectedTopics = new Set( $('#selectTopics').val());
  let selectedYears = new Set( $('#selectYears').val() );
  let selectedQuestions = window.questions
    .filter(a => intersect(new Set(a.tags), selectedTopics).size > 0)
    .filter(a => intersect(new Set([a.year]), selectedYears).size > 0);

  debugger;
}

$('#makeQual').on('click', function(event) {
  event.preventDefault(); 
  updateSelectedQuestions();
});

fetch("/questions.json")
  .then(response => response.json())
  .then(json => parseQuestions(json));

