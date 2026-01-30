// Flashcard interaction logic

let currentIndex = 0;
let reviewedCount = 0;
let isFlipped = false;

// Shuffle array in place (Fisher-Yates)
function shuffle(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    if (cards && cards.length > 0) {
        // Create reverse copies (English front, French back)
        const reversed = cards.map(c => Object.assign({}, c, { reversed: true }));
        cards.push(...reversed);

        // Randomize order
        shuffle(cards);

        document.getElementById('total-cards').textContent = cards.length;
        showCard(0);
    }
});

// Display a card
function showCard(index) {
    if (index >= cards.length) {
        showSessionComplete();
        return;
    }

    const card = cards[index];
    currentIndex = index;
    isFlipped = false;

    // Update card content based on direction
    if (card.reversed) {
        // English on front, French (with pronunciation) on back
        document.getElementById('french-word').textContent = card.english;
        document.getElementById('pronunciation').textContent = '';
        document.getElementById('french-word-back').textContent = card.french;
        document.getElementById('pronunciation-back').textContent = card.pronunciation || '';
        document.getElementById('english-word').textContent = card.english;
    } else {
        // Normal: French on front, English on back
        document.getElementById('french-word').textContent = card.french;
        document.getElementById('pronunciation').textContent = card.pronunciation || '';
        document.getElementById('french-word-back').textContent = card.french;
        document.getElementById('pronunciation-back').textContent = card.pronunciation || '';
        document.getElementById('english-word').textContent = card.english;
    }

    // Reset flip state
    document.getElementById('flashcard').classList.remove('flipped');

    // Hide rating area
    document.getElementById('rating-area').style.display = 'none';

    // Update progress indicator
    document.getElementById('current-index').textContent = index + 1;
}

// Flip the card
function flipCard() {
    const flashcard = document.getElementById('flashcard');
    isFlipped = !isFlipped;

    if (isFlipped) {
        flashcard.classList.add('flipped');
        // Show rating area after flip
        setTimeout(() => {
            document.getElementById('rating-area').style.display = 'block';
        }, 300);
    } else {
        flashcard.classList.remove('flipped');
        document.getElementById('rating-area').style.display = 'none';
    }
}

// Submit a rating
async function submitRating(quality) {
    const card = cards[currentIndex];

    // Disable rating buttons temporarily
    const buttons = document.querySelectorAll('.rating-btn');
    buttons.forEach(btn => btn.disabled = true);

    try {
        const response = await fetch(reviewUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                card_id: card.id,
                quality: quality
            })
        });

        if (!response.ok) {
            throw new Error('Failed to submit review');
        }

        const result = await response.json();
        reviewedCount++;

        // Brief delay before showing next card
        setTimeout(() => {
            buttons.forEach(btn => btn.disabled = false);
            showCard(currentIndex + 1);
        }, 300);

    } catch (error) {
        console.error('Error submitting review:', error);
        buttons.forEach(btn => btn.disabled = false);
        alert('Failed to save review. Please try again.');
    }
}

// Show session complete screen
function showSessionComplete() {
    document.querySelector('.flashcard-area').style.display = 'none';
    document.getElementById('rating-area').style.display = 'none';

    document.getElementById('reviewed-count').textContent = reviewedCount;
    document.getElementById('session-complete').style.display = 'block';
}

// Exit session early
function exitSession() {
    if (reviewedCount > 0) {
        showSessionComplete();
    } else {
        window.location.href = dashboardUrl;
    }
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Space to flip
    if (e.code === 'Space' && !e.target.matches('button, input, textarea')) {
        e.preventDefault();
        flipCard();
    }

    // Number keys for ratings (when card is flipped)
    if (isFlipped && e.key >= '0' && e.key <= '5') {
        submitRating(parseInt(e.key));
    }
});
