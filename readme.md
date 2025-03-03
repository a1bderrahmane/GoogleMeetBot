# Google Meet Bot with Audio Playback

This project automates joining a Google Meet session using Selenium and plays an audio file upon successful meeting entry. It also handles Google authentication and automates basic meeting interaction.

## Features

- **Automated Login:** Uses Selenium to log into Google using credentials stored in environment variables.
- **Meeting Join Automation:** Navigates to a specified Google Meet link, clicks the join button, and verifies meeting entry.
- **Audio Playback:** Plays a specified audio file during the meeting using FFmpeg and subprocess calls.
- **Extensible Architecture:** Modular classes for authentication, meeting handling, and audio playback.

## Prerequisites

- **Python 3.7+**
- **Google Chrome** (compatible with [ChromeDriver](https://chromedriver.chromium.org/))
- **FFmpeg:**  
  Download and install [FFmpeg](https://ffmpeg.org/download.html). Make sure to add the FFmpeg executable directory to your system's environment variables (PATH) so that the `ffplay` command is available system-wide.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject

Create a virtual environment:
```bash
python -m venv venv
```

Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Environment Variables: Create a .env file in the root directory and add the following variables:
```dotenv
EMAIL_ID=your_email@gmail.com
EMAIL_PASSWORD=your_password
MEET_LINK=https://meet.google.com/your-meet-id
AUDIO_FILE=path_to_your_audio_file
AUDIO_DURATION=duration_in_seconds
JS_FILE=path_to_your_javascript_file
```

FFmpeg Installation: Ensure that FFmpeg is installed and its bin folder is added to your system's PATH:

Windows: Add the directory containing ffplay.exe to the PATH via System Properties > Environment Variables.
macOS/Linux: You can typically install FFmpeg using a package manager (e.g., `brew install ffmpeg` on macOS).

## Architecture
The project follows a modular design:

- **Audio Class:** Handles audio playback using FFmpeg (ffplay) and integrates with the Selenium driver to potentially inject JavaScript.
- **GoogleAuthenticator Class:** Manages login operations using Selenium, loading credentials from environment variables, and setting Chrome options for a smooth automated login experience.
- **GoogleMeetBot Class:** Automates joining a Google Meet session by:
  - Navigating to the provided meeting link.
  - Clicking the join button.
  - Verifying the meeting entry.
  - Playing audio via the Audio class.

## UML Diagram
![UML Diagram](UML.png)

## Behavior of the App

- **Authentication:** The app uses the GoogleAuthenticator class to open a Chrome session and log into your Google account using credentials provided in the .env file.
- **Meeting Joining:** Once authenticated, the GoogleMeetBot class navigates to the specified Google Meet link and simulates a user clicking the join button. It also checks if the meeting has successfully started by detecting a meeting identifier on the page.
- **Audio Playback:** After joining the meeting, the Audio class is invoked to play an audio file using FFmpeg. The process is monitored and stopped after a duration specified in the configuration.
- **Continuous Session:** The bot stays in the meeting indefinitely, with periodic sleeps to keep the session active. You can interrupt the session manually (e.g., CTRL+C) to exit.

## Running the Project
After setting up the environment and configuring the variables, run the project with:
```bash
python main.py
```
The script will launch Chrome, perform the login, join the Google Meet session, and play the audio file as configured.

## License
This project is open source and available under the MIT License.