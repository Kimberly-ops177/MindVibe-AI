# MindVibe AI - Prompt Engineering Guide

## VibeCoding Hackathon 2025

This document contains the strategic prompts used to guide AI development of MindVibe AI, a mental wellness tracking application with advanced sentiment analysis.

---

## 1. PROJECT CONCEPTUALIZATION

### Initial Vision Prompt

```
I need to create a comprehensive mental wellness application for a hackathon. The app should:
- Track user mood and mental state over time
- Use AI to analyze emotional patterns
- Provide personalized recommendations
- Include crisis detection for safety
- Have a modern, accessible interface

Help me design the complete architecture including frontend pages, backend API structure, and AI integration strategy.
```

### User Experience Design Prompt

```
Design a complete user journey for a mental wellness app called MindVibe AI. Include:
- Landing page that builds trust and explains value
- Onboarding assessment to understand user needs
- Dashboard for daily mood tracking and insights
- Pricing page for premium features

Focus on creating an empathetic, professional design that reduces stigma around mental health support.
```

---

## 2. FRONTEND DEVELOPMENT

### Landing Page Creation Prompt

```
Create a modern, professional landing page for MindVibe AI mental wellness app using HTML, CSS, and JavaScript. Requirements:
- Dark gradient background with glassmorphism effects
- Hero section explaining AI-powered mood tracking
- Features section highlighting key benefits
- Pricing tiers (free and premium)
- Modern animations and hover effects
- Mobile-responsive design
- Call-to-action buttons linking to dashboard and pricing

Use contemporary design trends with blue-to-pink gradient accents (#78dbff to #ff77c6).
```

### Dashboard Interface Prompt

```
Build a sophisticated dashboard interface for mood analysis with:
- Neural activity visualization with animated elements
- Text input area for mood description with character counter
- Voice input capability using Web Speech API
- Real-time AI analysis results display with mood scores
- Interactive charts showing mood trends over time
- Personalized recommendations panel
- Crisis detection alerts with appropriate styling
- Heatmap calendar showing mood patterns
- Sidebar with statistics and insights

Maintain consistent dark theme with blue-pink gradient accents and glassmorphism effects.
```

### Onboarding Assessment Prompt

```
Create a multi-step onboarding questionnaire for mental health assessment:
- Progressive form with 9-10 questions covering demographics, self-awareness, emotional patterns
- Visual progress bar and step indicators
- Dynamic question types: text input, single choice, multiple choice
- Smooth transitions between questions with validation
- Emotional intelligence in question phrasing
- Completion screen with testimonials and call-to-action
- Local storage for data persistence
- Responsive design matching main app theme

Questions should gather insights for personalized AI recommendations while being sensitive to mental health context.
```

### Pricing Page Integration Prompt

```
Design a pricing page that seamlessly integrates with the existing design system:
- Match the sophisticated gradient background and glassmorphism effects
- Present clear value proposition for premium features
- Include multiple payment methods (M-Pesa, cards, bank transfer) for accessibility
- Form validation and user feedback
- Professional pricing presentation with feature comparisons
- Smooth integration with existing navigation and user flow

Ensure the payment flow feels secure and trustworthy for mental health service pricing.
```

---

## 3. BACKEND DEVELOPMENT

### Flask API Architecture Prompt

```
Create a comprehensive Flask backend for mental wellness tracking with:
- RESTful API endpoints for mood analysis, history, and user data
- SQLite database schema for mood entries and user profiles
- CORS configuration for frontend integration
- Error handling and input validation
- Health check endpoints for monitoring
- Structured logging for debugging

Design the API to be scalable and maintainable with clear separation of concerns.
```

### AI Integration Strategy Prompt

```
Implement advanced mood analysis using multiple AI approaches:
- Primary: Hugging Face Transformers API for sentiment and emotion analysis
- Fallback: Local keyword-based analysis for reliability
- Crisis detection algorithms for safety
- Personalized recommendation engine based on user patterns
- Confidence scoring and validation

Create a robust system that works reliably regardless of external API availability, ensuring mental health users always receive support.
```

