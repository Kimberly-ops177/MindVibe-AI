import smtplib
from email.mime.text import MimeText
from email.mime.multipart import MimeMultipart
from datetime import datetime

@app.route('/send-confirmation-email', methods=['POST'])
def send_confirmation_email():
    try:
        data = request.get_json()
        
        # Email configuration (use environment variables)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "noreply@mindvibe-ai.help" 
        sender_password = "Prince@07" 
        
        # Email content
        html_content = f"""
        <html>
        <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            <div style="background: linear-gradient(135deg, #78dbff, #ff77c6); padding: 20px; text-align: center;">
                <h1 style="color: white; margin: 0;">🧠 MindVibe AI</h1>
                <h2 style="color: white; margin: 10px 0;">Payment Confirmation</h2>
            </div>
            
            <div style="padding: 30px; background: #f9f9f9;">
                <h3>Hi {data.get('name', 'there')},</h3>
                <p>Thank you for upgrading to MindVibe AI Premium! Your payment has been processed successfully.</p>
                
                <div style="background: white; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <h4>Transaction Details</h4>
                    <p><strong>Reference:</strong> {data.get('reference')}</p>
                    <p><strong>Amount:</strong> {data.get('amount')}</p>
                    <p><strong>Date:</strong> {datetime.now().strftime('%d %b, %Y')}</p>
                    <p><strong>Payment Method:</strong> {data.get('method')}</p>
                </div>
                
                <p>Your premium features are now active! If you have any issues, reply to this email or contact support@mindvibe-ai.help</p>
                
                <div style="text-align: center; margin: 30px 0;">
                    <a href="https://your-app-url.com/dashboard.html" 
                       style="background: linear-gradient(135deg, #78dbff, #ff77c6); 
                              color: white; padding: 12px 30px; text-decoration: none; 
                              border-radius: 25px; display: inline-block;">
                        Go to Dashboard
                    </a>
                </div>
            </div>
            
            <div style="text-align: center; padding: 20px; color: #666; font-size: 12px;">
                <p>© 2025 MindVibe AI. Built with care for mental wellness.</p>
                <p>This receipt is for your subscription. If you have questions, contact us at support@mindvibe-ai.help</p>
            </div>
        </body>
        </html>
        """
        
        # Send email
        msg = MimeMultipart('alternative')
        msg['Subject'] = f"Payment Confirmation - MindVibe AI Premium"
        msg['From'] = sender_email
        msg['To'] = data.get('email')
        
        html_part = MimeText(html_content, 'html')
        msg.attach(html_part)
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        
        return jsonify({'success': True, 'message': 'Confirmation email sent'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import sqlite3
from datetime import datetime, timedelta
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Hugging Face API configuration
HUGGING_FACE_API_TOKEN = "hf_qcZLjqECToXfFpqyMfIgpVrXQDnntiKoNxp"
HUGGING_FACE_HEADERS = {"Authorization": f"Bearer {HUGGING_FACE_API_TOKEN}"}

# API endpoints for different models (updated working URLs)
SENTIMENT_API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
EMOTION_API_URL = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('mindvibe.db')
    cursor = conn.cursor()

    # Enhanced mood_entries table (preserving your existing structure + new fields)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mood_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER DEFAULT 1,
            text TEXT NOT NULL,
            mood_score INTEGER NOT NULL,
            mood_category TEXT NOT NULL,
            sentiment_label TEXT NOT NULL,
            sentiment_score REAL NOT NULL,
            emotions TEXT NOT NULL,
            color TEXT NOT NULL,
            recommendations TEXT NOT NULL,
            crisis_level INTEGER DEFAULT 0,
            personalization_used TEXT DEFAULT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Enhanced users table (preserving your existing structure + new fields)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE DEFAULT NULL,
            name TEXT,
            gender TEXT,
            age TEXT,
            self_knowledge TEXT,
            bottling_feelings TEXT,
            overthinking TEXT,
            anxiety_moments TEXT,
            referred_by_professional TEXT,
            support_areas TEXT,
            preferred_coping_strategies TEXT DEFAULT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # New table for user feedback and learning (optional feature)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_preferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER DEFAULT 1,
            recommendation_type TEXT,
            effectiveness_rating INTEGER,
            used_suggestion BOOLEAN DEFAULT FALSE,
            feedback_text TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    conn.commit()
    conn.close()

def get_user_profile(user_id=1):
    """Get user's onboarding profile for personalization (new feature)"""
    conn = sqlite3.connect('mindvibe.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT name, gender, age, self_knowledge, bottling_feelings, 
               overthinking, anxiety_moments, referred_by_professional, support_areas
        FROM users WHERE id = ?
    ''', (user_id,))
    
    profile_data = cursor.fetchone()
    if not profile_data:
        conn.close()
        return None
    
    profile = {
        'name': profile_data[0],
        'gender': profile_data[1],
        'age': profile_data[2],
        'self_knowledge': profile_data[3],
        'bottling_feelings': profile_data[4],
        'overthinking': profile_data[5],
        'anxiety_moments': profile_data[6],
        'referred_by_professional': profile_data[7],
        'support_areas': json.loads(profile_data[8]) if profile_data[8] else []
    }
    
    conn.close()
    return profile

def query_huggingface_api(api_url, payload):
    """
    Query Hugging Face API with retry logic (preserved from your original)
    """
    try:
        response = requests.post(api_url, headers=HUGGING_FACE_HEADERS, json=payload)

        if response.status_code == 503:
            # Model is loading, wait and retry once
            import time
            time.sleep(2)
            response = requests.post(api_url, headers=HUGGING_FACE_HEADERS, json=payload)

        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Hugging Face API error: {e}")
        return None

def fallback_analysis(text):
    """
    Enhanced fallback analysis (improved from your original)
    """
    text_lower = text.lower()

    # Enhanced keyword dictionaries (expanded from your original)
    positive_words = ['happy', 'excited', 'joyful', 'great', 'amazing', 'wonderful', 'love',
                      'grateful', 'blessed', 'fantastic', 'awesome', 'excellent', 'perfect', 'brilliant',
                      'content', 'peaceful', 'optimistic', 'hopeful']
    negative_words = ['sad', 'depressed', 'angry', 'frustrated', 'anxious', 'worried',
                      'terrible', 'awful', 'horrible', 'hate', 'stressed', 'overwhelmed', 'upset', 
                      'disappointed', 'hopeless', 'worthless', 'lonely', 'scared']
    neutral_words = ['okay', 'fine', 'normal', 'regular', 'usual', 'average']

    # Count matches
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    neutral_count = sum(1 for word in neutral_words if word in text_lower)

    # Determine sentiment (preserved logic)
    if positive_count > negative_count:
        sentiment_label = "POSITIVE"
        sentiment_score = min(0.9, 0.6 + (positive_count * 0.1))
    elif negative_count > positive_count:
        sentiment_label = "NEGATIVE"
        sentiment_score = min(0.9, 0.6 + (negative_count * 0.1))
    else:
        sentiment_label = "NEUTRAL"
        sentiment_score = 0.5

    # Enhanced emotion detection (improved from your original)
    emotions = []
    if 'happy' in text_lower or 'joy' in text_lower or 'excited' in text_lower:
        emotions.append({'label': 'joy', 'score': 0.8})
    if any(word in text_lower for word in ['sad', 'crying', 'depressed', 'lonely']):
        emotions.append({'label': 'sadness', 'score': 0.8})
    if any(word in text_lower for word in ['angry', 'mad', 'frustrated', 'annoyed']):
        emotions.append({'label': 'anger', 'score': 0.7})
    if any(word in text_lower for word in ['scared', 'afraid', 'anxious', 'worried', 'nervous']):
        emotions.append({'label': 'fear', 'score': 0.7})

    return sentiment_label, sentiment_score, emotions

def generate_personalized_recommendations(mood_score, sentiment_label, emotions, text, user_profile=None):
    """
    NEW: Enhanced recommendation engine that uses onboarding data
    """
    recommendations = []
    personalization_used = []
    
    # Get primary emotion
    primary_emotion = emotions[0]['label'].lower() if emotions else 'neutral'
    text_lower = text.lower()
    
    # Crisis-level recommendations (always take priority)
    if mood_score < 25:
        recommendations.extend([
            "Please reach out to a mental health professional immediately",
            "Contact a crisis hotline: 988 (US) or your local emergency services",
            "Talk to a trusted friend, family member, or counselor right away",
            "Remember: You matter, and help is available"
        ])
        return recommendations, ["crisis_intervention"]
    
    # NEW: Use onboarding data for personalization
    if user_profile:
        name = user_profile.get('name', '')
        support_areas = user_profile.get('support_areas', [])
        
        # Personalized greeting for difficult moments
        if mood_score < 50 and name:
            recommendations.append(f"Hi {name}, I notice you're having a challenging moment. Let's work through this together.")
            personalization_used.append("personalized_greeting")
        
        # Address specific support areas from onboarding
        if 'anxiety_worry' in support_areas and (primary_emotion in ['fear', 'anxiety'] or 'anxious' in text_lower):
            if user_profile.get('anxiety_moments') == 'yes':
                recommendations.extend([
                    "Since anxiety is something you've identified as a challenge, try the 4-7-8 breathing technique",
                    "Practice progressive muscle relaxation starting with your shoulders"
                ])
                personalization_used.append("anxiety_support_area")
        
        if 'stress_emotions' in support_areas and mood_score < 60:
            recommendations.append("You mentioned wanting support with stress management. Take 5 minutes for yourself right now")
            personalization_used.append("stress_management")
        
        if 'relationships' in support_areas and ('lonely' in text_lower or 'alone' in text_lower):
            recommendations.append("Consider reaching out to someone who makes you feel understood")
            personalization_used.append("relationship_support")
        
        # Address overthinking pattern
        if user_profile.get('overthinking') == 'yes' and ('think' in text_lower or 'mind' in text_lower):
            recommendations.append("I see you might be caught in overthinking again. Try the 'STOP' technique")
            personalization_used.append("overthinking_pattern")
    
    # Your original emotion-specific recommendations (preserved)
    if primary_emotion == 'sadness':
        recommendations.extend([
            "Practice self-compassion - be kind to yourself during difficult times",
            "Try gentle movement like a short walk or stretching",
            "Consider reaching out to someone you trust"
        ])
    elif primary_emotion == 'anger':
        recommendations.extend([
            "Take 10 deep breaths to help regulate your nervous system",
            "Try progressive muscle relaxation to release physical tension",
            "Channel this energy into physical exercise if possible"
        ])
    elif primary_emotion in ['fear', 'anxiety']:
        recommendations.extend([
            "Practice the 5-4-3-2-1 grounding technique (5 things you see, 4 you hear, etc.)",
            "Try box breathing: 4 counts in, hold 4, out 4, hold 4",
            "Remind yourself that this feeling is temporary and will pass"
        ])
    elif primary_emotion == 'joy':
        recommendations.extend([
            "Savor this positive moment through mindful awareness",
            "Share your joy with someone you care about",
            "Use this positive energy to work toward a meaningful goal"
        ])

    # Your original mood score-based recommendations (preserved)
    if mood_score < 50:
        recommendations.extend([
            "Focus on basic self-care: proper sleep, nutrition, and hydration",
            "Break large tasks into smaller, manageable steps",
            "Practice one act of self-kindness today"
        ])
    elif mood_score > 70:
        recommendations.extend([
            "Use this positive momentum to tackle something you've been postponing",
            "Practice gratitude by writing down what's going well",
            "Consider helping someone else to amplify positive feelings"
        ])

    # Your original context-specific recommendations (preserved)
    if 'work' in text_lower or 'job' in text_lower:
        recommendations.append("Set clear boundaries between work and personal time")
        personalization_used.append("work_context")
    if 'sleep' in text_lower or 'tired' in text_lower:
        recommendations.append("Prioritize getting 7-9 hours of quality sleep")
        personalization_used.append("sleep_context")
    if 'relationship' in text_lower:
        recommendations.append("Practice open, honest communication with loved ones")
        personalization_used.append("relationship_context")

    return recommendations[:4], personalization_used

def analyze_mood_with_ai(text, user_id=1):
    """
    Enhanced mood analysis (preserving your original logic + adding personalization)
    """
    # Get user profile for personalization (NEW)
    user_profile = get_user_profile(user_id)
    
    # Try Hugging Face API first (preserved from your original)
    sentiment_payload = {"inputs": text}
    sentiment_result = query_huggingface_api(SENTIMENT_API_URL, sentiment_payload)

    emotion_payload = {"inputs": text}
    emotion_result = query_huggingface_api(EMOTION_API_URL, emotion_payload)

    # Use AI results if available, otherwise fallback (preserved logic)
    if sentiment_result and isinstance(sentiment_result, list) and len(sentiment_result) > 0:
        top_sentiment = max(sentiment_result[0], key=lambda x: x['score'])
        sentiment_label = top_sentiment['label']
        sentiment_score = top_sentiment['score']

        emotions = []
        if emotion_result and isinstance(emotion_result, list) and len(emotion_result) > 0:
            emotions = sorted(emotion_result[0], key=lambda x: x['score'], reverse=True)

        print(f"✅ Using Hugging Face AI analysis")
    else:
        print(f"⚠️ Hugging Face API unavailable, using enhanced fallback analysis")
        sentiment_label, sentiment_score, emotions = fallback_analysis(text)

    # Calculate mood score (preserved your original function)
    mood_score = calculate_mood_score(sentiment_label, sentiment_score, emotions, text)

    # Determine mood category and color (preserved)
    category, color = get_mood_category_and_color(mood_score)

    # Check for crisis indicators (preserved)
    crisis_level = detect_crisis_level(text, emotions)

    # Generate personalized recommendations (NEW: enhanced version)
    recommendations, personalization_used = generate_personalized_recommendations(
        mood_score, sentiment_label, emotions, text, user_profile
    )

    return {
        'mood_score': mood_score,
        'mood_category': category,
        'sentiment_label': sentiment_label,
        'sentiment_score': round(sentiment_score, 3),
        'emotions': emotions[:5] if emotions else [],
        'color': color,
        'recommendations': recommendations,
        'crisis_level': crisis_level,
        'personalization_used': personalization_used,  # NEW
        'user_name': user_profile.get('name', '') if user_profile else '',  # NEW
        'timestamp': datetime.now().isoformat()
    }

# Preserved all your original functions exactly as they were
def calculate_mood_score(sentiment_label, sentiment_score, emotions, text):
    """
    Calculate mood score (0-100) based on AI analysis (PRESERVED from your original)
    """
    base_score = 50  # Neutral baseline

    # Adjust based on sentiment
    if sentiment_label == "LABEL_2" or sentiment_label == "POSITIVE":
        base_score = 50 + (sentiment_score * 50)
    elif sentiment_label == "LABEL_0" or sentiment_label == "NEGATIVE":
        base_score = 50 - (sentiment_score * 50)

    # Adjust based on emotions
    if emotions:
        emotion_adjustment = 0
        for emotion in emotions[:3]:  # Consider top 3 emotions
            emotion_name = emotion['label'].lower()
            emotion_score = emotion['score']

            if emotion_name in ['joy', 'happiness', 'love', 'optimism']:
                emotion_adjustment += emotion_score * 20
            elif emotion_name in ['sadness', 'anger', 'fear', 'disgust']:
                emotion_adjustment -= emotion_score * 20
            elif emotion_name in ['surprise']:
                emotion_adjustment += emotion_score * 5

        base_score += emotion_adjustment

    # Text-based keyword adjustments for more accuracy
    text_lower = text.lower()
    critical_keywords = ['suicide', 'kill myself', 'end it all', 'no point', 'worthless']
    positive_keywords = ['excited', 'happy', 'grateful', 'amazing', 'wonderful', 'love']

    if any(keyword in text_lower for keyword in critical_keywords):
        base_score = min(base_score, 15)  # Cap at very low score
    elif any(keyword in text_lower for keyword in positive_keywords):
        base_score = max(base_score, 70)  # Boost positive expressions

    return max(0, min(100, int(base_score)))

def get_mood_category_and_color(mood_score):
    """
    Determine mood category and color based on score (PRESERVED from your original)
    """
    if mood_score >= 85:
        return "Excellent", "#10b981"  # Emerald green
    elif mood_score >= 70:
        return "Very Good", "#22d3ee"  # Cyan
    elif mood_score >= 55:
        return "Good", "#3b82f6"  # Blue
    elif mood_score >= 40:
        return "Fair", "#f59e0b"  # Amber
    elif mood_score >= 25:
        return "Poor", "#f97316"  # Orange
    else:
        return "Critical", "#ef4444"  # Red

def detect_crisis_level(text, emotions):
    """
    Detect potential mental health crisis indicators (PRESERVED from your original)
    """
    crisis_level = 0
    text_lower = text.lower()

    # Critical phrases (level 3 - immediate concern)
    critical_phrases = [
        'kill myself', 'suicide', 'end it all', 'want to die',
        'no point living', 'everyone better without me'
    ]

    # Severe indicators (level 2 - high concern)
    severe_indicators = [
        'can\'t go on', 'hopeless', 'worthless', 'nothing matters',
        'giving up', 'can\'t take it', 'too much pain'
    ]

    # Moderate concern indicators (level 1)
    moderate_indicators = [
        'very depressed', 'extremely sad', 'completely alone',
        'no one understands', 'everything is wrong'
    ]

    if any(phrase in text_lower for phrase in critical_phrases):
        crisis_level = 3
    elif any(indicator in text_lower for indicator in severe_indicators):
        crisis_level = 2
    elif any(indicator in text_lower for indicator in moderate_indicators):
        crisis_level = 1

    # Check emotions for additional crisis indicators
    if emotions:
        sadness_score = next((e['score'] for e in emotions if e['label'].lower() == 'sadness'), 0)
        fear_score = next((e['score'] for e in emotions if e['label'].lower() == 'fear'), 0)

        if sadness_score > 0.8 or fear_score > 0.7:
            crisis_level = max(crisis_level, 2)

    return crisis_level

# Your original generate_ai_recommendations function is replaced by generate_personalized_recommendations above

@app.route('/analyze-mood', methods=['POST'])
def analyze_mood():
    """
    Enhanced mood analysis endpoint (PRESERVED your original logic + personalization)
    """
    try:
        data = request.get_json()

        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400

        text = data['text'].strip()
        user_id = data.get('user_id', 1)  # NEW: support for user_id

        if len(text) < 5:
            return jsonify({'error': 'Text too short for analysis'}), 400

        # Perform AI-powered mood analysis with personalization
        analysis_result = analyze_mood_with_ai(text, user_id)

        # Save to database (enhanced to include personalization data)
        conn = sqlite3.connect('mindvibe.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO mood_entries 
            (user_id, text, mood_score, mood_category, sentiment_label, sentiment_score, 
             emotions, color, recommendations, crisis_level, personalization_used)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            user_id,
            text,
            analysis_result['mood_score'],
            analysis_result['mood_category'],
            analysis_result['sentiment_label'],
            analysis_result['sentiment_score'],
            json.dumps(analysis_result['emotions']),
            analysis_result['color'],
            json.dumps(analysis_result['recommendations']),
            analysis_result['crisis_level'],
            json.dumps(analysis_result['personalization_used'])
        ))

        conn.commit()
        conn.close()

        # Add polarity and subjectivity for frontend compatibility (preserved)
        analysis_result['polarity'] = 1.0 if analysis_result['sentiment_label'] in [
            'POSITIVE', 'LABEL_2'] else -1.0 if analysis_result['sentiment_label'] in ['NEGATIVE', 'LABEL_0'] else 0.0
        analysis_result['subjectivity'] = analysis_result['sentiment_score']

        return jsonify(analysis_result)

    except Exception as e:
        print(f"Error in analyze_mood: {e}")
        return jsonify({'error': 'Analysis failed. Please try again.'}), 500

# All your other endpoints preserved exactly as they were
@app.route('/mood-history', methods=['GET'])
def get_mood_history():
    """
    Get mood history with enhanced data (PRESERVED from your original)
    """
    try:
        conn = sqlite3.connect('mindvibe.db')
        cursor = conn.cursor()

        # Get recent entries
        cursor.execute('''
            SELECT mood_score, mood_category, timestamp, recommendations, 
                   color, sentiment_label, emotions, crisis_level
            FROM mood_entries
            ORDER BY timestamp DESC
            LIMIT 30
        ''')

        entries = []
        crisis_alerts = 0

        for row in cursor.fetchall():
            entry = {
                'mood_score': row[0],
                'mood_category': row[1],
                'timestamp': row[2],
                'recommendations': json.loads(row[3]),
                'color': row[4],
                'sentiment_label': row[5],
                'emotions': json.loads(row[6]) if row[6] else [],
                'crisis_level': row[7]
            }
            entries.append(entry)

            if entry['crisis_level'] >= 2:
                crisis_alerts += 1

        conn.close()

        # Calculate enhanced statistics
        if entries:
            scores = [entry['mood_score'] for entry in entries]
            recent_scores = scores[:7]  # Last week

            stats = {
                'total_entries': len(entries),
                'average_mood': round(sum(scores) / len(scores), 1),
                'trend': 'Rising' if len(recent_scores) >= 2 and recent_scores[0] > recent_scores[-1] else 'Stable',
                'crisis_alerts': crisis_alerts,
                'weekly_average': round(sum(recent_scores) / len(recent_scores), 1) if recent_scores else 0
            }
        else:
            stats = {
                'total_entries': 0,
                'average_mood': 0,
                'trend': 'No Data',
                'crisis_alerts': 0,
                'weekly_average': 0
            }

        return jsonify({
            'entries': entries,
            'stats': stats
        })

    except Exception as e:
        print(f"Error in mood_history: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/save-onboarding', methods=['POST'])
def save_onboarding():
    """
    Save onboarding data from the assessment (PRESERVED + enhanced)
    """
    try:
        data = request.get_json()

        conn = sqlite3.connect('mindvibe.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO users 
            (email, name, gender, age, self_knowledge, bottling_feelings, overthinking, 
             anxiety_moments, referred_by_professional, support_areas)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data.get('email', ''),
            data.get('name', ''),
            data.get('gender', ''),
            data.get('age', ''),
            data.get('self_knowledge', ''),
            data.get('bottling_feelings', ''),
            data.get('overthinking', ''),
            data.get('anxiety_moments', ''),
            data.get('referred_by_professional', ''),
            json.dumps(data.get('support_areas', []))
        ))

        user_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return jsonify({
            'success': True, 
            'message': 'Onboarding data saved successfully',
            'user_id': user_id  # NEW: return user_id for frontend use
        })

    except Exception as e:
        print(f"Error in save_onboarding: {e}")
        return jsonify({'error': str(e)}), 500

# NEW: Optional endpoint for user feedback
@app.route('/rate-recommendation', methods=['POST'])
def rate_recommendation():
    """
    NEW: Allow users to rate recommendation effectiveness (optional feature)
    """
    try:
        data = request.get_json()
        user_id = data.get('user_id', 1)
        recommendation_type = data.get('recommendation_type')
        rating = data.get('rating')  # 1-5 scale
        feedback = data.get('feedback', '')
        
        conn = sqlite3.connect('mindvibe.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO user_preferences 
            (user_id, recommendation_type, effectiveness_rating, feedback_text)
            VALUES (?, ?, ?, ?)
        ''', (user_id, recommendation_type, rating, feedback))
        
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'message': 'Feedback saved'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Enhanced health check with API status (PRESERVED + enhanced)
    """
    # Test Hugging Face API connection
    test_payload = {"inputs": "I am feeling good today"}
    api_status = query_huggingface_api(SENTIMENT_API_URL, test_payload)

    return jsonify({
        'status': 'healthy',
        'message': 'MindVibe AI Backend with Personalization is running',
        'ai_api_status': 'connected' if api_status else 'disconnected',
        'database_status': 'connected',
        'features': ['ai_analysis', 'crisis_detection', 'personalized_recommendations']  # NEW
    })

if __name__ == '__main__':
    # Initialize database on startup
    init_db()
    print("🧠 MindVibe AI Backend with Enhanced Personalization starting...")
    print("📊 Database initialized successfully")
    print("🤖 AI models: Sentiment Analysis + Emotion Recognition")
    print("🎯 Personalized recommendations engine active")
    print("🔗 API available at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
