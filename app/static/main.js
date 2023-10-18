'use strict';

function imagePreviewHandler(event) {
    if (event.target.files && event.target.files[0]) {
        let reader = new FileReader();
        reader.onload = function (e) {
            let img = document.querySelector('.background-preview > img');
            img.src = e.target.result;
            if (img.classList.contains('d-none')) {
                let label = document.querySelector('.background-preview > label');
                label.classList.add('d-none');
                img.classList.remove('d-none');
            }
        }
        reader.readAsDataURL(event.target.files[0]);
    }
}

function openLink(event) {
    let row = event.target.closest('.row');
    if (row.dataset.url) {
        window.location = row.dataset.url;
    }
}



window.onload = function() {
    let background_img_field = document.getElementById('background_img');
    if (background_img_field) {
        background_img_field.onchange = imagePreviewHandler;
    }
    for (let course_elm of document.querySelectorAll('.courses-list .row')) {
        course_elm.onclick = openLink;
    }
}


document.addEventListener('DOMContentLoaded', function() {
    var textarea = document.getElementById('description');
    var editor = new EasyMDE({ element: textarea });
});

document.addEventListener('DOMContentLoaded', function() {
    var textarea = document.getElementById('text');
    var editor = new EasyMDE({ element: textarea });
});


  