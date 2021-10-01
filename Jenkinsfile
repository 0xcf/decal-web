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
    stage('check-gh-trust') {
      steps {
        checkGitHubAccess('0xcf')
      }
    }

    stage('bundle') {
      steps {
        sh 'make bundle'
      }
    }

    stage('build') {
      steps {
        echo "${env.BRANCH_NAME}"
        sh 'make build'
      }
    }

    stage('deploy') {
      when {
        branch 'master'
      }
      steps {
        sshagent (credentials: ['decal-ssh-key']) {
          sh 'make deploy'
        }
      }
    }
  }

  post {
    failure {
      emailNotification('decal+jenkins@ocf.berkeley.edu')
    }
    always {
      node(label: 'slave') {
        ircNotification('#decal-spam')
      }
    }
  }
}

// vim: ft=groovy
