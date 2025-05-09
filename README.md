# wumpus
## Running without Docker
Use `python game.py`

## Running through Docker
Run the following:  
`sudo docker build .`  
`sudo docker image ls` Determine image hash for next command  
`sudo docker run -ti <image hash> sh`  
`python game.py`
