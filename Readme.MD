# 🧳 CrewAI Travel Planner

A simple AI travel planner built with [CrewAI](https://www.crewai.com/) and OpenAI's `gpt-4o-mini`.
Enter any city and an AI travel-guide agent creates a **3-day itinerary** covering its most popular places, 3 per day.

## ✨ Features

- Interactive: asks for a city at runtime
- One AI agent acting as an experienced Indian travel guide
- Short, easy-to-read 3-day plan (3 places per day)
- Uses CrewAI task inputs (`{city}`) for dynamic prompts
- API keys kept safe in a `.env` file

## 🛠️ Tech Stack

- Python 3.10+
- CrewAI
- OpenAI `gpt-4o-mini`
- python-dotenv

## 📁 Project Structure

```
crew-ai/
├── app.py            # Agent, task and crew definition
├── .env              # Your API key (not committed)
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/kovarthanan/crewai-travel-planner.git
cd crewai-travel-planner
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install crewai python-dotenv
```

### 4. Add your OpenAI API key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run

```bash
python app.py
```

## 💡 Example

```
Which city? Chennai

Day 1:
- Marina Beach
- Kapaleeshwarar Temple
- Fort St. George

Day 2:
- ...
```

## ⚙️ How It Works

1. **Agent**: a "Travel planner" with 10 years of experience across India, told to explain things simply.
2. **Task**: build a 3-day plan for `{city}` with the most popular places.
3. **Crew**: runs the agent on the task with `crew.kickoff(inputs={"city": city})`, which fills in the city name.

## 🔮 Future Improvements

- Add a research agent with web search for live info (timings, ticket prices)
- Let the user choose the number of days and interests (nature, temples, food)
- Show the output as a formatted table using `rich`
- Add a Streamlit web UI

## 🔒 Note

Never commit your `.env` file. Add it to `.gitignore`:

```
venv/
.env
__pycache__/
```