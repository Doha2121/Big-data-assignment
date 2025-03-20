# Use Ubuntu as the base image
FROM ubuntu:latest

# Set non-interactive mode to prevent prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install Python and required dependencies
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment to avoid system-wide restrictions
RUN python3 -m venv /venv

# Activate the virtual environment and install required Python libraries
RUN /venv/bin/pip install pandas numpy seaborn matplotlib scikit-learn scipy

# Set the virtual environment as the default Python environment
ENV PATH="/venv/bin:$PATH"

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1/

# Set working directory
WORKDIR /home/doc-bd-a1/

# Copy dataset from host to container
COPY Social_Network_Ads.csv /home/doc-bd-a1/

# Start with a bash shell
CMD ["/bin/bash"]
