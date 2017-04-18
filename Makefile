none: help

help:
	@echo "DiamondQuest: A math mining adventure."
	@echo
	@echo "run            Run DiamondQuest directly from this repository."
	@echo "lint           Run pylint3 on the DiamondQuest package."
	@echo "test           Run pytests for DiamondQuest."


lint:
	@pylint3 --rcfile=pylintrc diamondquest

run:
	@python3 -m diamondquest

test:
	@python3 -m pytest elements


.PHONY: lint run test
