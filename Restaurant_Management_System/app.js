document.addEventListener('DOMContentLoaded', function() {
    const menuItemsDiv = document.getElementById('menu-items');

    // Fetch and display menu items from the server
    fetch('/api/menu')
        .then(response => response.json())
        .then(data => {
            data.forEach(item => {
                const itemDiv = document.createElement('div');
                itemDiv.className = 'menu-item';
                itemDiv.innerHTML = `<h3>${item.name}</h3><p>Price: ${item.price}</p>`;
                menuItemsDiv.appendChild(itemDiv);
            });
        });

    document.getElementById('add-item').addEventListener('click', function() {
        // Logic to add a new menu item
    });
});
