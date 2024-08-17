document.addEventListener('DOMContentLoaded', function () {
    const itemsTableBody = document.getElementById('items-table-body');

    function updateTotalPrice() {
        let totalQuantity = 0;
        let totalPrice = 0;

        itemsTableBody.querySelectorAll('tr').forEach(row => {
            const quantity = parseInt(row.querySelector('.quantity').value) || 0;
            const price = parseFloat(row.querySelector('.price').textContent) || 0;
            const lamination = row.querySelector('.lamination').checked ? 10 : 0;

            totalQuantity += quantity;
            totalPrice += (price + lamination) * quantity;

            row.querySelector('.total-price').textContent = (price + lamination) * quantity;
        });

        document.getElementById('total-quantity').textContent = totalQuantity;
        document.getElementById('total-price').textContent = totalPrice.toFixed(2);
    }

    itemsTableBody.addEventListener('click', function (event) {
        if (event.target.classList.contains('increment')) {
            const input = event.target.previousElementSibling;
            input.value = parseInt(input.value) + 1;
        } else if (event.target.classList.contains('decrement')) {
            const input = event.target.nextElementSibling;
            if (parseInt(input.value) > 1) {
                input.value = parseInt(input.value) - 1;
            }
        }

        updateTotalPrice();
    });

    itemsTableBody.addEventListener('change', function (event) {
        if (event.target.classList.contains('lamination')) {
            updateTotalPrice();
        }
    });

    updateTotalPrice();

    const uploadButton = document.querySelector('.making_order button[type="button"]');
    const imageInput = document.getElementById('imageFile');
    const imagesPreviewContainer = document.querySelector('.images-preview-container');

    if (uploadButton) {
        uploadButton.addEventListener('click', function () {
            console.log('Открытие модального окна для загрузки изображений');
        });
    }

    if (imageInput) {
        imageInput.addEventListener('change', function () {
            const files = imageInput.files;
            imagesPreviewContainer.innerHTML = '';  

            Array.from(files).forEach(file => {
                const reader = new FileReader();
                reader.onload = function (e) {
                    const img = document.createElement('img');
                    img.src = e.target.result;
                    img.style.width = '100px';
                    img.style.height = '100px';
                    img.style.margin = '10px';

                    imagesPreviewContainer.appendChild(img);
                };
                reader.readAsDataURL(file);
            });
        });
    }
});
