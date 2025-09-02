const API_BASE_URL = 'https://mindvibe-ai.onrender.com';
let moodChart = null;
let moodHistory = [];

document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
    loadMoodHistory();
    initializeMoodChart();
    updateStats();
});

function setupEventListeners() {
    const moodTextArea = document.getElementById('mood-text');
    const analyzeBtn = document.getElementById('analyze-btn');
    const charCount = document.getElementById('char-count');

    if (moodTextArea) {
        moodTextArea.addEventListener('input', function() {
            const count = this.value.length;
            charCount.textContent = count;
            
            if (count > 500) {
                charCount.style.color = '#ff4757';
            } else {
                charCount.style.color = '#666';
            }
        });
    }

    if (analyzeBtn) {
        analyzeBtn.addEventListener('click', analyzeMood);
    }
    
    if (moodTextArea) {
        moodTextArea.addEventListener('keypress', function(e) {
            if (e.key === 'Enter' && e.ctrlKey) {
                analyzeMood();
            }
        });
    }
}

async function analyzeMood() {
    const moodTextArea = document.getElementById('mood-text');
    const analyzeBtn = document.getElementById('analyze-btn');
    const text = moodTextArea.value.trim();
    
    if (!text) {
        alert('Please enter some text to analyze your mood.');
        return;
    }

    if (text.length > 500) {
        alert('Please keep your text under 500 characters.');
        return;
    }

    // Enhanced loading state with animation
    analyzeBtn.innerHTML = 'Analyzing<span class="loading-spinner"></span>';
    analyzeBtn.disabled = true;
    analyzeBtn.classList.add('analyzing');

    try {
        const response = await fetch(API_BASE_URL + '/analyze-mood', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text })
        });

        if (!response.ok) {
            throw new Error('HTTP error! status: ' + response.status);
        }

        const result = await response.json();
        
        // Add slight delay for dramatic effect
        setTimeout(() => {
            displayMoodResult(result);
            moodHistory.unshift(result);
            updateMoodChart();
            updateMoodHistory();
            updateStats();
            
            moodTextArea.value = '';
            document.getElementById('char-count').textContent = '0';
        }, 800);
        
    } catch (error) {
        console.error('Error analyzing mood:', error);
        alert('Error analyzing mood. Please make sure your backend is running on https://mindvibe-ai.onrender.com');
    } finally {
        setTimeout(() => {
            analyzeBtn.innerHTML = 'Analyze My Mood 🧠';
            analyzeBtn.disabled = false;
            analyzeBtn.classList.remove('analyzing');
        }, 800);
    }
}

function displayMoodResult(result) {
    const resultsSection = document.getElementById('results-section');
    resultsSection.style.display = 'block';
    resultsSection.scrollIntoView({ behavior: 'smooth' });

    // Animate mood score counting up
    animateCounter(0, result.mood_score, 'mood-score', 1500);
    
    document.getElementById('mood-category').textContent = result.mood_category;
    
    const scoreCircle = document.querySelector('.score-circle');
    if (scoreCircle) {
        setTimeout(() => {
            scoreCircle.style.background = 'conic-gradient(' + result.color + ' 0deg ' + (result.mood_score * 3.6) + 'deg, #e9ecef ' + (result.mood_score * 3.6) + 'deg 360deg)';
        }, 500);
    }

    document.getElementById('sentiment-value').textContent = (result.polarity > 0 ? 'Positive' : result.polarity < 0 ? 'Negative' : 'Neutral') + ' (' + result.polarity + ')';
    document.getElementById('confidence-value').textContent = Math.round(result.subjectivity * 100) + '%';

    // Animate recommendations appearing one by one
    const recommendationsList = document.getElementById('recommendations-list');
    recommendationsList.innerHTML = '';
    result.recommendations.forEach(function(rec, index) {
        setTimeout(() => {
            const div = document.createElement('div');
            div.className = 'recommendation-item';
            div.innerHTML = '<span class="rec-icon">💡</span> ' + rec;
            recommendationsList.appendChild(div);
        }, (index + 1) * 300);
    });
}

// Counter animation function
function animateCounter(start, end, elementId, duration) {
    const element = document.getElementById(elementId);
    if (!element) return;
    
    const range = end - start;
    const increment = Math.ceil(range / (duration / 50));
    let current = start;
    
    const timer = setInterval(function() {
        current += increment;
        if (current >= end) {
            current = end;
            clearInterval(timer);
        }
        element.textContent = current;
    }, 50);
}

function initializeMoodChart() {
    const canvas = document.getElementById('mood-chart');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    
    moodChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Mood Score',
                data: [],
                borderColor: '#667eea',
                backgroundColor: 'rgba(102, 126, 234, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.4,
                pointBackgroundColor: '#667eea',
                pointBorderColor: '#ffffff',
                pointBorderWidth: 2,
                pointRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    grid: {
                        color: 'rgba(0,0,0,0.1)'
                    }
                },
                x: {
                    grid: {
                        color: 'rgba(0,0,0,0.1)'
                    }
                }
            },
            plugins: {
                legend: {
                    display: true,
                    labels: {
                        color: '#333'
                    }
                }
            },
            animation: {
                duration: 2000,
                easing: 'easeInOutQuart'
            }
        }
    });
}

function updateMoodChart() {
    if (!moodChart) return;

    const last10Entries = moodHistory.slice(0, 10).reverse();
    const labels = last10Entries.map(function(entry, index) {
        const date = new Date(entry.timestamp);
        return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    });
    const scores = last10Entries.map(function(entry) {
        return entry.mood_score;
    });

    moodChart.data.labels = labels;
    moodChart.data.datasets[0].data = scores;
    moodChart.update();
}

