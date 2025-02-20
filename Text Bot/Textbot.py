import os
import json
print("Welcome to SFS System Maker")
print("©2024 Mariohobbs")
def smhelp():
    print("use command smhelp() to access the help menu")
    print("Use command 'setup()' to setup a system")
    print("Use command 'hmap()' to create a heightmap")
    print("Use command 'pd()' to create a planet")
    print("a guide on basic usage: https://spaceflight-simulator.fandom.com/wiki/Planet_Editor_Tutorial")
def setup():
    #Setup the planet pack
    #Creates Import Settings file and obtains the variables in the file
    file = "Import_Settings.txt"
    dp = input("Include Default Planets?(true/false) ")
    dh = input("Include Default Heightmaps?(true/false) ")
    dt = input("Include Default Textures?(true/false) ")
    hs = input("Hide Stars In Atmosphere?(true/false) ")
    #Converts the input into a string that'll be written soon
    ist = '{\n  "includeDefaultPlanets"; '+dp+","+'\n'+'  "includeDefaultHeightmaps": '+dh+","+'\n'+'  "includeDefaultTextures": '+dt+','+'\n'+'  "hideStarsInAtmosphere": '+hs+"\n"+"}"
    with open(file, 'w') as file:
        # Write content to the file
        file.write(ist)
     
    print("Import_Settings.txt Created Successfully")
    #Creates Space_Center_Data.txt
    file = "Space_Center_Data.txt"
    ad = input("Input where the space center will be (EX: Earth, Mars; use the name of the planet ")
    an = input("What will the angle of the space center be? ")
    hp = input("What will be the launchpad's horizontal position (In the frame of reference of the space center ")
    he = input("What will be the height of the launchpad? ")
    #Converts your data into a string
    ist = '{\n  "address": "'+ad+'",\n  "angle": '+an+',\n  "position_Launchpad": {\n    "horizontalPosition": '+hp+',\n    "heightVe": '+he+'\n  }\n}'
    with open(file, 'w') as file:
        # Write content to the file
        file.write(ist)
    print("Space_Center_Data.txt Created Successfully ")
    #Create Version.txt
    file = "Version.txt"
    ve = input("What version is this pack for? ")
    with open(file, 'w') as file:
        # Write content to the file
        file.write(ve)
    print("Version.txt Created")
    os.mkdir("Heightmap Data")
    os.mkdir("Planet Data")
    os.mkdir("Texture Data")
    print("Heightmap Folder Created!")
    print("Planet Data Folder Created!")
    print("Textures Folder Created")
    print("Basic Setup Completed")
def hmap():
    #Get a name for the heightmap
    hname = input("What will the heightmap be called?")
    file = "Heightmap Data/"+hname+".txt"
    point = 0
    heightmap = []
    #Repeatedly asks for the points
    while not point == "quit":
        point = input("Input a point or type quit if you are done ")
        if not point == "quit":
            heightmap.append(point)
    print(heightmap)
    heightmapstring = '{\n    "points": ['
    count = 0
    #Add the data from user to a string
    for i in heightmap:
        if count == 0:
            heightmapstring = heightmapstring+"\n"+"        "+i
            count = count+1
        else:
            heightmapstring = heightmapstring+",\n"+"        "+i
    heightmapstring = heightmapstring+"\n    ]\n}"
    with open(file, 'w') as file:
        # Write heightmap string to the file
        file.write(heightmapstring)
         
def pd():
    #Get a name for the planet
    file = "Planet Data/"+input("What will the planet be called? ")+".txt"
    data ={
        #base data
        "version": "1.5",
        "BASE_DATA": {
            "radius": int(input("Radius of body")),
            "radiusDifficultyScale": {},
            "gravity": int(input("Gravity")),
            "gravityDifficultyScale":{},
            "timewarpHeight": int(input("Timewarp Height")),
            "velocityArrowsHeight":"NaN",
            "mapColor": {
                "r": int(input("Red amount of body on map")),
                "g": int(input("Green amount of body on map")),
                "b": int(input("Blue amount of body on map")),
                "a": int(input("Alpha value of body on map"))
            },
            "significant":bool(input("Is the body considered significant T/F")),
            "rotateCamera":bool(input("Does the camera rotate? true or false"))
        },
        #Terrain Data
        "TERRAIN_DATA": {
            "TERRAIN_TEXTURE_DATA": {
                "planetTexture": input("Planet texture name"),
                "planetTextureCutout": int(input("cutout amount of tex")),
                "surfaceTexture_A": input("surface tex A"),
                "surfaceTextureSize_A": {
                    "x":int(input("size of surface tex x")),
                    "y":int(input("Size of surface tex Y"))
                },
                "surfaceLayerSize": int(input("Surface Layer size")),
                "minFade": int(input("Min Fade")),
                "maxFade": int(input("Max Fade")),
                "shadowIntensity": int(input("Shadow intensity")),
                "shadowHeight": int(input("shadow height"))
            },
            "terrainFormulaDifficulties": {
                "Normal": [input("Insert the full height map list")]
            },
            "textureFormula": [],
            "verticeSize":int(input("vertice size, number")),
            "collider":int(input("collider, true or false"))
        },
        "ORBIT_DATA": {
            "parent":input("what does it orbit"),
            "semiMajorAxis":int(input("Semi major axis")),
            "smaDifficultyScale": {},
            "eccentricity":int(input("Eccentricity")),
            "argumentOfPeriapsis":int(input("argument of periapsis")),
            "direction":int(input("direction")),
            "multiplierSOI":int(input("multiplierSOI")),
            "soiDifficultyScale":{}
        },
        "ACHIEVEMENT_DATA": {
            "Landed":bool(input("Achievement for Landing, True or false")),
            "Takeoff":bool(input("Achievement for takeoff, true or false")),
            "Atmosphere":bool(input("Achievement for atmosphere true or false")),
            "Orbit":bool(input("Achievement for orbit, True or false")),
            "Crash":bool(input("Achievement for crashing, True or false"))
        },
        "LANDMARKS":[]
        }
    print(data)
    with open(file, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    
