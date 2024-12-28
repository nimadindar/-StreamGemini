import google.generativeai as genai

def get_model():
    APIKEY = "REPLACE-WITH-YOUR-API-KEY"
    genai.configure(api_key=APIKEY)
    return genai.GenerativeModel("gemini-1.5-flash")

def gen_text(prompt):
    model = get_model()  
    response = model.generate_content(prompt)
    return response.text

