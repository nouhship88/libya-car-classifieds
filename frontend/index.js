const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3000;



app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');

app.get('/', (req, res) => {
    res.send('Welcome to the Libya Car Classifieds!');
});

// Route to fetch car listings from the Django backend
app.get('/cars', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:8000/api/cars/');
        res.render('index', { cars: response.data });
    } catch (error) {
        res.status(500).send('Error fetching car data');
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
