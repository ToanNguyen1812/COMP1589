/* Function to fetch data from a JSON file - Demonstrates Data Integration.
 * This function dynamically populates the gallery with community artworks.*/
function loadCommunityArt() {
    // Use Relative Path to fetch data - Ensures cross-platform compatibility
    fetch('data/community.json')
        .then(response => {
            // Check if the response is successful
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();// Parse the response as JSON format
        }) 
        .then(data => {
            const galleryContainer = document.getElementById('gallery-list');
            
            // // Loop through the artworks array in the JSON file
            data.artworks.forEach(art => {
                // Construct a dynamic HTML block for each artwork card
                const artItem = `
                    <article class="art-card">
                        <div class="art-image-wrapper">
                            <img src="${art.image}" alt="${art.title}" class="art-image">
                         </div>
                        <div class="art-content">
                             <h3>${art.title}</h3>
                            <p><strong>Artist:</strong> ${art.artist}</p>
                            <p class="description">${art.description}</p>
                            <span class="tag">${art.type}</span>
                        </div>
                    </article>
            `;
                // Append the generated HTML to the container in the gallery page
                galleryContainer.innerHTML += artItem;
            });
        })
        .catch(error => {
            // Error handling for robust application performance
            console.error('Error loading community art data:', error);
        });
}

// Event Listener to execute the script once the DOM is fully loaded.
document.addEventListener('DOMContentLoaded', () => {
    // Only execute if the gallery container exists on the current page
    if (document.getElementById('gallery-list')) {
        loadCommunityArt();
    }
});