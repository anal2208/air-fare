pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                
                bat 'pip3 install -r requirements.txt'
                echo 'Build Done'
                
            }
        }
       
        
                stage('Run'){
                     steps{
                        bat 'streamlit run st.py'
                        echo 'Success'
            }
                }

    }
}
