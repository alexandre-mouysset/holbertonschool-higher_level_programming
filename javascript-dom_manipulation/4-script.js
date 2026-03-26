const el = document.querySelector('#add_item');

el.addEventListener('click', () => {
  const el = document.querySelector('.my_list');
  const listElement = document.createElement('li');
  listElement.innerText = 'Item';
  el.appendChild(listElement);
});
