pipeline {
    agent any

    environment {
        IMAGE_NAME = "sidhu9676/employee-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Build') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh './venv/bin/python -m py_compile app.py'
            }
        }

        stage('Docker Build') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Docker Push') {
            steps {
                sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }

        stage('Deploy Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
