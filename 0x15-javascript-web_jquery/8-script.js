$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const lists = data.results;
  for (let i = 0; i < lists.length; i++) {
    $('UL#list_movies').append('<li>' + lists[i].title + '</li>');
  }
});
