const el = document.querySelector('#toggle_header');

el.addEventListener('click', () => {
  const el = document.querySelector('header');
  if (el.classList.contains('green')) {
    el.classList.replace('green', 'red');
  } else if (el.classList.contains('red')) {
    el.classList.replace('red', 'green');
  }
});
