LISTEN_IP := 0.0.0.0
RANDOM_PORT := $(shell expr $$(( 8000 + (`id -u` % 1000) + 2 )))
DEPLOY_DIR := public_html

.PHONY: dev
dev: bundle
	bundle exec jekyll serve --host $(LISTEN_IP) -P $(RANDOM_PORT)

.PHONY: local-dev
local-dev: LISTEN_IP=127.0.0.1
local-dev: dev

.PHONY: local-dev
local-dev: bundle
	bundle exec jekyll serve

.PHONY: bundle
bundle:
	bundle config set --local deployment 'true'&&bundle install

.PHONY: build
build:
	bundle exec jekyll build --verbose --trace

.PHONY: clean
clean:
	rm -rf .bundle vendor

.PHONY: deploy
deploy:
	ssh -o StrictHostKeyChecking=no decal@ssh.ocf.berkeley.edu "mkdir -p ~/$(DEPLOY_DIR)" && rsync -avzpce "ssh -o StrictHostKeyChecking=no" --del _site/ --exclude static --exclude archives decal@ssh.ocf.berkeley.edu:$(DEPLOY_DIR)

