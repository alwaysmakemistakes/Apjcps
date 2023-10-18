let deletePlastinkaModal = document.querySelector('#deletePlastinka');

deletePlastinkaModal.addEventListener('show.bs.modal', function(event) {
  let form = document.querySelector('#deletePlastinkaForm');
  form.action = event.relatedTarget.dataset.url;
  let plastinkaName = document.querySelector('#plastinkaName');
  plastinkaName.textContent = event.relatedTarget.closest('.row').querySelector('h4').textContent;
});
