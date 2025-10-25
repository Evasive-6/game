# Color Memory Challenge

A fun and engaging mini game app built with Django backend and React Native + Expo frontend. Test your memory by repeating increasingly complex color sequences!

## Features

- **Color Sequence Game**: Watch and repeat color sequences that get progressively harder
- **Score Tracking**: Keep track of your high scores and game statistics
- **User Authentication**: Register and login to save your progress
- **Responsive Design**: Modern UI with gradients, animations, and smooth interactions
- **Cross-Platform**: Built as a mobile app deployable as APK

## Tech Stack

### Backend
- **Django**: Web framework for building the API
- **Django REST Framework**: For creating RESTful APIs
- **SQLite**: Database for development (easily configurable for production)

### Frontend
- **React Native**: Framework for building native mobile apps
- **Expo**: Platform for universal React applications
- **TypeScript**: For type-safe JavaScript
- **Tailwind CSS**: Utility-first CSS framework via NativeWind
- **Expo Router**: File-based routing for React Native

## Project Structure

```
mobile-app-demo/
├── backend/          # Django backend
│   ├── backend/      # Django project settings
│   ├── game/         # Game app with models, views, serializers
│   └── requirements.txt
├── frontend/         # React Native + Expo frontend
│   ├── app/          # App screens and navigation
│   ├── components/   # Reusable UI components
│   ├── assets/       # Images and icons
│   └── package.json
└── README.md         # This file
```

## Installation

### Prerequisites
- Python 3.8+
- Node.js 18+
- Expo CLI
- Android Studio (for Android development)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the Django server:
   ```bash
   python manage.py runserver
   ```

The backend will be running at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the Expo development server:
   ```bash
   npx expo start
   ```

4. Run on your device:
   - For Android: Press `a` in the terminal or use Expo Go app
   - For iOS: Press `i` in the terminal (macOS required)
   - For web: Press `w` in the terminal

## Usage

1. **Register/Login**: Create an account or log in to save your scores
2. **Start Game**: Tap the start button to begin
3. **Watch Sequence**: Pay attention to the color sequence
4. **Repeat Sequence**: Tap the colors in the same order
5. **Score Points**: Earn points for each correct sequence
6. **Game Over**: Try again and beat your high score!

## API Endpoints

- `GET /api/games/` - List all games
- `POST /api/games/` - Create a new game
- `GET /api/scores/` - Get user scores
- `POST /api/scores/` - Submit a score

## Building APK

1. Configure EAS Build in `frontend/eas.json`
2. Install EAS CLI:
   ```bash
   npm install -g @expo/eas-cli
   ```

3. Build the APK:
   ```bash
   eas build --platform android
   ```

## Deployment

### Backend Deployment
The backend is configured for deployment on Render with:
- `Procfile` for process definition
- `render.yaml` for deployment configuration

### Frontend Deployment
- APK can be built and distributed via Expo Application Services (EAS)
- Web version can be deployed to any static hosting service

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