function updateMoodHistory() {
    const historyContainer = document.getElementById('mood-history');
    
    if (moodHistory.length === 0) {
        historyContainer.innerHTML = '<p class="empty-state">Start tracking to see your mood history here!</p>';
        return;
    }

    historyContainer.innerHTML = '';
    
    moodHistory.slice(0, 5).forEach(function(entry, index) {
        setTimeout(() => {
            const historyItem = document.createElement('div');
            historyItem.className = 'mood-history-item';
            
            const date = new Date(entry.timestamp);
            const timeStr = date.toLocaleString();
            
            historyItem.innerHTML = '<div class="history-header">' +
                '<span class="history-score" style="color: ' + entry.color + '">' + entry.mood_score + '%</span>' +
                '<span class="history-category">' + entry.mood_category + '</span>' +
                '<span class="history-time">' + timeStr + '</span>' +
                '</div>' +
                '<div class="history-text">' + entry.text + '</div>';
            
            historyContainer.appendChild(historyItem);
        }, index * 200);
    });
}

function loadMoodHistory() {
    // For demo purposes, start with empty history
}

function updateStats() {
    if (moodHistory.length > 0) {
        const scores = moodHistory.map(function(entry) {
            return entry.mood_score;
        });
        const avgMood = Math.round(scores.reduce(function(a, b) {
            return a + b;
        }, 0) / scores.length);
        
        // Animate stats updates
        animateCounter(parseInt(document.getElementById('total-entries').textContent) || 0, moodHistory.length, 'total-entries', 1000);
        animateCounter(parseInt(document.getElementById('avg-mood').textContent) || 0, avgMood, 'avg-mood', 1200);
        
        document.getElementById('mood-trend').textContent = scores.length >= 2 && scores[0] > scores[1] ? 'improving' : 'stable';
    }
}
let currentStep = 0;
let answers = {};

const questions = [
    { emoji: "🤝", text: "How would you like MindVibe to address you?", type: "text", key: "name", placeholder: "Enter your preferred name" },
    { emoji: "⚧️", text: "How do you identify your gender?", type: "single", key: "gender", options: [
        { text: "Male", value: "male" },
        { text: "Female", value: "female" },
        { text: "Non-binary", value: "nonbinary" }
    ]},
    { emoji: "🎂", text: "What's your age?", type: "single", key: "age", options: [
        { text: "18-24", value: "18-24" },
        { text: "25-34", value: "25-34" },
        { text: "35-44", value: "35-44" },
        { text: "45-54", value: "45-54" },
        { text: "55+", value: "55+" }
    ]},
    { emoji: "🌟", text: "Complete setup!", type: "completion", key: "completion" }
];

function renderQuestion() {
    const question = questions[currentStep];
    const container = document.getElementById('questionContainer');
    const progressFill = document.getElementById('progressFill');
    
    let progress = ((currentStep + 1)/questions.length)*100;
    progressFill.style.width = progress + '%';

    if (question.type === 'completion') {
        container.innerHTML = `<div class="completion-screen">
            <div class="completion-icon">🎉</div>
            <div class="completion-title">All Done!</div>
            <div class="completion-text">You're ready to start your MindVibe journey.</div>
            <button onclick="finishOnboarding()">Go to Dashboard</button>
        </div>`;
        return;
    }

    if(question.type === 'text') {
        container.innerHTML = `<div class="question-header">
            <div class="question-emoji">${question.emoji}</div>
            <div class="question-text">${question.text}</div>
        </div>
        <textarea id="textInput" class="text-input" placeholder="${question.placeholder}">${answers[question.key]||''}</textarea>`;
        document.getElementById('textInput').addEventListener('input', () => {
            answers[question.key] = document.getElementById('textInput').value;
            updateNavigationState();
        });
    } else if(question.type === 'single') {
        container.innerHTML = `<div class="question-header">
            <div class="question-emoji">${question.emoji}</div>
            <div class="question-text">${question.text}</div>
        </div>
        <div class="options-container">
            ${question.options.map((opt,i) => `<div class="option ${answers[question.key]===opt.value?'selected':''}" onclick="selectOption('${question.key}','${opt.value}',${i})">${opt.text}</div>`).join('')}
        </div>`;
    }

    updateNavigationState();
}

function selectOption(key,value,index) {
    answers[key] = value;
    document.querySelectorAll('.option').forEach((opt,i)=>opt.classList.toggle('selected', i===index));
    updateNavigationState();
}

function nextQuestion() {
    if(currentStep<questions.length-1) { currentStep++; renderQuestion(); }
}

function previousQuestion() {
    if(currentStep>0) { currentStep--; renderQuestion(); }
}

function updateNavigationState() {
    const continueBtn = document.getElementById('continueBtn');
    const backBtn = document.getElementById('backBtn');
    const q = questions[currentStep];
    
    backBtn.disabled = currentStep===0;
    if(q.type==='text') continueBtn.disabled = !answers[q.key];
    else continueBtn.disabled = !answers[q.key];
}

function finishOnboarding() {
    // Here you can send answers to backend before redirect
    console.log('User Answers:', answers);
    window.location.href = 'dashboard.html';
}

document.getElementById('continueBtn').addEventListener('click', nextQuestion);
document.getElementById('backBtn').addEventListener('click', previousQuestion);
renderQuestion();
