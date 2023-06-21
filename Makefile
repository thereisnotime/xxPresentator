#!make
########################################
# xxPresentator Makefile: v1.01
#########################################

# Project Configuration
MAKE_NAME := xxPresentator
MAKE_VERSION := 1.01
IMAGE_NAME := pptx-generator
OUTPUT_FILE := output.pptx

# Define colors
COLOR_DEFAULT := \033[0m
COLOR_GREEN := \033[0;32m
COLOR_YELLOW := \033[0;33m

# Logger date format
DATE_FORMAT := "%H:%M:%S %d.%m.%Y"

define log
	@echo "$(COLOR_GREEN)[$(shell date +$(DATE_FORMAT))]$(COLOR_DEFAULT) $(COLOR_YELLOW)$(1)$(COLOR_DEFAULT)"
endef

.PHONY: help
help:
	@printf "$(COLOR_GREEN)$(MAKE_NAME) - v$(MAKE_VERSION) - available targets:$(COLOR_DEFAULT)\n\
\t$(COLOR_YELLOW)help$(COLOR_DEFAULT)         Shows the help menu$(COLOR_DEFAULT)\n\
\t$(COLOR_YELLOW)run$(COLOR_DEFAULT)          Generates the presentation$(COLOR_DEFAULT)\n\
\t$(COLOR_YELLOW)content$(COLOR_DEFAULT)      Generates content for the presentation$(COLOR_DEFAULT)\n\
\t$(COLOR_YELLOW)presentation$(COLOR_DEFAULT) Generates the presentation and open it$(COLOR_DEFAULT)\n\
\t$(COLOR_YELLOW)clean$(COLOR_DEFAULT)        Deletes all artifacts and presentation$(COLOR_DEFAULT)\n\
\t$(COLOR_YELLOW)build$(COLOR_DEFAULT)        Prepares the base image$(COLOR_DEFAULT)\n"

.PHONY: all
all: build run

.PHONY: check_image
check_image:
ifeq ($(shell docker images -q $(IMAGE_NAME)),)
	$(call log,Docker image not found, building it...)
	@$(MAKE) build
endif

.PHONY: build
build:
	$(call log,Building base Docker image...)
	docker build -t $(IMAGE_NAME) .

.PHONY: run
run: check_image
	$(call log,Creating presentation...)
	docker run --rm -v $(shell pwd):/app $(IMAGE_NAME)
	$(call log,Done! Your presentation is in $(pwd)/$(OUTPUT_FILE))

.PHONY: clean
clean:
	$(call log,Cleaning up artifacts...)
	docker image rm $(IMAGE_NAME)
	rm -rf ./$(OUTPUT_FILE)

.PHONY: content
presentation: clean build run
	$(call log,Generating content...)
	open ./$(OUTPUT_FILE)

.PHONY: presentation
presentation: clean build run
	$(call log,Opening presentation...)
	open ./$(OUTPUT_FILE)

.DEFAULT_GOAL := help