const el = document.querySelector('#update_header');

el.addEventListener('click', () => {
  const el = document.querySelector('header');
  el.innerText = 'New Header!!!';
});
