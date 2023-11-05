#  Duke Fall 2023 Generative AI Hackathon - Team 6
## FixIt Handyman with YouTube Integration

Pipelined OpenAI GPT3.5-Turbo using YouTube transcripts for Retreval Autmated Generation making clear, how-to lists through Flask endpoints.

We built a React webapp to wrap this tool for use as a helpful AI handyman where users can input their issue and recieve a clear set of how-to steps. This includes clicking in to each step for elaboration, along with an embedded YouTube vieo and estimated difficulty, time, and cost.

### To Use
```bash 
pip install -r requirements.txt
cd backend/
python ./flask_server.py
```
```bash
cd frontend/
npm install
npm start
```

### Repo Structure
```
- requirements.txt
- backend/
    - combined_yt_gpt.py
    - flask_server.py
    - query_gpt.py
- frontend/
    - public
    - src
        - apis/
        - components/
        - App.js
        - App.css
        - index.js
    - package.json
    - package-loc.json
```
