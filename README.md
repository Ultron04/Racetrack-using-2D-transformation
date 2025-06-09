# Racetrack-using-2D-transformation
The main goal of this project is to simulate a race track using the principles of 2D transformations. The intent is to offer a visual demonstration of how mathematical transformations can result in believable motion. The car in the center does not actually move; instead, the track and environment shift to create the illusion of motion. This approach not only simplifies implementation but also highlights how efficient transformation-based animations can be in 2D space.

## Tools and Tech Used
1.	Programming Language: Python 3.x 
2.	Graphics Library: Pygame 
3.	Graphics Asset: car.png image file

## Project description 
Let's break down how this racing track simulation works, all powered by Python and Pygame:
1.	The Illusion of Movement: We create the sense of driving by constantly sliding (translating) individual road segments downward on the screen. The car itself remains fixed, giving you the feeling you're moving through the world.
2.	Building the Curves: The track's natural-looking curves come from sine waves. These waves smoothly adjust each road segment's horizontal position, creating those realistic turns and bends.
3.	Road Construction: The track is built piece by piece, using many rectangular segments stacked vertically. Each segment's exact horizontal center is pre-calculated based on our special path, which includes both straightaways and those sine-wave-driven curves.
4.	Visual Details: To make it feel real, we've added things like clear road boundaries, bright white edge lines, and a dotted white line down the center.
5.	Infinite Loop: The animation is driven by a frame_count. This keeps the track endlessly looping, so you get that seamless, infinite racing experience.
6.	Start/Finish Marker: Look out for a subtle visual cue: a periodic gap in the dotted center line. This clever detail acts as your "start/finish" line, helping you track your laps.
7.	User Controls: For simple interaction, we've included familiar "Play," "Pause," and "Quit" buttons.

## Preview
<img src="https://github.com/user-attachments/assets/22e3129d-bcd9-4341-9d01-540300e6a816" alt="Racing Track Preview" width="500"/>
<img src="https://github.com/user-attachments/assets/a11a7ab5-5892-4559-8be5-1ea95c9aeb06" alt="Racing Track Preview" width="500"/>
