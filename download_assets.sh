#!/bin/bash

# Create folders
mkdir -p assets
mkdir -p assets/bakedImages
mkdir -p assets/screensImages
mkdir -p assets/videos
mkdir -p assets/fonts
mkdir -p assets/bunnyVirusImages

# Reference base URL
BASE_URL="https://idas-gameboy.netlify.app"

echo "Downloading Gameboy GLB model..."
curl -L -s "$BASE_URL/gameboy.glb" -o gameboy.glb

echo "Downloading general assets..."
curl -L -s "$BASE_URL/assets/backArrow.png" -o assets/backArrow.png
curl -L -s "$BASE_URL/assets/vectordesign.jpg" -o assets/vectordesign.jpg
curl -L -s "$BASE_URL/assets/apple-touch-icon-BK-U4OMY.png" -o assets/apple-touch-icon-BK-U4OMY.png
curl -L -s "$BASE_URL/assets/favicon-32x32-B_VmjPyH.png" -o assets/favicon-32x32-B_VmjPyH.png
curl -L -s "$BASE_URL/assets/favicon-16x16-C1gCMz7U.png" -o assets/favicon-16x16-C1gCMz7U.png
curl -L -s "$BASE_URL/assets/site-DcafIg3Q.webmanifest" -o assets/site-DcafIg3Q.webmanifest

echo "Downloading baked images..."
declare -a baked=(
  "calcBaked.jpg"
  "cupJoystickBaked.jpg"
  "extraSmallPartsBaked.jpg"
  "floorBaked.jpg"
  "keyboardBaked.jpg"
  "chassisBaked.jpg"
  "gameboyParts2Baked.jpg"
  "gameboyPartsBaked.jpg"
  "smallPartsBaked.jpg"
  "chassis2Baked.jpg"
  "cordsBaked.jpg"
)
for file in "${baked[@]}"; do
  echo "Downloading $file..."
  curl -L -s "$BASE_URL/assets/bakedImages/$file" -o "assets/bakedImages/$file"
done

echo "Downloading screen images..."
declare -a screens=(
  "startScreen.jpg"
  "robotScreen.jpg"
  "projectsScreen.jpg"
  "project3DPortfolioScreen.jpg"
  "projectMobileAppScreen.jpg"
  "projectBrowserExtScreen.jpg"
  "projectRHGScreen.jpg"
  "projectReactPortfolioScreen.jpg"
  "projectFlexboxGameScreen.jpg"
  "projectTicTacToeScreen.jpg"
  "userScreen.jpg"
  "notesScreen.jpg"
  "creditsScreen.jpg"
  "photosScreen.jpg"
  "eeveeScreen.jpg"
  "eeveeScreen2.jpg"
  "yoshiScreen.jpg"
  "yoshiScreen2.jpg"
  "binScreen.jpg"
  "binDocScreen.jpg"
)
for file in "${screens[@]}"; do
  echo "Downloading $file..."
  curl -L -s "$BASE_URL/assets/screensImages/$file" -o "assets/screensImages/$file"
done

echo "Downloading videos..."
declare -a videos=(
  "robot.mp4"
  "wave.mp4"
  "heart.mp4"
  "shortVideo.mp4"
)
for file in "${videos[@]}"; do
  echo "Downloading $file..."
  curl -L -s "$BASE_URL/assets/videos/$file" -o "assets/videos/$file"
done

echo "Downloading fonts..."
curl -L -s "$BASE_URL/assets/fonts/BrownMedium%20Regular.ttf" -o "assets/fonts/BrownMedium Regular.ttf"
curl -L -s "$BASE_URL/assets/fonts/BrownLight%20Regular.ttf" -o "assets/fonts/BrownLight Regular.ttf"

echo "Downloading bunny virus images..."
declare -a bunnies=(
  "bunnyVirusWarning.png"
  "bunnyVirusVictory.jpg"
  "bunnyVirus.png"
)
for file in "${bunnies[@]}"; do
  echo "Downloading $file..."
  curl -L -s "$BASE_URL/assets/bunnyVirusImages/$file" -o "assets/bunnyVirusImages/$file"
done

echo "Assets download complete!"
