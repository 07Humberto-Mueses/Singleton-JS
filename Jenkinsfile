pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Instalar dependencias') {
            steps {
                bat 'pip install pytest'
            }
        }
        stage('Ejecutar pruebas') {
            steps {
                bat 'pytest'
            }
        }
    }
}