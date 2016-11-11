# DIGITAL WALLET

This is an implementation of the data challenge from Insight Data Engineering.

### Requirements
Assumptions:
1. pip is already present on the machine this is being tested on.
2. The code is being run from the home directory of the project
3. The first line of the batch file and stream file is a header.

Run:


Simply do ``` ./run.sh``` from the **home directory** of the project and it will populate the output files. It also takes care of installing the requirements.

### Algorithm
1. Create a graph from the batch payment data.
2. When evaluating the stream payment:
	1. Get the distance between the two nodes. For that, I use [Djikstra's shortest path algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). This is an umbrella step that generalizes well to different graph sizes and topologies.
	2. I use the above to implement all three features. For example, for feature 2, I check if the distance between the two nodes is less than or equal to 2.
3. After processing the information from each payment from the stream data, I add it into the graph (if it isn't already).


### Features
1. Speed:
	1. The processing time of each stream data line is in the order of milli-seconds. This was implemented on a MacBook Pro with 8 GB RAM.
	2. This allows me to replicate the real world data engineering scenario, where in order to keep up with the incoming data, the ingestion and throughput should be at par.
2. Generalizability:
	1. Using Graph as an abstraction allows us to perform various searches on the data. This would be a harder and less efficient implementation with other data structures.
	2. Djikstra's algorithm is one of the most common and efficient algorithms for finding shortest path between two nodes. This allows us greater generalizability as the size and topologies of the graph changes.
	3. In a real world scenario, we can use a graph database for speeding up the searches.
