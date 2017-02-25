# -*- coding: utf-8 -*-

"""Gets args from cmd line to be used with reddit query"""

import argparse

def args():
    parser = argparse.ArgumentParser(description="Command Line Arguments for Downloading reddit comments.")

    parser.add_argument("-sub", metavar="SUBREDDIT", type=str, required=True,
                        help="The subreddit to gather submissions from")

    parser.add_argument("-start", metavar="START_TIME", type=str, required=False, default=None,
                        help="The starting time range to begin gathering reddit submissions. If none is"
                             "specified, start will be the current time")

    parser.add_argument("-end", metavar="END_TIME", type=str, required=False,
			            help="The end time range for submissions to be gathered within. Required.")

    parser.add_argument("-subcount", metavar="SUBMISSION_COUNT", type=int, required=False, default=None,
                        help="The number of submissions to capture. Defaults to None if not specified"
                             "which will receive as many as are within the time range given")

    parser.add_argument("-comcount", metavar="COMMENT_COUNT", type=int, required=False, default=None,
                        help="The number of comments to capture. Defaults to None if not specified"
                             "which will receive as many as are within the time range given")


    arg = parser.parse_args()

    if not (arg.end or arg.subcount or arg.comcount):
        parser.error("Invalid Arguments: Please specify -end, -subcount or -comcount")

    return arg
