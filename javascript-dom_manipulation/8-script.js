let el;

document.addEventListener('DOMContentLoaded', () => {
  el = document.querySelector('#hello');
  display();
});

async function display () {
  const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
  const json = await response.json();
  const cle = json.hello;
  el.innerText = cle;
}
