# Google Meet Bot 

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
- **Virtual Audio Cable:**  
  Download and install [Virtual Audio Cable](https://vac.muzychenko.net/en/). This software is used to route the audio playback directly to a virtual line, ensuring that the audio is transmitted clearly during the Google Meet session. Configure the Virtual Audio Cable to create a virtual line and set it as the default playback device.
## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/a1bderrahmane/GoogleMeetBot.git
   cd GoogleMeetBot

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
```

FFmpeg Installation: Ensure that FFmpeg is installed and its bin folder is added to your system's PATH:

## Architecture
The project follows a modular design:

- **Audio Class:** Handles audio playback using FFmpeg (ffplay) ,it executes the appropriate shell command to start the audio. The class also ensures efficient process management by controlling playback duration and terminating the process when needed.
- **GoogleAuthenticator Class:** Manages login operations using Selenium, loading credentials from environment variables, and setting Chrome options for a smooth automated login experience.
- **GoogleMeetBot Class:** Automates joining a Google Meet session by:
  - Navigating to the provided meeting link.
  - Clicking the join button.
  - Verifying the meeting entry.
  - Playing audio via the Audio class.

## UML Diagram
![UML Diagram](UML.svg)

## Behavior of the App

- **Authentication:** The app uses the GoogleAuthenticator class to open a Chrome session and log into your Google account using credentials provided in the .env file.
- **Meeting Joining:** Once authenticated, the GoogleMeetBot class navigates to the specified Google Meet link and simulates a user clicking the join button. It also checks if the meeting has successfully started by detecting a meeting identifier on the page.
- **Audio Playback:** After joining the meeting, the Audio class is invoked to play an audio file using FFmpeg. The process is monitored and stopped after a duration specified in the configuration.

## Running the Project
After setting up the environment and configuring the variables, ensure that you create a virtual audio line using VAC (Virtual Audio Cable) to route the audio properly. Once the virtual line is set up, run the project with:
```bash
python main.py
```
The script will launch Chrome, perform the login, join the Google Meet session, and play the audio file as configured.
