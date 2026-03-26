const el = document.querySelector('#character');
// fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
//   .then((response) =>
//     response.json()
//   ).then((data) => {
//     el.innerText = data.name;
//   });

async function character () {
  const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  const json = await response.json();
  el.innerText = json.name;
}
character();
