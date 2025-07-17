document.getElementById('recommendation-form').addEventListener('submit', function(event) {
    // Prevent the default form submission which reloads the page
    event.preventDefault();

    // Get values from the form
    const budget = document.getElementById('budget').value;
    const season = document.getElementById('season').value;
    const interests = document.getElementById('interests').value;
    const resultsContainer = document.getElementById('results-container');

    // Construct the query parameters string
    let queryParams = [];
    if (budget) {
        queryParams.push(`budget=${encodeURIComponent(budget)}`);
    }
    if (season) {
        queryParams.push(`season=${encodeURIComponent(season)}`);
    }
    if (interests) {
        queryParams.push(`interests=${encodeURIComponent(interests)}`);
    }

    // The base URL of your Flask API
    const apiUrl = `http://127.0.0.1:5000/recommend?${queryParams.join('&')}`;

    // Clear previous results and show a loading message
    resultsContainer.innerHTML = '<p>Fetching recommendations...</p>';

    // Fetch data from the API
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Clear the loading message
            resultsContainer.innerHTML = '';

            if (data.length === 0) {
                resultsContainer.innerHTML = '<p>No destinations found matching your criteria. Please try different options!</p>';
                return;
            }

            // Create and append a card for each destination
            data.forEach(destination => {
                const card = document.createElement('div');
                card.className = 'result-card';

                const interestsHtml = destination.interests.map(interest => 
                    `<span class="interest-tag">${interest}</span>`
                ).join('');

                card.innerHTML = `
                    <h3>${destination.name}</h3>
                    <p><strong>Budget:</strong> ${destination.budget}</p>
                    <p><strong>Best Season:</strong> ${destination.season}</p>
                    <div class="interests-list">${interestsHtml}</div>
                `;
                resultsContainer.appendChild(card);
            });
        })
        .catch(error => {
            console.error('Error fetching recommendations:', error);
            resultsContainer.innerHTML = '<p>Sorry, something went wrong. Please ensure the API is running and try again.</p>';
        });
});