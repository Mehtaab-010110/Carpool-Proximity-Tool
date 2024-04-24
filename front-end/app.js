document.addEventListener('DOMContentLoaded', function() {
    var logoutButton = document.getElementById('logoutButton');
    var uploadButton = document.getElementById('uploadButton');
    var downloadButton = document.getElementById('downloadButton');
    var fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.style.display = 'none'; // Hide the file input element
    document.body.appendChild(fileInput); // Append to the DOM

    logoutButton?.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default action
        // Display confirmation dialog
        if (confirm('Are you sure you want to logout?')) {
            window.location.href = 'index.html'; // Redirect to the login page if user confirms
        } else {
            // Do nothing if user cancels
            console.log('Logout canceled.');
        }
    });

    downloadButton?.addEventListener('click', function() {
        alert('Download Template clicked');
        // Placeholder for initiating a download
    });

    uploadButton?.addEventListener('click', function() {
        if (fileInput.getAttribute('data-uploaded') === 'true') {
            // If a file was previously selected, simulate its change event to perform the upload
            fileInput.dispatchEvent(new Event('change'));
        } else {
            // Trigger the file input's click event to open the file dialog
            fileInput.click();
        }
    });

    fileInput.addEventListener('change', function() {
        if (this.files && this.files[0]) {
            var formData = new FormData();
            formData.append('file', this.files[0]);

            // Perform the POST request to send the file
            fetch('your-upload-url', {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                alert('File uploaded successfully!');
            })
            .catch((error) => {
                console.error('Error:', error);
                alert('Failed to upload file.');
            });

            fileInput.setAttribute('data-uploaded', 'true');
            uploadButton.textContent = 'CONFIRM UPLOAD'; // Change button text to prompt for upload
        }
    });
});
