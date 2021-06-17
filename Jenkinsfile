pipeline {
  agent any

  stages {
      
    stage('Clean Workspace') {
      steps {
        // Clean the workspace
        echo "Clean" 
      }
    }

    stage('Build') {
      steps {
          echo "Build"
        sh "pip install -r requirements.txt"
        // build, build stages can be made in parallel aswell
        // build stage can call other stages
        // can trigger other jenkins pipelines and copy artifact from that pipeline
      }
    }

    stage('Test') {
      steps {
        // Test (Unit test / Automation test(Selenium/Robot framework) / etc.)
        echo "Testing"
        sh "python -m pytest  -v -s  --alluredir=localReport"
   
      }
    }

    stage('Deploy') {
      steps {
          echo "Deploy"
        // Deploy to cloud providers /local drives /artifactory etc.
        // Deploy to Deploy/prod /test/ etc
      }
    }
  }

  post {
    success {
      echo "SUCCESS"
      echo "${env.BUILD_ID} on ${env.JENKINS_URL}"
    }
    failure {
      echo "FAILURE"
      echo "${env.BUILD_ID} on ${env.JENKINS_URL}"
    }
    changed {
      echo "Status Changed: [From: $currentBuild.previousBuild.result, To: $currentBuild.result]"
    }
  }
}
