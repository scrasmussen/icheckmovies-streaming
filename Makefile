lc=python3
file=check_streaming.py

all: run

run:
	${lc} ${file}

clean:
	rm -f *~
