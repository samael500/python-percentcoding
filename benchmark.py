#!/usr/bin/env python

import percentcoding
import urllib
import string
from timeit import Timer

LOREMIPSUM = """

[32] Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet, consectetur, adipisci[ng] velit, sed quia non numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?

[33] At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet, ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat...

"""

safe = string.uppercase + string.lowercase + string.digits + "-_.~"
unsafe = "!*'();:@&=+$,/?#[]"
safeset = set([c for c in safe]) - set([c for c in unsafe])
safe = ''.join([c for c in safeset])
codec = percentcoding.Codec(safe)

LOREMIPSUM_ENCODED = codec.encode(LOREMIPSUM)


def benchmark_percent_encode(codec):
  e = codec.encode(LOREMIPSUM)

def benchmark_percent_decode(codec):
  d = codec.decode(LOREMIPSUM_ENCODED)

def benchmark_urllib_encode():
  e = urllib.quote(LOREMIPSUM)

def benchmark_urllib_decode():
  d = urllib.unquote(LOREMIPSUM_ENCODED)


def main():

  times = 10000

  print "percentcodec.encode x %u" % times
  timer = Timer("benchmark_percent_encode(codec)", "from __main__ import benchmark_percent_encode, codec")
  print timer.timeit(times), "\n"

  print "percentcodec.decode x %u" % times
  timer = Timer("benchmark_percent_decode(codec)", "from __main__ import benchmark_percent_decode, codec")
  print timer.timeit(times), "\n"

  print "urllib.quote x %u" % times
  timer = Timer("benchmark_urllib_encode()", "from __main__ import benchmark_urllib_encode")
  print timer.timeit(times), "\n"

  print "urllib.unquote x %u" % times
  timer = Timer("benchmark_urllib_decode()", "from __main__ import benchmark_urllib_decode")
  print timer.timeit(times), "\n"


if __name__ == '__main__':
  main()
