# wumpus
## Running without Docker
Use `python game.py`

## Running through Docker
Run the following: </br>
`sudo docker build .` </br>
`sudo docker image ls` Determine image hash for next command </br>
`sudo docker run -ti <image hash> sh` </br>
`python game.py`
