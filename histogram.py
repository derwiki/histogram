from collections import defaultdict
import sys

MAX_BAR_WIDTH = 80
BIN_DIVISOR = 100

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) > 1:
        truncate_at = int(sys.argv[1])
    else:
        truncate_at = 100

    events = sorted(int(x) for x in sys.stdin)
    events_length = len(events)

    bins = defaultdict(int)
    keys = set()
    for event in events:
        key = event / BIN_DIVISOR
        bins[key] += 1
        keys.add(key)

    sorted_keys = sorted(bins.keys())
    print "{} items, {} keys".format(events_length, len(sorted_keys))

    max_bar = float(max(bins.values()))
    for i, timing_key in enumerate(sorted_keys):
        if i > truncate_at: continue

        bin_count = bins[timing_key]
        width = int(bin_count / max_bar * MAX_BAR_WIDTH)
        bucket_range = "{}-{}".format(i * BIN_DIVISOR, (i+1) * BIN_DIVISOR - 1)
        print ''.join((
          str(bucket_range).ljust(15),
          str(bin_count).ljust(5),
          '=' * width
        ))

