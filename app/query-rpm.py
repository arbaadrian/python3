#!/usr/bin/env python

from parse_args import get_program_args
from rpm_lib import check_rpm

query_args = get_program_args()

result = check_rpm(query_args.name, query_args.version)

print("Function return: {}".format(result))
