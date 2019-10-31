# MISTIFY
## A Playlist for Every Atmosphere

##### Spotify User ID
See attached PDFs for how to obtain your Spotify user ID using either the mobile app, desktop app, or in browser.

##### Spotify Authorization
Once the city, country code, and Spotify ID have been submitted, a new window/tab will open showing "https://google.com/" followed by a long string of characters. This entire URL needs to be copy and pasted into the terminal to give the app authorization to access your Spotify account defined in the scope.

##### How It Works
Mistify uses the OpenWeather API to find the current weather forecast for the provided city & country. It uses the weather description to search the Pixabay API for a related image that is then used as the background for the web application. Concurrently, the weather description is also to search the Spotify API for a playlist related to the weather. The playlist is displayed in the Spotify widget in the web app.