### Database Design Prompt

```
Design a SQLite database schema for mental wellness tracking:
- Users table for onboarding assessment data
- Mood_entries table with comprehensive analysis fields
- Proper indexing for performance
- Data validation and constraints
- Migration-ready structure
- Privacy considerations for sensitive mental health data

Ensure the schema supports both current features and future enhancements.
```

---

## 4. AI MODEL INTEGRATION

### Hugging Face API Integration Prompt

```
Integrate Hugging Face Inference API for advanced sentiment analysis:
- Use cardiffnlp/twitter-roberta-base-sentiment-latest for sentiment
- Implement SamLowe/roberta-base-go_emotions for emotion detection
- Handle API authentication with secure token management
- Implement retry logic and error handling
- Parse and normalize model outputs for consistent application use
- Rate limiting and response caching strategies

Create a production-ready integration that handles API limitations gracefully.
```

### Fallback Analysis System Prompt

```
Create a robust local sentiment analysis system as backup:
- Keyword-based sentiment classification
- Emotional pattern recognition using predefined dictionaries
- Context-aware scoring algorithms
- Crisis phrase detection for safety
- Performance optimization for real-time analysis

Ensure the fallback provides meaningful analysis when external APIs are unavailable.
```

### Crisis Detection Algorithm Prompt

```
Implement a mental health crisis detection system with:
- Multi-level severity classification (0-3 scale)
- Keyword pattern matching for concerning language
- Context analysis to reduce false positives
- Appropriate response recommendations based on severity
- Integration with mood analysis pipeline
- Logging and monitoring for safety review

Balance sensitivity with specificity to provide helpful intervention without over-alerting.
```

---

## 5. RECOMMENDATION ENGINE

### Personalized Suggestions Prompt

```
Create an intelligent recommendation engine that generates personalized mental wellness suggestions:
- Analyze mood scores, emotions, and user context
- Provide evidence-based coping strategies
- Adapt recommendations to user's specific emotional state
- Include immediate actions and long-term practices
- Consider user's onboarding assessment data for personalization
- Vary recommendations to prevent repetition

Focus on actionable, research-backed mental wellness techniques appropriate for different mood states.
```

### Safety-First Content Strategy Prompt

```
Develop content guidelines for mental health recommendations that:
- Prioritize user safety above all other considerations
- Provide appropriate crisis intervention suggestions
- Avoid giving medical advice or diagnoses
- Include professional help resources when needed
- Use compassionate, non-judgmental language
- Respect diverse cultural approaches to mental wellness

Ensure all generated content meets mental health service standards.
```

---

## 6. DEPLOYMENT AND INTEGRATION

### Production Deployment Strategy Prompt

```
Plan deployment architecture for a mental health application:
- Frontend: Static hosting on Netlify/Vercel for reliability
- Backend: Python Flask API on Railway/Render with database persistence
- Environment variable management for API keys and configuration
- HTTPS enforcement for data security
- CORS configuration for cross-origin requests
- Monitoring and logging setup

Prioritize reliability and security appropriate for mental health data handling.
```

### Performance Optimization Prompt

```
Optimize the application for production performance:
- Frontend: Minimize JavaScript bundle size, optimize images, implement lazy loading
- Backend: Database query optimization, API response caching, connection pooling
- Network: CDN integration, compression, efficient API design
- User Experience: Loading states, progressive enhancement, offline functionality

Ensure fast, reliable performance that doesn't interfere with users seeking mental health support.
```

### Security and Privacy Prompt

```
Implement comprehensive security measures for mental health data:
- Data encryption in transit and at rest
- Input validation and SQL injection prevention
- Rate limiting and abuse prevention
- Privacy-by-design data handling
- Secure API key management
- GDPR-compliant data practices

Mental health applications require the highest security standards to protect vulnerable user data.
```

