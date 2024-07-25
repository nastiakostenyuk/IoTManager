# IoTManager
A simple Python application for managing IoT devices.

## Getting Started
### 1. Install Docker (if not already present):
 - Refer to the official Docker documentation for installation instructions: \
 https://docs.docker.com/engine/install/

### 2. Clone this Repository
### 3. Configure Environment Variables:
 - Create a file named .env in the project directory.
 - Use the provided .env.example file as a template for your .env configuration.
### 4. Start the Application:
 - Open a terminal or command prompt within the project directory.
 - Run the following command to build and start the application using Docker Compose:
   ```bash
   docker-compose up --build -d

## Endpoints:
#### - GET /api/devices: Retrieves a list of all devices.
#### - GET /api/devices/{id}: Retrieves a specific device by its unique identifier.
#### - POST /api/devices: Creates a new device.
#### - DELETE /api/devices/{id}: Deletes an existing device.
#### - PUT /api/devices/{id}: Updates an existing device.

