# Imports
import logging
import argparse
import time
import sys
from caesar_code import caesar_code as cc
from caesar_hack import caesar_hack as hack

# Saving time to calculate time needed
startTime = time.time()

# Argparser
parser = argparse.ArgumentParser()
parser.version = "1.0"

parser.add_argument("--version", action="version")
parser.add_argument("-v", action="store_true",
                    help="Verbose")
parser.add_argument("-c", action="store",
                    help="Code to decrypt")
parser.add_argument("-a", action="store",
                    help="Alphabet to work with")
parser.add_argument("-m", action="store",
                    help="The alphabet ordered by the most commen letters")
parser.add_argument("-g", action="store_true",
                    help="Switches to graphic analyses")

args = vars(parser.parse_args())

# Verbose
log_format = "%(asctime)s [%(name)s][%(levelname)s]: %(message)s"

if args["v"]:
    logging.basicConfig(level=logging.DEBUG, format=log_format,
                        filename="log.log", filemode="w")
else:
    logging.basicConfig(level=logging.INFO, format=log_format,
                        filename="log.log", filemode="w")

log = logging.getLogger()

# Graphicsmode switch

# Set Variables to args
code = args["c"]
alphabet = args["a"]
many_char = args["m"]

log.debug("Everything Initialized")
log.debug(f"Code entered is {code}")

# Replace arg variables if they are not set
if code is None:
    log.error("No code was entered."
              + "Try to start the program with the argument -c")
    sys.exit()
if alphabet is None:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    log.debug(f"No Alphabet in arguments")
if many_char is None:
    many_char = "enisratdhulcgmobwfkzpvjyxq"
    log.debug(f"No common letters in arguments")
log.debug(f"Finished giving values")

if args["g"]:
    import matplotlib.pyplot as plt
    log.debug(f"Switching to graphics mode")
    ha = hack(code, alphabet, many_char)
    ha.count_and_sort()
    x, y = zip(*ha.sort_counts)

    # Configuring the graphic
    log.debug(f"Configuring the graphic")
    plt.title('Letters used in the code')
    plt.ylabel('How ofthen used')
    plt.xlabel("Letters")
    couleur = ['#000000', '#dbb243', '#2e42d3', '#e54fe3', '#f23434']
    plt.bar(x, y, align='center', alpha=0.6, color=couleur)
    plt.show()
else:
    # Hack the code
    ha = hack(code, alphabet, many_char)

    # Showing the messages and keys
    keys = ha.run()
    for i in keys:
        log.info(f"Keys found: {i}")
        c_code = cc(code, i, alphabet)
        msg = c_code.decrypt()
        log.info(f"Message found: {msg}")
        print(f"Message found: {msg}")

# Calculate time needed
log.info(f"---------Took {time.time() - startTime} secs to complete---------")
print(f"---------Took {time.time() - startTime} secs to complete---------")
