# YouTube Video Transcript Summarizer with Generative AI

**Introduction**
test2
The YouTube Video Transcript Summarizer with GenAI is an innovative tool designed to save time by automatically generating concise summaries from YouTube video transcripts. This application leverages the YouTube Transcript API to retrieve video transcripts, and integrates Google's Gemini AI to summarize them, helping users get key takeaways quickly without watching the entire video. With a clean, user-friendly interface built using Streamlit, this project simplifies the process of obtaining summaries from video content, making it accessible to students, professionals, and anyone looking to boost their productivity.

<br />

**Table of Contents**

1. Key Technologies and Skills
2. Requirements
3. Installation
4. Usage
5. Features
6. Recent Updates & Improvements
7. Contributing
8. License
9. Contact

<br />

**Key Technologies and Skills**
- Python
- Google Generative AI
- YouTube Transcript API
- Prompt Engineering
- Streamlit

<br />

**Requirements**
- Python 3.7 or higher
- Google API Key (for Gemini AI)
- Internet connection (for YouTube Transcript API)

**Key Dependencies:**
- `youtube-transcript-api>=0.6.0` - For retrieving video transcripts
- `google-generativeai` - For AI-powered summarization (Gemini 2.5 Flash)
- `streamlit` - For web interface
- `langcodes` - For language name conversion

<br />

**Installation**

To run this project, you need to install the following packages:

```bash
pip install -r requirements.txt
```

<br />

**Usage**

To use this project, follow these steps:

1. Clone the repository: ```git clone https://github.com/gopiashokan/YouTube-Video-Transcript-Summarizer-with-GenAI.git```
2. Install the required packages: ```pip install -r requirements.txt```
3. Get your Google API key:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Click "Create API Key" to generate your key
4. Create a `.env` file in the root directory (use `.env.example` as template)
5. Add your Google API key to the `.env` file:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```
   **⚠️ IMPORTANT:** Never commit your `.env` file to Git. It contains sensitive API keys.
6. Run the Streamlit app: ```streamlit run app.py```
7. Access the app in your browser at ```http://localhost:8501```

<br />

**Features**

#### YouTube Video Transcript Retrieval:

   - **Input Video Link:** Users can easily provide a YouTube video link to the application. The system automatically extracts the video ID from various YouTube URL formats (standard, shortened, embed) and prepares the request for the transcript.

   - **Transcript Language Detection:** Using the `YouTube Transcript API` (v1.2.3+), the application detects all available transcript languages for the given video. The updated implementation uses the modern API workflow with instance methods for improved reliability.

   - **Language Conversion:** The detected language codes are transformed into human-readable names using the `Langcodes` library, allowing users to effortlessly identify and select their preferred transcript language.


#### Transcript Processing:

   - **Language Selection:** Once the user selects their preferred transcript language, the YouTube Transcript API retrieves the transcript in that language. This step ensures that the transcript is tailored to the user’s language choice, preparing it for accurate AI processing.

   - **Transcript Handling:** The application then processes and formats the retrieved transcript to ensure it meets the requirements of the generative AI model. This step involves cleaning and organizing the text for effective summarization by the AI.


#### AI-Powered Summarization:

   - **Generative AI Model:** The project incorporates Google's Gemini AI `gemini-2.5-flash` model to generate summaries. The model processes the video transcript along with a carefully crafted prompt to deliver concise, accurate, and context-aware summaries, eliminating the need for users to watch the entire video.

   - **Custom Prompting:** The system uses an intelligently designed prompt that guides the AI in producing relevant summaries, ensuring the key points from the video are captured and presented clearly.


#### Streamlit Application:

   - **User-Friendly Interface:** The entire application is built using Streamlit, which provides a smooth and interactive interface. This ensures that users can easily input video links, select languages, and view the summarized content, all in one place.

   - **Real-Time Interaction:** The application provides real-time feedback and results, allowing users to receive their video summaries almost instantly. This makes the experience not only efficient but also highly responsive to user actions.


#### Recent Updates & Improvements:

   - **API Compatibility:** Updated to support the latest YouTube Transcript API (v1.2.3+) with modern instance-based methods
   - **AI Model Upgrade:** Migrated from deprecated `gemini-pro` to current `gemini-2.5-flash` model for improved performance
   - **Enhanced Security:** Added `.gitignore` and `.env.example` for better API key management and repository security
   - **Code Quality:** Fixed deprecation warnings and improved error handling throughout the application
   - **Documentation:** Improved setup instructions and added comprehensive environment configuration guide


#### References:

   - Streamlit: [https://docs.streamlit.io/](https://docs.streamlit.io/)
   - Google Gemini AI: [https://ai.google.dev/](https://ai.google.dev/)
   - YouTube Transcript API: [https://pypi.org/project/youtube-transcript-api/](https://pypi.org/project/youtube-transcript-api/)
   - Langcodes: [https://pypi.org/project/langcodes/](https://pypi.org/project/langcodes/)

<br />

**Contributing**

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request.

<br />

**License**

This project is licensed under the MIT License. Please review the LICENSE file for more details.

<br />

**Contact**

📧 Email: gopiashokankiot@gmail.com 

🌐 LinkedIn: [linkedin.com/in/gopiashokan](https://www.linkedin.com/in/gopiashokan)

For any further questions or inquiries, feel free to reach out. We are happy to assist you with any queries.

