// Load the required modules
const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON and form-encoded bodies
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files such as HTML, CSS, and JavaScript
app.use(express.static(__dirname));

// In-memory arrays for users and bookings
const users = [];
const bookings = [];

// Serve the homepage
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Save user details from the login page
app.post('/login', (req, res) => {
  const { name, phone } = req.body;

  if (!name || !phone) {
    return res.status(400).json({ message: 'Name and phone are required.' });
  }

  users.push({ name, phone, createdAt: new Date().toISOString() });
  res.json({ message: 'User saved successfully' });
});

// Save booking details
app.post('/book', (req, res) => {
  const { name, phone, pickup, drop, fare } = req.body;

  if (!name || !phone || !pickup || !drop || fare === undefined || fare === null || fare === '') {
    return res.status(400).json({ message: 'Name, phone, pickup, drop, and fare are required.' });
  }

  const booking = {
    name,
    phone,
    pickup,
    drop,
    fare: Number(fare),
    createdAt: new Date().toISOString()
  };

  bookings.push(booking);
  res.json({ message: 'Booking saved successfully', booking });
});

// Return all bookings
app.get('/bookings', (req, res) => {
  res.json(bookings);
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
