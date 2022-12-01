#Binary to string converter
import sys
import pprint

def main():
    if len(sys.argv) != 2:
        print("Usage: ./main.py <binary file>")
        sys.exit(1)
    
    try:
        string = sys.argv[1].split(" ")
        print("\nConverting binary to string...\n")
        for i in string:
            print(chr(int(i,2)),end="")
        print("\n")
    except:
        print("Error: Invalid binary string")
        sys.exit(1)

if __name__ == "__main__":
    main()