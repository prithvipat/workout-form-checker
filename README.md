# Workout Form Checker App

## Idea
When people initially join a gym, they typically don’t know what they’re 
doing and/or start off with bad form unless they have someone to go with. This app, shows you 
the correct way of doing it and is able to record your sets tells you whats wrong with it. In this way newcomers won't be affair to come into the gym and have the fear of messing up


## Strategy
- Phase 1:
  - Prototype
    - Build core logic
    - Analyze form, detect bad reps, playback
  - Tools
    - Python
    - OpenCV (Video Input/Output)
    - MediaPipe (Pose Detection)
    - NumPy(Calculate angle between joins, distances etc.)
    - TKinter (GUI)

- Phase 2
  - Web Based Application + Mobile Friendly App
  - API Server
    - Flask or FastAPI
    - Video Storage (Local Storage)
  - Tools
    - Flutter (Dart) (UI for andriod and IOS)
    - Axios Call (Python backend)
    - Expo
    - React Native (cross-platform framework)

- Phase 3
  - On-Device Real-Time Analysis
