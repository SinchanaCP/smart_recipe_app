const form = document.querySelector('.search-form');
const loader = document.querySelector('.loader');

if (form) {
  form.addEventListener('submit', () => {
    loader.classList.remove('hidden');
  });
}
