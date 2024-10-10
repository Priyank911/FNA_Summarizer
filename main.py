# import os
# import shutil
# import subprocess
# import speech_recognition as sr
# from fastapi import FastAPI, File, UploadFile, HTTPException, Response
# from fastapi.responses import FileResponse
# from fastapi.middleware.cors import CORSMiddleware
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib import colors
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# app = FastAPI()

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000", "*"],  
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Ensure necessary directories exist
# os.makedirs("uploads", exist_ok=True)
# os.makedirs("processed", exist_ok=True)

# @app.post("/upload_video")
# async def upload_video(file: UploadFile = File(...)):
#     """Uploads a video file and processes it to generate a summary."""
#     try:
#         # Save the uploaded file to the 'uploads' directory
#         file_location = f"uploads/{file.filename}"
#         with open(file_location, "wb+") as file_object:
#             shutil.copyfileobj(file.file, file_object)

#         print(f"File {file.filename} saved at {file_location}")

#         # Process the uploaded video and return detailed information
#         detailed_info = process_video(file_location)
#         pdf_path = generate_pdf(detailed_info)
#         # Generate and return the PDF after processing
#         return FileResponse(pdf_path, media_type='application/pdf', filename="video_summary.pdf")
    
#     except Exception as e:
#         print(f"Error during file upload: {str(e)}")
#         raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# def generate_pdf(data):
#     """Generates a PDF file from the provided data."""
#     try:
#         description = data.get("description", "")
#         summary = data.get("summary", "No summary available.")  # Default message if summary is empty

#         # Path to save the PDF
#         pdf_path = "processed/video_summary.pdf"
        
#         # Create a PDF document with better formatting
#         pdf = SimpleDocTemplate(pdf_path, pagesize=letter)
#         styles = getSampleStyleSheet()
#         elements = []

#         # Title
#         title = Paragraph("Video Analysis Summary", styles['Title'])
#         elements.append(title)
#         elements.append(Spacer(1, 12))

#         # Description
#         description_title = Paragraph("Description:", styles['Heading2'])
#         elements.append(description_title)
#         elements.append(Spacer(1, 6))
#         description_text = Paragraph(description, styles['BodyText'])
#         elements.append(description_text)
#         elements.append(Spacer(1, 12))

#         # Summary
#         summary_title = Paragraph("Summary:", styles['Heading2'])
#         elements.append(summary_title)
#         elements.append(Spacer(1, 6))
#         summary_text = Paragraph(summary, styles['BodyText'])
#         elements.append(summary_text)

#         # Build the PDF
#         pdf.build(elements)

#         # Return the PDF file
#         return pdf_path
    
#     except Exception as e:
#         print(f"Error generating PDF: {str(e)}")
#         raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# def process_video(file_path):
#     """Processes the video to extract audio, transcribe it, and generate detailed information."""
#     try:
#         # Extract audio from the video
#         audio_path = extract_audio(file_path)
#         print(f"Audio extracted to {audio_path}")
        
#         # Convert audio to text
#         transcript = speech_to_text(audio_path)
#         print(f"Transcript: {transcript}")

#         # Generate detailed information
#         detailed_info = generate_detailed_info(transcript)
#         return detailed_info  # Return a dict with description and summary
    
#     except Exception as e:
#         print(f"Error processing video: {str(e)}")
#         return {"description": "Error processing video.", "summary": str(e)}

# # def extract_audio(video_path):
# #     """Extracts audio from the provided video file using ffmpeg."""
# #     try:
# #         audio_path = f"processed/{os.path.basename(video_path)}.wav"
# #         # Use ffmpeg to extract audio
# #         subprocess.call([r'C:\ffmpeg\bin\ffmpeg.exe', '-i', video_path, '-ab', '160k', '-ac', '2', '-ar', '44100', '-vn', audio_path])
# #         return audio_path
# #     except Exception as e:
# #         print(f"Error extracting audio: {str(e)}")
# #         raise e

# def extract_audio(video_path):
#     """Extracts audio from the provided video file using ffmpeg."""
#     try:
#         audio_path = f"processed/{os.path.basename(video_path)}.wav"
#         if os.path.exists(audio_path):
#             print(f"File '{audio_path}' already exists. Skipping extraction.")
#             return audio_path
#         subprocess.call([r'C:\ffmpeg\bin\ffmpeg.exe', '-y', '-i', video_path, '-ab', '160k', '-ac', '2', '-ar', '44100', '-vn', audio_path])
#         return audio_path
    
#     except Exception as e:
#         print(f"Error extracting audio: {str(e)}")
#         raise e


