from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "This is the AIML Project API"}

@app.get("/predict/")
def predict(maths_marks: float, aiml_marks: float, hs_marks: float):
    prediction = maths_marks*0.05923455 + aiml_marks*0.05228749 + hs_marks*0.0188615 + 5.02906376
    return {
        "Maths marks": maths_marks,
        "AIML marks": aiml_marks,
        "HS Marks": hs_marks,
        "Predicted CGPA": prediction
    }
