// Unicorn Animation Script

// Sparkle emojis and colors
const SPARKLE_EMOJIS = ['✨', '💫', '⭐', '💖', '🌟', '💜', '💗'];
const SPARKLE_CLASSES = ['sparkle-pink', 'sparkle-purple', 'sparkle-gold', 'sparkle-blue'];
const DUST_CLASSES = ['dust-pink', 'dust-purple', 'dust-gold', 'dust-cyan'];

let unicornTimeout = null;

/**
 * Trigger the unicorn animation
 */
function triggerUnicorn() {
    // Don't stack animations
    if (document.querySelector('.unicorn-container')) {
        return;
    }

    // Create container
    const container = document.createElement('div');
    container.className = 'unicorn-container';
    document.body.appendChild(container);

    // Create unicorn
    const unicorn = document.createElement('div');
    unicorn.className = 'unicorn';
    unicorn.textContent = '🦄';
    container.appendChild(unicorn);

    // Add screen flash effect
    addScreenFlash();

    // Spawn sparkles along the path
    const sparkleInterval = setInterval(() => {
        const rect = unicorn.getBoundingClientRect();
        if (rect.left > window.innerWidth + 100) {
            clearInterval(sparkleInterval);
            return;
        }

        // Spawn sparkles at unicorn position
        for (let i = 0; i < 3; i++) {
            spawnSparkle(container, rect.left + 30, rect.top + rect.height / 2);
        }

        // Spawn magic dust
        for (let i = 0; i < 2; i++) {
            spawnMagicDust(container, rect.left + 50, rect.top + rect.height / 2);
        }
    }, 100);

    // Add floating hearts periodically
    const heartInterval = setInterval(() => {
        const rect = unicorn.getBoundingClientRect();
        if (rect.left > window.innerWidth + 100) {
            clearInterval(heartInterval);
            return;
        }
        spawnFloatingHeart(container, rect.left, rect.top);
    }, 400);

    // Clean up after animation
    unicornTimeout = setTimeout(() => {
        clearInterval(sparkleInterval);
        clearInterval(heartInterval);
        container.remove();
    }, 4000);
}

/**
 * Spawn a sparkle at given position
 */
function spawnSparkle(container, x, y) {
    const sparkle = document.createElement('div');
    sparkle.className = 'sparkle ' + SPARKLE_CLASSES[Math.floor(Math.random() * SPARKLE_CLASSES.length)];
    sparkle.textContent = SPARKLE_EMOJIS[Math.floor(Math.random() * SPARKLE_EMOJIS.length)];

    // Random offset from position
    const offsetX = (Math.random() - 0.5) * 100;
    const offsetY = (Math.random() - 0.5) * 80;

    sparkle.style.left = (x + offsetX) + 'px';
    sparkle.style.top = (y + offsetY) + 'px';
    sparkle.style.fontSize = (16 + Math.random() * 16) + 'px';

    container.appendChild(sparkle);

    // Remove after animation
    setTimeout(() => sparkle.remove(), 1000);
}

/**
 * Spawn magic dust particle
 */
function spawnMagicDust(container, x, y) {
    const dust = document.createElement('div');
    dust.className = 'magic-dust ' + DUST_CLASSES[Math.floor(Math.random() * DUST_CLASSES.length)];

    // Random offset
    const offsetX = (Math.random() - 0.5) * 60;
    const offsetY = (Math.random() - 0.5) * 40;

    dust.style.left = (x + offsetX) + 'px';
    dust.style.top = (y + offsetY) + 'px';
    dust.style.width = (4 + Math.random() * 8) + 'px';
    dust.style.height = dust.style.width;

    container.appendChild(dust);

    setTimeout(() => dust.remove(), 1500);
}

/**
 * Spawn floating heart
 */
function spawnFloatingHeart(container, x, y) {
    const heart = document.createElement('div');
    heart.className = 'floating-heart';
    heart.textContent = ['💖', '💕', '💗', '💜', '🩷'][Math.floor(Math.random() * 5)];

    heart.style.left = (x + Math.random() * 50) + 'px';
    heart.style.top = (y - 20 + Math.random() * 40) + 'px';

    container.appendChild(heart);

    setTimeout(() => heart.remove(), 2000);
}

/**
 * Add a brief screen flash effect
 */
function addScreenFlash() {
    const flash = document.createElement('div');
    flash.className = 'screen-flash';
    document.body.appendChild(flash);

    setTimeout(() => flash.remove(), 500);
}

/**
 * Trigger a celebration burst (for correct answers)
 */
function triggerCelebrationBurst() {
    const burst = document.createElement('div');
    burst.className = 'celebration-burst';
    document.body.appendChild(burst);

    const emojis = ['🎉', '⭐', '✨', '💫', '🌟', '🎊', '💖'];
    const numParticles = 12;

    for (let i = 0; i < numParticles; i++) {
        const particle = document.createElement('div');
        particle.className = 'burst-particle';
        particle.textContent = emojis[Math.floor(Math.random() * emojis.length)];

        // Calculate direction
        const angle = (i / numParticles) * Math.PI * 2;
        const distance = 80 + Math.random() * 60;
        const tx = Math.cos(angle) * distance;
        const ty = Math.sin(angle) * distance;

        particle.style.setProperty('--tx', tx + 'px');
        particle.style.setProperty('--ty', ty + 'px');

        burst.appendChild(particle);
    }

    setTimeout(() => burst.remove(), 1000);
}

/**
 * Add glitter overlay effect
 */
function addGlitterOverlay() {
    const glitter = document.createElement('div');
    glitter.className = 'glitter-overlay';
    document.body.appendChild(glitter);

    setTimeout(() => glitter.remove(), 2000);
}

// Make functions globally available
window.triggerUnicorn = triggerUnicorn;
window.triggerCelebrationBurst = triggerCelebrationBurst;
window.addGlitterOverlay = addGlitterOverlay;
