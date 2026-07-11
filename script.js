// Handle the first page login form.
const loginForm = document.getElementById('login-form');

if (loginForm) {
  loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const name = document.getElementById('name').value.trim();
    const phone = document.getElementById('phone').value.trim();

    if (!name || !phone) {
      alert('Please enter your name and phone number.');
      return;
    }

    try {
      const response = await fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, phone })
      });

      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.message || 'Unable to save user details');
      }

      localStorage.setItem('userName', name);
      localStorage.setItem('userPhone', phone);
      window.location.href = 'booking.html';
    } catch (error) {
      alert(error.message);
    }
  });
}
