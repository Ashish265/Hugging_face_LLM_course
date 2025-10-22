from transformers import pipeline

classifier = pipeline("sentiment-analysis")
classifier("I've been waiting for a huggingface course my whole life")