---

## 7. TESTING AND VALIDATION

### Comprehensive Testing Strategy Prompt

```
Create testing protocols for mental health application:
- Unit tests for AI analysis accuracy
- Integration tests for API endpoints
- User experience testing with diverse mood inputs
- Crisis detection validation with appropriate test cases
- Cross-browser compatibility testing
- Mobile responsiveness verification
- Performance testing under various loads

Ensure reliability standards appropriate for mental wellness applications.
```

### Quality Assurance Prompt

```
Develop quality assurance checklist for mental health app:
- Accuracy of mood analysis across different input types
- Appropriateness of recommendations for various mental states
- Crisis detection sensitivity and specificity
- User interface accessibility standards
- Data privacy compliance verification
- Professional language and tone consistency

Mental health applications require rigorous QA to ensure user safety and trust.
```

---

## 8. PROMPT ENGINEERING BEST PRACTICES

### Iterative Refinement Strategy

```
When refining prompts during development:
1. Start with broad architectural guidance
2. Progressively add specific technical requirements
3. Include context about mental health sensitivity
4. Test outputs for appropriateness and safety
5. Iterate based on technical feasibility and user needs
6. Validate against professional mental health standards
```

### Context-Aware Prompting

```
Always include relevant context in prompts:
- Technical constraints (libraries, frameworks, deployment targets)
- User safety considerations for mental health applications
- Design system consistency requirements
- Performance and accessibility standards
- Integration points between different components
- Regulatory and ethical considerations for health tech
```

---

## CONCLUSION

This prompt engineering approach enabled rapid development of a comprehensive mental wellness application by:

- Providing clear, specific technical requirements
- Maintaining focus on user safety and mental health best practices
- Ensuring consistent design and user experience
- Building robust, production-ready architecture
- Implementing appropriate AI integration with fallback systems

The strategic use of detailed, context-aware prompts allowed for efficient development while maintaining the high standards required for mental health technology.
This document contains the strategic prompts used to guide AI development of MindVibe AI, a mental wellness tracking application with advanced sentiment analysis.

---

## 1. PROJECT CONCEPTUALIZATION

### Initial Vision Prompt

```
I need to create a comprehensive mental wellness application for a hackathon. The app should:
- Track user mood and mental state over time
- Use AI to analyze emotional patterns
- Provide personalized recommendations
- Include crisis detection for safety
- Have a modern, accessible interface

Help me design the complete architecture including frontend pages, backend API structure, and AI integration strategy.
```

### User Experience Design Prompt

```
Design a complete user journey for a mental wellness app called MindVibe AI. Include:
- Landing page that builds trust and explains value
- Onboarding assessment to understand user needs
- Dashboard for daily mood tracking and insights
- Pricing page for premium features

Focus on creating an empathetic, professional design that reduces stigma around mental health support.
```

---

## 2. FRONTEND DEVELOPMENT

### Landing Page Creation Prompt

```
Create a modern, professional landing page for MindVibe AI mental wellness app using HTML, CSS, and JavaScript. Requirements:
- Dark gradient background with glassmorphism effects
- Hero section explaining AI-powered mood tracking
- Features section highlighting key benefits
- Pricing tiers (free and premium)
- Modern animations and hover effects
- Mobile-responsive design
- Call-to-action buttons linking to dashboard and pricing

Use contemporary design trends with blue-to-pink gradient accents (#78dbff to #ff77c6).
```

### Dashboard Interface Prompt

```
Build a sophisticated dashboard interface for mood analysis with:
- Neural activity visualization with animated elements
- Text input area for mood description with character counter
- Voice input capability using Web Speech API
- Real-time AI analysis results display with mood scores
- Interactive charts showing mood trends over time
- Personalized recommendations panel
- Crisis detection alerts with appropriate styling
- Heatmap calendar showing mood patterns
- Sidebar with statistics and insights

Maintain consistent dark theme with blue-pink gradient accents and glassmorphism effects.
```

