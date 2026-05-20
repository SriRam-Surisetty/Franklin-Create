from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Franklin Create MVP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    id: int
    text: str
    type: str
    options: List[str]

class Answer(BaseModel):
    question_id: int
    answer: str

class AnswerSubmission(BaseModel):
    answers: List[Answer]

QUESTIONS = [
    {
        "id": 1,
        "text": "What is your primary use case for this product?",
        "type": "text",
        "options": []
    },
    {
        "id": 2,
        "text": "How often would you use this tool?",
        "type": "single",
        "options": ["Daily", "Weekly", "Monthly", "Rarely"]
    },
    {
        "id": 3,
        "text": "Which features are most important to you?",
        "type": "multi",
        "options": ["Content generation", "Template management", "Collaboration", "Integrations", "Exporting / Publishing"]
    },
    {
        "id": 4,
        "text": "How satisfied are you with the current MVP?",
        "type": "single",
        "options": ["0", "1", "2", "3", "4", "5"]
    },
    {
        "id": 5,
        "text": "What is the single biggest improvement we could make?",
        "type": "text",
        "options": []
    }
]

BEST_ANSWERS = {
    2: "Daily",
    4: "5"
}

@app.get("/api/questions", response_model=List[Question])
def list_questions():
    return [Question(**q) for q in QUESTIONS]

@app.post("/api/submit")
def submit_answers(submission: AnswerSubmission):
    score = 0
    results = []

    for answer in submission.answers:
        question = next((q for q in QUESTIONS if q["id"] == answer.question_id), None)
        if not question:
            continue

        best = BEST_ANSWERS.get(answer.question_id)
        correct = best is not None and answer.answer == best
        if correct:
            score += 1

        results.append({
            "question_id": question["id"],
            "question": question["text"],
            "answer": answer.answer,
            "best_answer": best,
            "correct": correct
        })

    return {
        "score": score,
        "total": len(BEST_ANSWERS),
        "percentage": round((score / len(BEST_ANSWERS)) * 100, 1) if BEST_ANSWERS else 0,
        "results": results,
        "message": "Thank you for completing the MVP questionnaire."
    }

@app.get("/")
def root():
    return {"message": "Franklin Create MVP backend is running."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
