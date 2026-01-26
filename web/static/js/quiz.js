// Quiz interaction logic

let currentQuestion = null;
let correctCount = 0;
let totalCount = 0;
let isAnswered = false;
const MAX_QUESTIONS = 10;

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    loadNextQuestion();
    setupOptionButtons();
});

// Setup option button click handlers
function setupOptionButtons() {
    const buttons = document.querySelectorAll('.option-btn');
    buttons.forEach((btn, index) => {
        btn.addEventListener('click', () => selectOption(index));
    });
}

// Load a new question
async function loadNextQuestion() {
    if (totalCount >= MAX_QUESTIONS) {
        showQuizComplete();
        return;
    }

    isAnswered = false;

    // Reset UI
    document.getElementById('feedback-area').style.display = 'none';
    const buttons = document.querySelectorAll('.option-btn');
    buttons.forEach(btn => {
        btn.classList.remove('selected', 'correct', 'incorrect', 'show-correct');
        btn.disabled = false;
    });

    // Show loading state
    document.getElementById('quiz-french-word').textContent = 'Loading...';
    document.getElementById('quiz-pronunciation').textContent = '';

    try {
        const response = await fetch(questionUrl);
        if (!response.ok) {
            throw new Error('Failed to load question');
        }

        currentQuestion = await response.json();

        // Update question display
        document.getElementById('quiz-french-word').textContent = currentQuestion.card.french;
        document.getElementById('quiz-pronunciation').textContent = currentQuestion.card.pronunciation || '';

        // Update options
        currentQuestion.options.forEach((option, index) => {
            const btn = document.querySelector(`.option-btn[data-index="${index}"]`);
            const imageSpan = btn.querySelector('.option-image');
            imageSpan.textContent = option.image;
        });

    } catch (error) {
        console.error('Error loading question:', error);
        document.getElementById('quiz-french-word').textContent = 'Error loading question';
    }
}

// Handle option selection
async function selectOption(index) {
    if (isAnswered || !currentQuestion) return;

    isAnswered = true;
    totalCount++;

    const selectedBtn = document.querySelector(`.option-btn[data-index="${index}"]`);
    const correctIndex = currentQuestion.correct_index;
    const isCorrect = index === correctIndex;

    // Disable all buttons
    document.querySelectorAll('.option-btn').forEach(btn => btn.disabled = true);

    // Mark selected option
    selectedBtn.classList.add('selected');

    // Show correct/incorrect feedback
    if (isCorrect) {
        correctCount++;
        selectedBtn.classList.add('correct');

        // Trigger unicorn for Family user on correct answer
        if (isFamily && typeof triggerUnicorn === 'function') {
            triggerUnicorn();
        }
    } else {
        selectedBtn.classList.add('incorrect');
        // Show the correct answer
        const correctBtn = document.querySelector(`.option-btn[data-index="${correctIndex}"]`);
        correctBtn.classList.add('show-correct');
    }

    // Submit answer to server
    try {
        await fetch(answerUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                card_id: currentQuestion.card.id,
                correct: isCorrect
            })
        });
    } catch (error) {
        console.error('Error submitting answer:', error);
    }

    // Update score display
    document.getElementById('score-correct').textContent = correctCount;
    document.getElementById('score-total').textContent = totalCount;

    // Show feedback
    showFeedback(isCorrect);
}

// Show feedback after answer
function showFeedback(isCorrect) {
    const feedbackArea = document.getElementById('feedback-area');
    const feedbackMessage = document.getElementById('feedback-message');
    const feedbackEnglish = document.getElementById('feedback-english');

    if (isCorrect) {
        feedbackMessage.textContent = getCorrectMessage();
        feedbackMessage.className = 'feedback-message correct';
    } else {
        feedbackMessage.textContent = getIncorrectMessage();
        feedbackMessage.className = 'feedback-message incorrect';
    }

    feedbackEnglish.textContent = `${currentQuestion.card.french} = ${currentQuestion.card.english}`;

    feedbackArea.style.display = 'block';

    // Update button text for last question
    if (totalCount >= MAX_QUESTIONS) {
        document.getElementById('next-btn').textContent = 'See Results';
    }
}

// Get random correct message
function getCorrectMessage() {
    const messages = [
        'Correct! 🎉',
        'Great job! ⭐',
        'Parfait! 🌟',
        'Excellent! 👏',
        'Bien fait! 🎊',
        'Amazing! 💫'
    ];
    return messages[Math.floor(Math.random() * messages.length)];
}

// Get random incorrect message
function getIncorrectMessage() {
    const messages = [
        'Not quite! 🤔',
        'Try to remember! 📚',
        'Keep learning! 💪',
        'Almost! 🎯',
        'Next time! 👍'
    ];
    return messages[Math.floor(Math.random() * messages.length)];
}

// Show quiz complete screen
function showQuizComplete() {
    document.getElementById('quiz-area').style.display = 'none';
    document.querySelector('.quiz-footer').style.display = 'none';

    document.getElementById('final-correct').textContent = correctCount;
    document.getElementById('final-total').textContent = totalCount;

    // Calculate score message
    const percentage = Math.round((correctCount / totalCount) * 100);
    let message = '';
    if (percentage === 100) {
        message = 'Perfect score! You\'re a French superstar! 🌟';
    } else if (percentage >= 80) {
        message = 'Excellent work! Keep it up! 🎉';
    } else if (percentage >= 60) {
        message = 'Good job! Practice makes perfect! 💪';
    } else if (percentage >= 40) {
        message = 'Nice effort! Keep studying! 📚';
    } else {
        message = 'Keep practicing, you\'ll get better! 🌱';
    }
    document.getElementById('score-message').textContent = message;

    document.getElementById('quiz-complete').style.display = 'block';

    // Trigger unicorn celebration for Family user with good score
    if (isFamily && percentage >= 70 && typeof triggerUnicorn === 'function') {
        setTimeout(() => triggerUnicorn(), 500);
    }
}

// Start a new quiz
function startNewQuiz() {
    correctCount = 0;
    totalCount = 0;
    currentQuestion = null;
    isAnswered = false;

    document.getElementById('score-correct').textContent = '0';
    document.getElementById('score-total').textContent = '0';

    document.getElementById('quiz-complete').style.display = 'none';
    document.getElementById('quiz-area').style.display = 'block';
    document.querySelector('.quiz-footer').style.display = 'block';
    document.getElementById('next-btn').textContent = 'Next Question →';

    loadNextQuestion();
}

// End quiz early
function endQuiz() {
    if (totalCount > 0) {
        showQuizComplete();
    } else {
        window.history.back();
    }
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Number keys 1-4 for options
    if (!isAnswered && e.key >= '1' && e.key <= '4') {
        selectOption(parseInt(e.key) - 1);
    }

    // Enter or Space to continue
    if (isAnswered && (e.code === 'Enter' || e.code === 'Space')) {
        e.preventDefault();
        loadNextQuestion();
    }
});
