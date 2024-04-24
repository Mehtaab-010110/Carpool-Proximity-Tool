document.addEventListener('DOMContentLoaded', function() {
    var logoutButton = document.getElementById('logoutButton');
    var dataTable = document.getElementById('data-table');

    // Sample data
    var sampleData = [
        { companyName: "Airdrie", employeeCount: 23, matches500m: 12, matches1000m: 7 },
        { companyName: "Cochrane", employeeCount: 12, matches500m: 4, matches1000m: 2 },
        { companyName: "Chestermere", employeeCount: 15, matches500m: 10, matches1000m: 4 },
        { companyName: "NW Calgary", employeeCount: 41, matches500m: 19, matches1000m: 6 },
        { companyName: "NE Calgary", employeeCount: 8, matches500m: 3, matches1000m: 0 },
        { companyName: "SW Calgary", employeeCount: 36, matches500m: 20, matches1000m: 8 },
        { companyName: "SE Calgary", employeeCount: 11, matches500m: 2, matches1000m: 0 },
    ]
    // Function to populate the table
    function populateTable(data) {
        data.forEach(function(item) {
            var row = document.createElement('tr');
            row.innerHTML = `
                <td>${item.companyName}</td>
                <td>${item.employeeCount}</td>
                <td>${item.matches500m}</td>
                <td>${item.matches1000m}</td>
            `;
            dataTable.appendChild(row);
        });
    }

    populateTable(sampleData);

    logoutButton.addEventListener('click', function(event) {
        event.preventDefault();
        if (confirm('Are you sure you want to logout?')) {
            window.location.href = 'index.html';
        }
    });
});
