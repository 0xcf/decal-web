pipeline {
  agent {
    label 'slave'
  }

  options {
    ansiColor('xterm')
    timeout(time: 1, unit: 'HOURS')
    disableConcurrentBuilds()
  }

  stages {
    stage('bundle') {
      sh 'make bundle'
    }

    stage('build') {
      sh 'make build'
    }

    stage('deploy') {
      sshagent (credentials: ['decal-ssh-key']) {
        sh 'make deploy'
      }
    }
  }

  post {
    failure {
      emailNotification()
    }
    always {
      node(label: 'slave') {
        ircNotification()
      }
    }
  }
}

// vim: ft=groovy
