window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const suggestionsContainer = document.getElementById('search-suggestions');

    searchInput.addEventListener('input', function () {
        let query = this.value.trim();

        if (query.length >= 1) {  // Show suggestions after 1 letter
            fetch(`/search-products?q=${query}`)
                .then(response => response.json())
                .then(results => {
                    suggestionsContainer.innerHTML = '';  // Clear previous suggestions

                    if (results.length > 0) {
                        results.forEach(product => {
                            let item = document.createElement('div');
                            item.classList.add('dropdown-item', 'search-result');
                            item.innerHTML = `
                                <img src="${product.image_url}" alt="${product.name}" class="me-2" width="40" height="40">
                                <span class="search-text">${product.name}</span>`;

                            item.addEventListener('click', function () {
                                window.location.href = `/product-details/${product.id}`;
                            });

                            suggestionsContainer.appendChild(item);
                        });
                        suggestionsContainer.style.display = 'block';
                    } else {
                        suggestionsContainer.style.display = 'none';
                    }
                });
        } else {
            suggestionsContainer.style.display = 'none';
        }
    });

    // Hide suggestions when clicking outside
    document.addEventListener('click', function (event) {
        if (!searchInput.contains(event.target) && !suggestionsContainer.contains(event.target)) {
            suggestionsContainer.style.display = 'none';
        }
    });
});