### Onboarding Assessment Prompt

```
Create a multi-step onboarding questionnaire for mental health assessment:
- Progressive form with 9-10 questions covering demographics, self-awareness, emotional patterns
- Visual progress bar and step indicators
- Dynamic question types: text input, single choice, multiple choice
- Smooth transitions between questions with validation
- Emotional intelligence in question phrasing
- Completion screen with testimonials and call-to-action
- Local storage for data persistence
- Responsive design matching main app theme

Questions should gather insights for personalized AI recommendations while being sensitive to mental health context.
```

### Pricing Page Integration Prompt

```
Design a pricing page that seamlessly integrates with the existing design system:
- Match the sophisticated gradient background and glassmorphism effects
- Present clear value proposition for premium features
- Include multiple payment methods (M-Pesa, cards, bank transfer) for accessibility
- Form validation and user feedback
- Professional pricing presentation with feature comparisons
- Smooth integration with existing navigation and user flow

Ensure the payment flow feels secure and trustworthy for mental health service pricing.
```

---

## 3. BACKEND DEVELOPMENT

### Flask API Architecture Prompt

```
Create a comprehensive Flask backend for mental wellness tracking with:
- RESTful API endpoints for mood analysis, history, and user data
- SQLite database schema for mood entries and user profiles
- CORS configuration for frontend integration
- Error handling and input validation
- Health check endpoints for monitoring
- Structured logging for debugging

Design the API to be scalable and maintainable with clear separation of concerns.
```

### AI Integration Strategy Prompt

```
Implement advanced mood analysis using multiple AI approaches:
- Primary: Hugging Face Transformers API for sentiment and emotion analysis
- Fallback: Local keyword-based analysis for reliability
- Crisis detection algorithms for safety
- Personalized recommendation engine based on user patterns
- Confidence scoring and validation

Create a robust system that works reliably regardless of external API availability, ensuring mental health users always receive support.
```

### Database Design Prompt

```
Design a SQLite database schema for mental wellness tracking:
- Users table for onboarding assessment data
- Mood_entries table with comprehensive analysis fields
- Proper indexing for performance
- Data validation and constraints
- Migration-ready structure
- Privacy considerations for sensitive mental health data

Ensure the schema supports both current features and future enhancements.
```

---

## 4. AI MODEL INTEGRATION

### Hugging Face API Integration Prompt

```
Integrate Hugging Face Inference API for advanced sentiment analysis:
- Use cardiffnlp/twitter-roberta-base-sentiment-latest for sentiment
- Implement SamLowe/roberta-base-go_emotions for emotion detection
- Handle API authentication with secure token management
- Implement retry logic and error handling
- Parse and normalize model outputs for consistent application use
- Rate limiting and response caching strategies

Create a production-ready integration that handles API limitations gracefully.
```

### Fallback Analysis System Prompt

```
Create a robust local sentiment analysis system as backup:
- Keyword-based sentiment classification
- Emotional pattern recognition using predefined dictionaries
- Context-aware scoring algorithms
- Crisis phrase detection for safety
- Performance optimization for real-time analysis

Ensure the fallback provides meaningful analysis when external APIs are unavailable.
```

### Crisis Detection Algorithm Prompt

```
Implement a mental health crisis detection system with:
- Multi-level severity classification (0-3 scale)
- Keyword pattern matching for concerning language
- Context analysis to reduce false positives
- Appropriate response recommendations based on severity
- Integration with mood analysis pipeline
- Logging and monitoring for safety review

Balance sensitivity with specificity to provide helpful intervention without over-alerting.
```

---

## 5. RECOMMENDATION ENGINE

### Personalized Suggestions Prompt

