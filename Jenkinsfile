void setBuildStatus(String message, String state) {
  step([
      $class: "GitHubCommitStatusSetter",
      reposSource: [$class: "ManuallyEnteredRepositorySource", url: "https://github.com/0xcf/decal-web"],
      contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/build-status"],
      errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
      statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
  ]);
}

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
        echo "Building branch ${env.BRANCH_NAME}"
        sh 'make build'
      }
    }

    stage('deploy') {
      parallel {
        stage('building master') {
          when {
            branch 'master'
          }
          steps {
            sshagent (credentials: ['decal-ssh-key']) {
              sh 'make deploy'
            }
          }
        }
        stage('building branch') {
          when {
            not {
              branch 'master'
            }
          }
          steps {
            sshagent (credentials: ['decal-ssh-key']) {
	      sh "bundle exec jekyll build --verbose --trace --baseurl /pr/${env.BRANCH_NAME}"
              sh "make deploy DEPLOY_DIR=public_html/pr/${env.BRANCH_NAME}"
	      script {
	      
	      	if (env.CHANGE_ID) {
			ircMessage("New PR to decal-web (https://github.com/0xcf/decal-web/pull/${env.CHANGE_ID}). Hosted at https://decal.ocf.berkeley.edu/pr/${env.BRANCH_NAME}", "decal-web_PR_Notifier", "#decal-comm", "irc.ocf.berkeley.edu:6697")
	      	}
              }
            }
          }
        }
      }
    }
  }

  post {
    always {
      node(label: 'slave') {
        ircNotification('#decal-spam')
      }
    }
    success {
      setBuildStatus("Build succeeded", "SUCCESS");
    }
    failure {
      setBuildStatus("Build failed", "FAILURE");
    }
  }
}

// vim: ft=groovy
