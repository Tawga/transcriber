# Transcriber Application

## Overview

This is a simple Python application designed to transcribe audio files. It uses a graphical user interface (GUI) for user interaction and leverages the Whisper library for audio transcription. Additionally, it provides the functionality to save the transcription as an SRT file.

## Components

### 1\. `main.py`

This is the entry point of the application. It initializes the `Transcriber` and `Ui` classes and starts the main event loop.

### 2\. `transcriber.py`

This module contains the `Transcriber` class responsible for handling the transcription process. It uses the Whisper library to transcribe audio files. The class provides methods to transcribe audio and save the transcription as an SRT file.

### 3\. `ui.py`

This module contains the `Ui` class, which defines the graphical user interface of the application. It utilizes the `customtkinter` library for GUI components. Users can select an audio file, choose a transcription model, and opt for translation to English. After transcription, the results are displayed in the UI.

## Usage

1. Run `main.py` to start the application.
2. Use the GUI to select an audio file, choose a model, and specify translation preferences.
3. Click the "Transcribe audio" button to initiate the transcription process.
4. Once the transcription is complete, the results will be displayed in the UI.
5. Optionally, click the "Save as SRT" button to save the transcription as an SRT file.

## Dependencies

- Python 3.x
- Whisper library
- CustomTkinter library

## Note

Ensure that the necessary dependencies are installed before running the application.
