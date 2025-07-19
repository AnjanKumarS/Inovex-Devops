# Inovex Unified Flask Application

## Overview
Inovex is a modular, scalable software platform designed to empower startups and enterprises with cloud-native digital solutions. This unified version combines all backend services and the frontend into a single Flask application for simplicity and ease of deployment.

## Features
- Unified Flask backend (Python)
- Modular frontend (HTML, CSS, JS) served by Flask
- Admin and user dashboards
- Single SQLite database for all data
- Easy local development and deployment
- Dockerized for containerized deployment
- Kubernetes manifests for orchestration
- Jenkinsfile for CI/CD automation

## Navigation Bar & Use Cases
The website features a consistent navigation bar across all pages, providing quick access to major sections:

- **Home** (`/`): Landing page introducing Inovexa and its mission.
- **Services** (`/services`): Overview of all digital solutions and services offered.
- **Industries** (`/industries`): Information about industries served and relevant case studies.
- **About Us** (`/about`): Details about the company, vision, and team.
- **Careers** (`/careers`): Explore open positions and submit job applications.
- **Contact** (`/contact`): Contact form for inquiries, support, or partnership opportunities.
- **Admin Login** (`/admin-page`): Secure portal for administrators to manage the platform.

Each link in the navbar is designed to help users quickly navigate to the relevant section, whether they are prospective clients, job seekers, or administrators.

## Database
- The app uses a single SQLite database: `inovex_app/inovex.db`.
- All data (users, contacts, applications, etc.) is stored here.

## How to Clone and Run the Project

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd Inovex/inovex_app
   ```
2. **(Optional) Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Linux/Mac
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Flask application:**
   ```sh
   python app.py
   ```
5. **Access the website:**
   Open your browser and go to `http://localhost:5000`

---

## Docker Usage

### Build the Docker Image
```sh
cd inovex_app
# Build the Docker image
docker build -t inovex-app .
```

### Run the Docker Container
```sh
docker run -p 5000:5000 inovex-app
```

The app will be available at [http://localhost:5000](http://localhost:5000).

---

## Kubernetes Deployment

Kubernetes manifests are provided in the `k8s/` directory.

### Deploy to Kubernetes
1. Ensure your Docker image is available to your cluster (push to Docker Hub or load into Minikube).
2. Apply the manifests:
   ```sh
   kubectl apply -f k8s/flask-deployment.yaml
   kubectl apply -f k8s/flask-service.yaml
   ```
3. Check pod status:
   ```sh
   kubectl get pods
   ```
4. Access the app via the NodePort specified in the service manifest (default: 30007):
   - For Minikube: `minikube ip` + `:30007`
   - For Docker Desktop: `localhost:30007`

---

## CI/CD with Jenkins

A `Jenkinsfile` is included for automating build, test, and deployment steps.

### Example Jenkins Pipeline Steps
- Build Docker image
- Run tests
- Push image to registry
- Deploy to Kubernetes

### To use Jenkins:
1. Set up a Jenkins server with Docker and Kubernetes plugins.
2. Configure credentials for your Docker registry and Kubernetes cluster.
3. Add this repository as a Jenkins project (Pipeline type).
4. Jenkins will automatically use the `Jenkinsfile` for pipeline steps.

---

## Team
- Anjan Kumar S (CEO & Founder)
- Roshan Ameen (Chief Technology Officer)
- Rahul Dev (Technical Advisor)

## License
© 2025 Inovexa. All rights reserved.

---

**Note:** To run the application, navigate to the inovex_app directory and use the following command:
```sh
python app.py
```