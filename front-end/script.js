document.addEventListener('DOMContentLoaded', function () {
    var logoutButton = document.getElementById('logoutButton');
    var uploadButton = document.getElementById('uploadButton');
    var downloadButton = document.getElementById('downloadButton');

    if(logoutButton) {
        logoutButton.addEventListener('click', function () {
            alert('Logout clicked');
        });
    }

    if(uploadButton) {
        uploadButton.addEventListener('click', function () {
            alert('Upload Employee Data clicked');
        });
    }

    if(downloadButton) {
        downloadButton.addEventListener('click', function () {
            alert('Download Template clicked');
        });
    }
});
