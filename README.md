# gazebo_quadcopter_model
Gazebo model of quadcopter and world with multiple instances.

This project is a quadcopter model for Gazebo.
It's an updated version of the example Gazebo quadcopter model, located in: 
/usr/share/gazebo-5.3/worlds/quad_rotor_demo.world

The use case for this model was multi-robot colaboration/swarms.
So I wanted to have a world where I could ideally spawn multiple instances of a single model.
However I was having difficulties getting this to work in Gazebo.
So I took a different approach, where by I created a template model file with a placeholder model name.
When I wanted multiple quads in a world, I used a simple Python script to copy the quad model template and update the model name place holder.
Then in the Gazebo world file I could simply include the individual quad models.
This worked pretty well.

Also I wanted the models I developed to be in my local workspace directory.
I copied the standard Gazebo setup.sh script and added my model paths.
So there is a boot2292.sh script that runs the custom setup script, then boots a world with three quads.
From there I would run controller applications which interfaced with the Gazebo world and controlled the quads.

To run, update your paths in modelDev/gz_setup.sh, then source boot2292.sh.
If you want to change the number of quads in the world, or want them to have differnet names, update genModels.py and rerun.

Thanks for your interest!

![Alt text](screenshot.png?raw=true "Quadcopters")
