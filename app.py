import os
import re
import langcodes
import google.generativeai as genai
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

import config



def streamlit_config():

    # page configuration
    st.set_page_config(page_title=config.PAGE_TITLE)

    # page header transparent color and Removes top padding 
    page_background_color = """
    <style>

    [data-testid="stHeader"] 
    {
    background: rgba(0,0,0,0);
    }

    .block-container {
        padding-top: 0rem;
    }

    </style>
    """
    st.markdown(page_background_color, unsafe_allow_html=True)

    # title and position
    add_vertical_space(config.VERTICAL_SPACE_MEDIUM)
    st.markdown(f'<h2 style="text-align: center;">{config.APP_TITLE}</h2>',
                unsafe_allow_html=True)
    add_vertical_space(config.VERTICAL_SPACE_MEDIUM)



def extract_video_id(video_link):
    """
    Extract video ID from various YouTube URL formats.
    Supports:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID
    - https://www.youtube.com/v/VIDEO_ID
    """
    try:
        # Pattern for youtube.com URLs
        if 'youtube.com' in video_link:
            parsed_url = urlparse(video_link)
            if parsed_url.path == '/watch':
                video_id = parse_qs(parsed_url.query).get('v')
                if video_id:
                    return video_id[0]
            elif '/embed/' in parsed_url.path:
                return parsed_url.path.split('/embed/')[1].split('?')[0]
            elif '/v/' in parsed_url.path:
                return parsed_url.path.split('/v/')[1].split('?')[0]

        # Pattern for youtu.be URLs
        elif 'youtu.be' in video_link:
            parsed_url = urlparse(video_link)
            return parsed_url.path.lstrip('/')

        # If it's already just the video ID (11 characters)
        elif re.match(r'^[A-Za-z0-9_-]{11}$', video_link.strip()):
            return video_link.strip()

        return None

    except Exception as e:
        return None


def _get_transcript_list(video_id):
    """
    Helper function to get transcript list for a YouTube video.
    Returns TranscriptList object or None on error.
    """
    try:
        ytt_api = YouTubeTranscriptApi()
        return ytt_api.list(video_id)
    except Exception as e:
        st.error(config.ERROR_TRANSCRIPT_FETCH.format(error=str(e)))
        return None


def extract_languages(video_id):
    """
    Extract available transcript languages for a YouTube video.
    Returns tuple of (language_list, language_dict) or (None, None) on error.
    """
    # Get transcript list using helper function
    transcript_list = _get_transcript_list(video_id)
    if not transcript_list:
        return None, None

    try:
        # Extract the Language Codes from List ---> ['en','ta']
        available_transcripts = [i.language_code for i in transcript_list]

        # Convert Language_codes to Human-Readable Language_names ---> 'en' into 'English'
        language_list = list({langcodes.Language.get(i).display_name() for i in available_transcripts})

        # Create a Dictionary Mapping Language_names to Language_codes
        language_dict = {langcodes.Language.get(i).display_name():i for i in available_transcripts}

        return language_list, language_dict

    except Exception as e:
        st.error(config.ERROR_TRANSCRIPT_FETCH.format(error=str(e)))
        return None, None



def extract_transcript(video_id, language):
    """
    Extract transcript text for a YouTube video in specified language.
    Returns transcript string or None on error.
    """
    # Get transcript list using helper function
    transcript_list = _get_transcript_list(video_id)
    if not transcript_list:
        return None

    try:
        # Find transcript in the specified language
        transcript = transcript_list.find_transcript([language])

        # Fetch the actual transcript content
        transcript_content = transcript.fetch()

        # Extract Transcript Content from JSON Response and Join to Single Response
        transcript_text = ' '.join([i.text for i in transcript_content])

        return transcript_text

    except Exception as e:
        st.error(config.ERROR_TRANSCRIPT_EXTRACT.format(error=str(e)))
        return None



def generate_summary(transcript_text):
    """
    Generate AI-powered summary using Google Gemini.
    Returns summary string or None on error.
    """
    try:
        # Check if API key exists
        api_key = os.getenv(config.GOOGLE_API_KEY_ENV)
        if not api_key:
            st.error(config.ERROR_API_KEY_MISSING)
            return None

        # Configures the genai Library
        genai.configure(api_key=api_key)

        # Initializes a Gemini 2.5 Flash Generative Model
        model = genai.GenerativeModel(model_name=config.GEMINI_MODEL)

        # Define a Prompt for AI Model
        prompt = config.SUMMARY_PROMPT_TEMPLATE.format(word_limit=config.SUMMARY_WORD_LIMIT)

        response = model.generate_content(prompt + transcript_text)

        return response.text

    except Exception as e:
        st.error(config.ERROR_SUMMARY_GENERATE.format(error=str(e)))
        return None


 
def main():

    # Load the Environment Variables
    load_dotenv()

    # Streamlit Configuration Setup
    streamlit_config()

    # Initialize the Button Variable
    button = False
    video_id = None
    language = None

    with st.sidebar:

        image_url = config.BANNER_IMAGE_PATH
        st.image(image_url, use_container_width=True)
        add_vertical_space(config.VERTICAL_SPACE_MEDIUM)

        # Get YouTube Video Link From User
        video_link = st.text_input(label=config.LABEL_VIDEO_LINK)

        if video_link:
            # Extract the Video ID From URL
            video_id = extract_video_id(video_link)

            if not video_id:
                st.error(config.ERROR_INVALID_URL)
            else:
                # Extract Language from Video_ID
                language_list, language_dict = extract_languages(video_id)

                if language_list and language_dict:
                    # User Select the Transcript Language
                    language_input = st.selectbox(label=config.LABEL_SELECT_LANGUAGE,
                                                options=language_list)

                    # Get Language_code from Dict
                    language = language_dict[language_input]

                    # Click Submit Button
                    add_vertical_space(config.VERTICAL_SPACE_SMALL)
                    button = st.button(label=config.BUTTON_SUBMIT)


    # User Enter the Video Link and Click Submit Button
    if button and video_link and video_id and language:

        # UI Split into Columns
        _, col2, _ = st.columns([config.LAYOUT_LEFT_MARGIN, config.LAYOUT_CENTER_WIDTH, config.LAYOUT_RIGHT_MARGIN])

        # Display the Video Thumbnail Image
        with col2:
            st.image(image=config.YOUTUBE_THUMBNAIL_URL_TEMPLATE.format(video_id=video_id),
                     use_container_width=True)

        # Extract Transcript from YouTube Video
        add_vertical_space(config.VERTICAL_SPACE_MEDIUM)
        with st.spinner(text=config.SPINNER_EXTRACTING):
            transcript_text = extract_transcript(video_id, language)

        if not transcript_text:
            st.error(config.ERROR_TRANSCRIPT_FAILED_GENERIC)
            return

        # Generating Summary using Gemini AI
        with st.spinner(text=config.SPINNER_GENERATING):
            summary = generate_summary(transcript_text)

        # Display the Summary
        if summary:
            st.write(summary)
        else:
            st.error(config.ERROR_SUMMARY_FAILED_GENERIC)
        


if __name__ == '__main__':
    main()

