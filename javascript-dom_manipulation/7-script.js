const el = document.querySelector('#list_movies');

async function movies () {
  const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
  const json = await response.json();
  for (const movie of json.results) {
    const list = document.createElement('li');
    list.innerText = movie.title;
    el.appendChild(list);
  }
}
movies();
