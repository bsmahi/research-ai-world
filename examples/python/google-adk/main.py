import google.generativeai as genai
import os

# Warning: You must set GOOGLE_API_KEY environment variable.

# Configure the API key
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY", "your-api-key"))

# List available models (just to verify connection)
print("Available models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

# Create a generative model instance
model = genai.GenerativeModel('gemini-pro')

# Generate content
print("\nGenerating content about AI Agents...")
response = model.generate_content("Explain the concept of AI Agents in 50 words.")

print("Response:")
print(response.text)
