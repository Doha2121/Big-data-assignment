This project demonstrates data processing using Docker and Python. It includes:
- Data Loading
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Visualization
- K-Means Clustering
- Automated result extraction via a Bash script

The execution is fully containerized using Docker, ensuring reproducibility and easy deployment.


# Build the Docker image
docker build -t bd-a1-image .

# Run a new container interactively
docker run -it --name bd-a1-container bd-a1-image

# List running containers
docker ps

# Copy files from the container to the local machine
docker cp bd-a1-container:/home/doc-bd-a1/res_dpre.csv bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-1.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-2.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-3.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/vis.png bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/k.txt bd-a1/service-result/

# Stop and remove the container
docker stop bd-a1-container
docker rm bd-a1-container

# Remove the Docker image 
docker rmi bd-a1-image
