# Python CI/CD Pipeline with GitHub Actions & AWS

This project demonstrates a **CI/CD pipeline** for a simple Python Flask application using **GitHub Actions**, **Docker**, and **AWS EC2** You can watch the explanation for this project on Youtube
It’s designed for **DevOps learning, interview prep, and YouTube tutorials**.

---

## Project Overview
The application is a small **Task Manager API** built with Flask.  
It supports:
- `/` → Welcome message  
- `/tasks` → Get all tasks  
- `/tasks` (POST) → Add a task  
- `/tasks/<id>` (DELETE) → Delete a task  

The app is containerized with Docker and deployed to AWS EC2 via GitHub Actions.

---

##  Tech Stack
- **Language:** Python 3.10  
- **Framework:** Flask  
- **Testing:** Pytest  
- **CI/CD:** GitHub Actions  
- **Containerization:** Docker  
- **Deployment:** AWS EC2  

---

## Project Structure
```plaintext
python-cicd-pipeline/
│
├── app.py                 # Flask API
├── test_app.py             # Unit tests with pytest
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build file
├── .gitignore              # Ignore unnecessary files
└── .github/
    └── workflows/
        └── ci-cd.yml       # GitHub Actions pipeline
```

---

## CI/CD Pipeline Stages
The GitHub Actions workflow runs on every push to `main`:

1. **Source** → Checkout code from GitHub  
2. **Build** → Ssetup Python, environment and install dependencies 
3. **Test** → Run automated tests with Pytest  
4. **Staging** → Build Docker image  
5. **Deploy** → Deploy Docker container to AWS EC2  

---

## Run Locally
Clone the repository:
```bash
git clone https://github.com/Gaurav-Kaushal/python-cicd-pipeline.git
cd python-cicd-pipeline
```

Create virtual environment & install dependencies:
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Run the Flask app:
```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000)

---

## Run Tests
```bash
pytest
```

---

## Docker Build
```bash
docker build -t python-cicd-app .
docker run -d -p 5000:5000 python-cicd-app
```

---

## AWS Deployment (via GitHub Actions)

### Prerequisites
- AWS EC2 instance (Amazon Linux or Ubuntu)  
- Docker installed on EC2 (`sudo yum install docker -y && sudo service docker start`)  
- Security Group allowing inbound traffic on port `80`  

### GitHub Secrets
Set these secrets in your repo:  
- `AWS_ACCESS_KEY_ID`  
- `AWS_SECRET_ACCESS_KEY`  
- `AWS_EC2_IP`  

After pushing to `main`, the pipeline will:  
- Run tests  
- Build Docker image  
- SSH into EC2 and deploy the app  

---

## Use Cases
- Learning **DevOps pipelines**  
- Practicing **GitHub Actions**  
- Demonstrating **CI/CD in interviews**  
- Creating content for **YouTube tutorials**  

---

## Author
Created by [Gaurav Kaushal](https://github.com/Gaurav-Kaushal)
