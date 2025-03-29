pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''#!/bin/bash
                echo 'In C or Java, we can compile our program in this step'
                echo 'In Python, we can build our package here or skip this step'
                '''
            }
        }
        
        stage('Test') {
            steps {
                sh '''#!/bin/bash
                echo 'Test Step: We run testing tool like pytest here'

                # Initialize Conda
                source /opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh

                # Activate the Conda environment
                conda activate mlip

                # Run pytest inside the Conda environment
                pytest || { echo "pytest failed"; exit 1; }

                echo 'pytest completed successfully'
                '''
            }
        }


        stage('Deploy') {
            steps {
                echo 'In this step, we deploy our porject'
                echo 'Depending on the context, we may publish the project artifact or upload pickle files'
            }
        }
    }
}
