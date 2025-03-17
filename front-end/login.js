// Event handling for the login form submission
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();  // Prevent the default form submission behavior
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    
    // Simple authentication check
    if(username === 'user' && password === '1234') {
        alert('Login successful');
        window.location.href = 'home_page.html'; // Redirect to the home page upon successful login
    } else {
        alert('Login failed');  // Notify user of failed login attempt
    }
});
