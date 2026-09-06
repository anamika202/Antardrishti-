
# Antardrishti AI (अन्तर्दृष्टि)
Privacy-First Reflective Journaling Companion powered by Gemini Flash AI, Firebase Auth, and Google Cloud Firestore.

## 🚀 Cloud Run & Challenge Metadata
- **Challenge Track**: Google Cloud Gen AI Academy APAC (Cohort 3)
- **Service Label**: `dev-tutorial=cloud-run-ai-challenge`
- **Target Platform**: Google Cloud Run (Serverless Container)
- **Live Demo**: https://anamika202.github.io/Antardrishti-/

---

## 🛠️ Architecture & Tech Stack
- **AI Intelligence**: Real-time contextual reflections powered by Gemini Flash AI.
- **Authentication**: Firebase Authentication with instant evaluator tenant isolation.
- **Database**: Google Cloud Firestore with strict per-user sandbox partition.
- **Deployment Specification**: Containerized web application built for Google Cloud Run execution.

---

## 🔒 Firestore Security Rules (`firestore.rules`)
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId}/reflections/{reflectionId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}

📦 Cloud Run Deployment Steps
To deploy the Antardrishti container service to Google Cloud Run:
 * Build Container Image:
   gcloud builds submit --tag gcr.io/[PROJECT_ID]/antardrishti-ai

 * Deploy to Cloud Run with Challenge Label:
   gcloud run deploy antardrishti-ai \
  --image gcr.io/[PROJECT_ID]/antardrishti-ai \
  --platform managed \
  --region asia-southeast1 \
  --allow-unauthenticated \
  --set-labels dev-tutorial=cloud-run-ai-challenge