# def speech_to_text(audio_path):
#     """Converts audio to text using the SpeechRecognition library."""
#     try:
#         recognizer = sr.Recognizer()
#         with sr.AudioFile(audio_path) as source:
#             audio = recognizer.record(source)
#         text = recognizer.recognize_google(audio)
#         return text
#     except sr.UnknownValueError:
#         return "Speech Recognition could not understand audio."
#     except sr.RequestError as e:
#         return f"Could not request results from Speech Recognition service; {e}"

# def generate_detailed_info(transcript):
#     """Processes the transcript to provide detailed explanations based on keywords."""
#     try:
#         # Define potential explanations based on keywords
#         explanations = {
#             "conflict": "This video discusses ongoing tensions related to regional conflicts, which have drawn international attention.",
#             "environment": "The environmental impacts mentioned in the transcript highlight critical issues facing our planet today.",
#             "economy": "Economic discussions often relate to market fluctuations and their broader implications for global trade.",
#         }

#         # Extract keywords from the transcript to identify which explanation to use
#         relevant_explanations = []
#         for key in explanations:
#             if key in transcript.lower():
#                 relevant_explanations.append(explanations[key])

#         # Create the description and summary
#         description = f"{transcript}."  # Description is the transcript
#         summary = (
#             "In summary, this video provides insights on the following key themes: "
#             + " ".join(relevant_explanations) + " "
#             "This highlights the importance of these issues and encourages further discussion."
#         )
        
#         return {
#             "description": description,
#             "summary": summary
#         }
    
#     except Exception as e:
#         print(f"Error generating detailed information: {str(e)}")
#         return {
#             "description": "Error generating detailed information.",
#             "summary": str(e)
#         }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

import os
import shutil
import subprocess
import speech_recognition as sr
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from mangum import Mangum  # Adapter for serverless environments

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure directories exist
os.makedirs("uploads", exist_ok=True)
os.makedirs("processed", exist_ok=True)

@app.post("/upload_video")
async def upload_video(file: UploadFile = File(...)):
    try:
        file_location = f"uploads/{file.filename}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)

        detailed_info = process_video(file_location)
        pdf_path = generate_pdf(detailed_info)
        return FileResponse(pdf_path, media_type='application/pdf', filename="video_summary.pdf")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

def generate_pdf(data):
    try:
        description = data.get("description", "")
        summary = data.get("summary", "No summary available.")
        pdf_path = "processed/video_summary.pdf"
        pdf = SimpleDocTemplate(pdf_path, pagesize=letter)
        styles = getSampleStyleSheet()
        elements = []

        title = Paragraph("Video Analysis Summary", styles['Title'])
        elements.append(title)
        elements.append(Spacer(1, 12))

        description_title = Paragraph("Description:", styles['Heading2'])
        elements.append(description_title)
        elements.append(Spacer(1, 6))
        description_text = Paragraph(description, styles['BodyText'])
        elements.append(description_text)
        elements.append(Spacer(1, 12))

        summary_title = Paragraph("Summary:", styles['Heading2'])
        elements.append(summary_title)
        elements.append(Spacer(1, 6))
        summary_text = Paragraph(summary, styles['BodyText'])
        elements.append(summary_text)

        pdf.build(elements)
        return pdf_path
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

def process_video(file_path):
    try:
        audio_path = extract_audio(file_path)
        transcript = speech_to_text(audio_path)
        detailed_info = generate_detailed_info(transcript)
        return detailed_info
    
    except Exception as e:
        return {"description": "Error processing video.", "summary": str(e)}

def extract_audio(video_path):
    try:
        audio_path = f"processed/{os.path.basename(video_path)}.wav"
        if os.path.exists(audio_path):
            return audio_path
        subprocess.call([r'C:\ffmpeg\bin\ffmpeg.exe', '-y', '-i', video_path, '-ab', '160k', '-ac', '2', '-ar', '44100', '-vn', audio_path])
        return audio_path
    
    except Exception as e:
        raise e

def speech_to_text(audio_path):
    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech Recognition could not understand audio."
    except sr.RequestError as e:
        return f"Could not request results from Speech Recognition service; {e}"

def generate_detailed_info(transcript):
    try:
        explanations = {
            "conflict": "This video discusses ongoing tensions related to regional conflicts.",
            "environment": "The video mentions environmental impacts.",
            "economy": "The video discusses economic issues and trade impacts.",
        }

        relevant_explanations = [explanations[key] for key in explanations if key in transcript.lower()]
        description = f"{transcript}."
        summary = "This video covers: " + " ".join(relevant_explanations)
        return {"description": description, "summary": summary}
    
    except Exception as e:
        return {"description": "Error generating detailed information.", "summary": str(e)}

# This line is essential to make it compatible with Vercel
handler = Mangum(app)