```
Create an intelligent recommendation engine that generates personalized mental wellness suggestions:
- Analyze mood scores, emotions, and user context
- Provide evidence-based coping strategies
- Adapt recommendations to user's specific emotional state
- Include immediate actions and long-term practices
- Consider user's onboarding assessment data for personalization
- Vary recommendations to prevent repetition

Focus on actionable, research-backed mental wellness techniques appropriate for different mood states.
```

### Safety-First Content Strategy Prompt

```
Develop content guidelines for mental health recommendations that:
- Prioritize user safety above all other considerations
- Provide appropriate crisis intervention suggestions
- Avoid giving medical advice or diagnoses
- Include professional help resources when needed
- Use compassionate, non-judgmental language
- Respect diverse cultural approaches to mental wellness

Ensure all generated content meets mental health service standards.
```

---

## 6. DEPLOYMENT AND INTEGRATION

### Production Deployment Strategy Prompt

```
Plan deployment architecture for a mental health application:
- Frontend: Static hosting on Netlify/Vercel for reliability
- Backend: Python Flask API on Railway/Render with database persistence
- Environment variable management for API keys and configuration
- HTTPS enforcement for data security
- CORS configuration for cross-origin requests
- Monitoring and logging setup

Prioritize reliability and security appropriate for mental health data handling.
```

### Performance Optimization Prompt

```
Optimize the application for production performance:
- Frontend: Minimize JavaScript bundle size, optimize images, implement lazy loading
- Backend: Database query optimization, API response caching, connection pooling
- Network: CDN integration, compression, efficient API design
- User Experience: Loading states, progressive enhancement, offline functionality

Ensure fast, reliable performance that doesn't interfere with users seeking mental health support.
```

### Security and Privacy Prompt

```
Implement comprehensive security measures for mental health data:
- Data encryption in transit and at rest
- Input validation and SQL injection prevention
- Rate limiting and abuse prevention
- Privacy-by-design data handling
- Secure API key management
- GDPR-compliant data practices

Mental health applications require the highest security standards to protect vulnerable user data.
```

---

## 7. TESTING AND VALIDATION

### Comprehensive Testing Strategy Prompt

```
Create testing protocols for mental health application:
- Unit tests for AI analysis accuracy
- Integration tests for API endpoints
- User experience testing with diverse mood inputs
- Crisis detection validation with appropriate test cases
- Cross-browser compatibility testing
- Mobile responsiveness verification
- Performance testing under various loads

Ensure reliability standards appropriate for mental wellness applications.
```

### Quality Assurance Prompt

```
Develop quality assurance checklist for mental health app:
- Accuracy of mood analysis across different input types
- Appropriateness of recommendations for various mental states
- Crisis detection sensitivity and specificity
- User interface accessibility standards
- Data privacy compliance verification
- Professional language and tone consistency

Mental health applications require rigorous QA to ensure user safety and trust.
```

---

## 8. PROMPT ENGINEERING BEST PRACTICES

### Iterative Refinement Strategy

```
When refining prompts during development:
1. Start with broad architectural guidance
2. Progressively add specific technical requirements
3. Include context about mental health sensitivity
4. Test outputs for appropriateness and safety
5. Iterate based on technical feasibility and user needs
6. Validate against professional mental health standards
```

### Context-Aware Prompting

```
Always include relevant context in prompts:
- Technical constraints (libraries, frameworks, deployment targets)
- User safety considerations for mental health applications
- Design system consistency requirements
- Performance and accessibility standards
- Integration points between different components
- Regulatory and ethical considerations for health tech
```

---

## CONCLUSION

This prompt engineering approach enabled rapid development of a comprehensive mental wellness application by:

- Providing clear, specific technical requirements
- Maintaining focus on user safety and mental health best practices
- Ensuring consistent design and user experience
- Building robust, production-ready architecture
- Implementing appropriate AI integration with fallback systems

The strategic use of detailed, context-aware prompts allowed for efficient development while maintaining the high standards required for mental health technology.
