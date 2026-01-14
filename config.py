"""
Application configuration constants.

This module centralizes all configuration values, magic strings, and constants
for the YouTube Transcript Summarizer application. This makes the application
more maintainable and easier to customize.
"""

# ============================================================================
# UI Configuration
# ============================================================================

APP_TITLE = "YouTube Transcript Summarizer with GenAI"
PAGE_TITLE = "YouTube"

# ============================================================================
# Image URLs and Assets
# ============================================================================

# Local banner image (faster, more reliable than external URL)
BANNER_IMAGE_PATH = "image/youtube_banner.JPG"

# YouTube thumbnail URL template (HTTPS for security)
YOUTUBE_THUMBNAIL_URL_TEMPLATE = "https://img.youtube.com/vi/{video_id}/0.jpg"

# ============================================================================
# AI Configuration
# ============================================================================

# Google Gemini model name
GEMINI_MODEL = "gemini-2.5-flash"

# Summary generation prompt template
SUMMARY_PROMPT_TEMPLATE = """You are a YouTube video summarizer. You will be taking the transcript text and summarizing the entire video,
                    providing the important points with proper sub-headings in a concise manner (within {word_limit} words).
                    Please provide the summary of the text given here: """

# Summary word limit
SUMMARY_WORD_LIMIT = 500

# ============================================================================
# API Configuration
# ============================================================================

# Environment variable name for Google API key
GOOGLE_API_KEY_ENV = "GOOGLE_API_KEY"

# ============================================================================
# Layout Configuration
# ============================================================================

# Column layout ratios for centered content display
LAYOUT_LEFT_MARGIN = 0.07
LAYOUT_CENTER_WIDTH = 0.83
LAYOUT_RIGHT_MARGIN = 0.10

# Vertical spacing units
VERTICAL_SPACE_SMALL = 1
VERTICAL_SPACE_MEDIUM = 2

# ============================================================================
# Error Messages
# ============================================================================

ERROR_INVALID_URL = "Invalid YouTube URL. Please enter a valid YouTube video link."
ERROR_API_KEY_MISSING = f"Google API key not found. Please add {GOOGLE_API_KEY_ENV} to your .env file."
ERROR_TRANSCRIPT_FETCH = "Error fetching transcripts: {error}"
ERROR_TRANSCRIPT_EXTRACT = "Error extracting transcript: {error}"
ERROR_SUMMARY_GENERATE = "Error generating summary: {error}"
ERROR_TRANSCRIPT_FAILED_GENERIC = "Failed to extract transcript. Please try again."
ERROR_SUMMARY_FAILED_GENERIC = "Failed to generate summary. Please try again."

# ============================================================================
# Input Labels
# ============================================================================

LABEL_VIDEO_LINK = "Enter YouTube Video Link"
LABEL_SELECT_LANGUAGE = "Select Transcript Language"
BUTTON_SUBMIT = "Submit"

# ============================================================================
# Spinner Messages
# ============================================================================

SPINNER_EXTRACTING = "Extracting Transcript..."
SPINNER_GENERATING = "Generating Summary..."
