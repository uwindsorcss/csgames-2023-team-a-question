
all: build run

build:
	g++ -o solution solution.cpp -Wall -Wextra

run: build
	./solution

clean:
	rm -f solution