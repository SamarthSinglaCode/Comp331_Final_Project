document.getElementById('food-form').addEventListener('submit', function(e) {
    e.preventDefault();  // Prevents the form from submitting normally

    // Get the food name input
    let foodName = document.getElementById('food-name').value;

    // Prepare data to be sent to the backend
    let foodData = { "food_name": foodName };

    // Send data to the backend using fetch (AJAX request)
    fetch('http://127.0.0.1:5000/predict', {  // Ensure the correct backend URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(foodData)
    })
    .then(response => response.json())
    .then(data => {
        // Display the prediction result and nutritional content
        document.getElementById('result').style.display = 'block';
        document.getElementById('prediction').textContent = `Food Status: ${data.food_status}`;
        document.getElementById('nutrition').textContent = `Protein: ${data.protein}g, Fat: ${data.fat}g, Carbohydrates: ${data.carbohydrates}g`;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error with the request.');
    });
    
});
