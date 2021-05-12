$.getJSON(
  'https://swapi-api.hbtn.io/api/films/?format=json',
  function ({ results }) {
    results.forEach(film => {
      $('UL#list_movies').append(`<li>${film.title}</li>`);
    });
  }
);
