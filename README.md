# skyScraper
https://www.linkedin.com/posts/gregorybufithis_today-an-entire-industry-stopped-making-activity-7461015327804678144-vG4u/
Yes — conceptually you are building an application/pipeline.
Not just “a scraper.”
The scraper is only the data collection layer.
The actual interesting system is:

Internet Media
   ↓
Scraping / Collection
   ↓
Understanding Geometry
   ↓
3D Reconstruction
   ↓
Scene Generation
   ↓
Interactive Environment

So the scraping part is actually the easiest 10%. What are you actually trying to build?
From what you described, the end goal sounds like: “Take images/videos and automatically generate explorable 3D environments.”

That means your system has roughly 5 major stages.
-----------------------------------------------------------------------------------
Full pipeline
Stage 1 — Data Collection (Scraping)
Goal: Collect images/videos

Tools:
Python
Selenium / Playwright
requests
yt-dlp

Output:
images/
videos/
metadata.json

At this point you ONLY have raw media.
No 3D yet.
-----------------------------------------------------------
Stage 2 — Scene Understanding

Now AI tries to understand:

depth
surfaces
camera angle
object boundaries
lighting
motion

This is where Computer Vision starts.
Example
Input image:
A room photo
AI predicts: Wall depth
Table location
Floor geometry
Camera perspective

Models used:

MiDaS
Depth Anything
SAM
OpenCV

Output:

depth map
segmentation map
camera pose
-----------------------------------------------------------------------------------
Stage 3 — 3D Reconstruction

Now the system converts that understanding into actual 3D structure.

This is the magic part.

From a SINGLE image

The AI “hallucinates” missing geometry.

Very approximate.

From VIDEO or MULTIPLE IMAGES

Much better.

Because:

multiple angles exist
motion gives depth clues

This is how:

NeRF
Gaussian Splatting
COLMAP

work.

Important concept

A video is basically:

many images + camera movement

Camera movement is GOLD for 3D reconstruction.

Example pipeline

Video frames:

frame1
frame2
frame3
frame4

↓

System estimates:

camera moved left
object shifted
depth changed

↓

Now triangulation becomes possible.

↓

3D structure is reconstructed.

Output after reconstruction

You now get:

point cloud
mesh
Gaussian splats
textured geometry
-----------------------------------------------------------------------------------

Stage 4 — Environment Generation

Now you convert reconstruction into a usable world.

This means:

collision
lighting
textures
navigation
physics

Usually done in:

Blender
Unity
Unreal Engine
Example

You reconstructed:

room
sofa
walls
floor

Now engine adds:

gravity
shadows
movement
collisions

Now it becomes:

explorable
trainable
game-like
-----------------------------------------------------------------------------------

Stage 5 — Robot/AI Training

Now agents can:

walk
navigate
pick objects
learn policies

Frameworks:

NVIDIA Isaac Sim
Habitat
Unity ML-Agents
