
all: build run

build:
	g++ -o solution solution.cpp -Wall -Wextra

run: build
	/usr/bin/time -v ./solution < sample_input.txt

clean:
	rm -f solution